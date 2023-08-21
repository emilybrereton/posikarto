import os
import pandas as pd
import jaklas
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

def perform_dbscan_clustering(filtered_folder, clustered_folder, eps, min_samples, feature_columns):
    print("clustering")
    for filename in os.listdir(filtered_folder):
        if filename.lower().endswith('.laz') or filename.lower().endswith('.las'):
            dbscan_input_path = os.path.join(filtered_folder, filename)
            dbscan_output_csv_path = os.path.join(clustered_folder, filename.replace('.laz', '_clustered.csv'))
            dbscan_output_laz_path = os.path.join(clustered_folder, filename.replace('.laz', '_clustered.laz'))

            # Read the data from a file into a DataFrame
            df = jaklas.read_pandas(dbscan_input_path)

            # Standardize the feature columns
            scaler = StandardScaler()
            scaled_features = scaler.fit_transform(df[feature_columns])
            df_scaled = pd.DataFrame(scaled_features, columns=feature_columns)

            # Perform DBSCAN clustering
            dbscan = DBSCAN(eps=eps, min_samples=min_samples)
            df['cluster_label'] = dbscan.fit_predict(df_scaled)

            # Save the DataFrame with cluster information to a new CSV file
            df.to_csv(dbscan_output_csv_path, index=False)
            # print("DataFrame with DBSCAN cluster information saved to:", dbscan_output_csv_path)

            # Save the clustered DataFrame as a LAZ file
            jaklas.write(df, dbscan_output_laz_path)
            # print("Clustered point cloud saved to:", dbscan_output_laz_path)
