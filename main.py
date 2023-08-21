# main.py

from point_cloud_loader import load_point_cloud_data
from dbscan_clustering import perform_dbscan_clustering
# from kmeans import perform_kmeans_clustering
# from feature_computation import compute_features
# from csv_writer import write_to_csv

if __name__ == '__main__':
    input_folder = "/Users/emilybrereton/posikarto/inputs"
    output_folder = "/Users/emilybrereton/posikarto/outputs"

    # Load point cloud data
    point_cloud_data = load_point_cloud_data(input_folder)

    # Perform DBSCAN clustering
    filtered_folder = "/Users/emilybrereton/posikarto/filtered"
    clustered_folder = "/Users/emilybrereton/posikarto/clustered"   
    eps = 0.5  # Adjust the epsilon parameter as needed
    min_samples = 5  # Adjust the min_samples parameter as needed
    feature_columns = ['x', 'y', 'z']  # Replace with your feature column names

    labels = perform_dbscan_clustering(filtered_folder, clustered_folder, eps, min_samples, feature_columns)


    # plot clustered data
    # plot_clustered_data(clustered_data)
    # Compute features using Jakteristics
    # feature_data = compute_features(clustered_data)

    # Write computed features to CSV files
    # write_to_csv(feature_data, output_folder)
