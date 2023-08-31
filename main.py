from point_cloud_loader import load_point_cloud_data
from dbscan_clustering import get_planarity, perform_dbscan_clustering
from calculate_features import calculate_jakteristic_features
from get_position import get_position
from constants import FEATURE_NAMES


if __name__ == '__main__':
   
    input_folder = "C:\\Users\\ebrereton\\posikarto\\posikarto\\inputs"
    output_folder = "C:\\Users\\ebrereton\\posikarto\\posikarto\\outputs"

    # Load point cloud data
    point_cloud_data = load_point_cloud_data(input_folder)

    # compute jakteristic features
    jak_input_folder = "C:\\Users\\ebrereton\\posikarto\\posikarto\\filtered"
    features_output = "C:\\Users\\ebrereton\\posikarto\\posikarto\\jakteristics"
    feature_names = FEATURE_NAMES
    calculate_jakteristic_features(jak_input_folder, features_output, feature_names)

    planarity_output = "C:\\Users\\ebrereton\\posikarto\\posikarto\\planarity"
    get_planarity(features_output, planarity_output)

    # Perform DBSCAN clustering
    clustered_folder = "C:\\Users\\ebrereton\\posikarto\\posikarto\\clustered"
    eps = 0.5  # Adjust the epsilon parameter as needed
    min_samples = 1  # Adjust the min_samples parameter as needed
    feature_columns = ['x', 'y', 'z']  # Replace with your feature column names

    labels = perform_dbscan_clustering(planarity_output, clustered_folder, eps, min_samples, feature_columns)
    
    # get position
    plots_folder = "C:\\Users\\ebrereton\\posikarto\\posikarto\\plots"
    roadsign_position = "C:\\Users\\ebrereton\\posikarto\\posikarto\\roadsign_position"
    get_position(plots_folder, roadsign_position)