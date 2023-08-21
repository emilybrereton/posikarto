import pandas as pd
import jaklas
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

def perform_dbscan_clustering(dbscan_input_path, dbscan_output_file_path, eps, min_samples, feature_columns):
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
    df.to_csv(dbscan_output_file_path, index=False)

    print("DataFrame with DBSCAN cluster information saved to:", dbscan_output_file_path)
    print(df["cluster_label"])
