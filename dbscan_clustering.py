import os
import pandas as pd
import numpy as np
import jaklas
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from calculate_features import calculate_jakteristic_features
from jakteristics import las_utils, compute_features, FEATURE_NAMES


# method - planarity
# read jakteristics files
# remove points which >= 0.1 planarity values
def get_planarity(features_output, planarity_output):
    print("filtering for planarity")
    for filename in os.listdir(features_output):
        planarity_input_path = os.path.join(features_output, filename)
        df = jaklas.read_pandas(planarity_input_path)
        planarity = df[df['planarity'] >= 0.1].copy()

        output_filename = os.path.splitext(filename)[0] + '.laz'
        
        output_path = os.path.join(planarity_output, output_filename)
        jaklas.write(planarity, output_path)

def perform_dbscan_clustering(filtered_folder, clustered_folder, eps, min_samples, feature_columns):
    print("performing dbscan clustering")
    plot_folder = "C:\\Users\\ebrereton\\posikarto\\posikarto\\plots"

    for filename in os.listdir(filtered_folder):
        if filename.lower().endswith('.laz') or filename.lower().endswith('.las'):
            dbscan_input_path = os.path.join(filtered_folder, filename)
            dbscan_output_csv_path = os.path.join(plot_folder, filename.replace('.laz', '.csv'))
            dbscan_output_laz_path = os.path.join(clustered_folder, filename.replace('.laz', '.laz'))

            # Read the data from a file into a DataFrame
            df = jaklas.read_pandas(dbscan_input_path)

            # Check if the DataFrame is empty before proceeding
            if df.empty:
                print(f"Skipping empty file: {filename}")
                continue

            # Standardize the feature columns
            scaler = StandardScaler()
            scaled_features = scaler.fit_transform(df[feature_columns])
            df_scaled = pd.DataFrame(scaled_features, columns=feature_columns)

            # Perform DBSCAN clustering
            dbscan = DBSCAN(eps=eps, min_samples=min_samples)
            df['cluster_label'] = dbscan.fit_predict(df_scaled)

            # Calculate the average planarity for each cluster
            cluster_labels = np.unique(df['cluster_label'])
            cluster_planarity = {}

            for label in cluster_labels:
                if label == -1:
                    continue  # Skip noise points
                cluster_points = df[df['cluster_label'] == label]
                average_planarity = np.mean(cluster_points['planarity'])  # Assuming you have a 'planarity' column
                cluster_planarity[label] = average_planarity
                # print(f"Cluster {label}: Average Planarity = {average_planarity:.2f}")
            
            # Find the cluster with the highest planarity
            highest_planarity_label = max(cluster_planarity, key=cluster_planarity.get)
            
            # Keep only the cluster with the highest planarity and remove the rest
            df_highest_planarity = df[df['cluster_label'] == highest_planarity_label]

            # Save the DataFrame with cluster information to a new CSV file
            df_highest_planarity.to_csv(dbscan_output_csv_path, index=False)
            # print("DataFrame with DBSCAN cluster information saved to:", dbscan_output_csv_path)

            # Save the clustered DataFrame as a LAZ file
            jaklas.write(df, dbscan_output_laz_path)
            # print("Clustered point cloud saved to:", dbscan_output_laz_path)
            