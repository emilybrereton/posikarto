# main.py

from point_cloud_loader import load_point_cloud_data
from dbscan_clustering import perform_dbscan_clustering
# from feature_computation import compute_features
# from csv_writer import write_to_csv

if __name__ == '__main__':
    input_folder = "C:\\Users\\ebrereton\\posikarto\\inputs"
    output_folder = "C:\\Users\\ebrereton\\posikarto\\outputs"

    # Load point cloud data
    point_cloud_data = load_point_cloud_data(input_folder)

    # Perform DBSCAN clustering
    # hyperparams
    eps = 0.1 # max distance between two samples for nbhd
    min_samples = 200 # min num samples to form core point
    clustered_data = perform_dbscan_clustering(point_cloud_data, eps, min_samples)

    # plot clustered data
    # plot_clustered_data(clustered_data)
    # Compute features using Jakteristics
    # feature_data = compute_features(clustered_data)

    # Write computed features to CSV files
    # write_to_csv(feature_data, output_folder)
