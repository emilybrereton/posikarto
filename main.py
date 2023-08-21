# main.py

from point_cloud_loader import load_point_cloud_data
from dbscan_clustering import perform_dbscan_clustering
from kmeans import perform_kmeans_clustering
# from feature_computation import compute_features
# from csv_writer import write_to_csv

if __name__ == '__main__':
    input_folder = "/Users/emilybrereton/posikarto/inputs"
    output_folder = "/Users/emilybrereton/posikarto/outputs"

    # Load point cloud data
    # point_cloud_data = load_point_cloud_data(input_folder)
    # fuss w this later
    # point_cloud_data = process_laz_files(input_folder, output_folder)

    # # Perform k-means clustering
    # kmeans_input_path = '/Users/emilybrereton/posikarto/outputs/road_signs_anotation_data_680_semantikarto_filtered.laz'
    # output_file_path = '/Users/emilybrereton/posikarto/outputs/kmeans_0.csv'
    # n_clusters = 3
    # feature_columns = ['x', 'y', 'z']
    # # clustered_data = perform_kmeans_clustering(kmeans_input_path, output_file_path, n_clusters, feature_columns)

    # # Perform DBSCAN clustering
    # # hyperparams
    dbscan_input_path = "outputs/road_signs_anotation_data_5_semantikarto_filtered.laz"
    dbscan_output_file_path = "/Users/emilybrereton/posikarto/outputs/dbscan_5.csv"
    eps = 0.5  # Adjust the epsilon parameter as needed
    min_samples = 5  # Adjust the min_samples parameter as needed
    feature_columns = ['x', 'y', 'z']  # Replace with your feature column names

    perform_dbscan_clustering(dbscan_input_path, dbscan_output_file_path, eps, min_samples, feature_columns)


    # eps = 0.1 # max distance between two samples for nbhd
    # min_samples = 5 # min num samples to form core point
    # clustered_data = perform_dbscan_clustering(point_cloud_data, eps, min_samples)

    # plot clustered data
    # plot_clustered_data(clustered_data)
    # Compute features using Jakteristics
    # feature_data = compute_features(clustered_data)

    # Write computed features to CSV files
    # write_to_csv(feature_data, output_folder)
