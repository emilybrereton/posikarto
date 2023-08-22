import os
from jakteristics import las_utils, compute_features, FEATURE_NAMES

def calculate_jakteristic_features(jak_input_folder, features_output, feature_names, search_radius=0.15):
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
            features = compute_features(xyz, search_radius=0.15, feature_names=["planarity"])

            # Write features as extra dimensions to the output file
            las_utils.write_with_extra_dims(input_path, output_path, features, feature_names)


# from jakteristics import las_utils, compute_features, FEATURE_NAMES

# input_path = "C:\\Users\\ebrereton\\posikarto\\posikarto\\clustered\\road_signs_anotation_data_1_semantikarto_filtered_clustered.laz"
# xyz = las_utils.read_las_xyz(input_path)

# features = compute_features(xyz, search_radius=0.15, feature_names=FEATURE_NAMES)

# output_path = "C:\\Users\\ebrereton\\posikarto\\posikarto\\jakteristics\\testtest.las"
# las_utils.write_with_extra_dims(input_path, output_path, features, FEATURE_NAMES)

# # or for a specific feature:
# omnivariance = compute_features(xyz, search_radius=0.15, feature_names=["omnivariance"])
# output_omnivariance = "C:\\Users\\ebrereton\\posikarto\\posikarto\\jakteristics\\output_omnivariance.las"
# las_utils.write_with_extra_dims(input_path, output_omnivariance, omnivariance, ["omnivariance"])