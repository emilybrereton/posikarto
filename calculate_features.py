import os
from jakteristics import las_utils, compute_features, FEATURE_NAMES

def calculate_jakteristic_features(jak_input_folder, features_output, feature_names, search_radius=0.15):
    print("computing geometric features")
    # Create the output folder if it doesn't exist
    if not os.path.exists(features_output):
        os.makedirs(features_output)

    # Iterate through laz files in the input folder
    for filename in os.listdir(jak_input_folder):
        if filename.lower().endswith('.laz') or filename.lower().endswith('.las'):
            input_path = os.path.join(jak_input_folder, filename)
            output_path = os.path.join(features_output, filename)

            # Read XYZ data from the input file
            xyz = las_utils.read_las_xyz(input_path)

            # Compute features using Jakteristics
            features = compute_features(xyz, search_radius=0.15, feature_names=FEATURE_NAMES)
            print("features", features)
            # Write features as extra dimensions to the output file
            las_utils.write_with_extra_dims(input_path, output_path, features, FEATURE_NAMES)

