import os
import jaklas
import pandas as pd

def load_point_cloud_data(input_folder):
    point_cloud_data = []
    print("loading and filtering")

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.laz') or filename.lower().endswith('.las'):
            file_path = os.path.join(input_folder, filename)
            df = jaklas.read_pandas(file_path)
            point_cloud_data.append(df)

            path = "C:\\Users\\ebrereton\\posikarto\\posikarto"
            output_folder = path + "\\filtered"

            # Retain roadsign (Class: 1); Remove all other classes from df
            # Filter rows with label_semantikarto equal to 1
            road_sign_df = df[df['label_semantikarto'] == 1].copy()

            # Define the output filename
            output_filename = os.path.splitext(filename)[0] + '.laz'

            # Save the filtered DataFrame using jaklas (assuming this library supports it)
            output_path = os.path.join(output_folder, output_filename)
            jaklas.write(road_sign_df, output_path)
            