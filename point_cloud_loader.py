import os
import jaklas
import pandas as pd

def load_point_cloud_data(input_folder):
    point_cloud_data = []
    road_sign_data = [] # empty list to store filtered roadsign df

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.laz') or filename.lower().endswith('.las'):
            file_path = os.path.join(input_folder, filename)
            df = jaklas.read_pandas(file_path)
            point_cloud_data.append(df)
            # print(df)

            # Save DataFrame to a text file
            output_folder = "/Users/emilybrereton/posikarto/outputs"
            output_filename = os.path.splitext(filename)[0] + '_filtered.laz' 
            # output_path = os.path.join(output_folder, output_filename)
            
            # df.to_csv(output_path, index=False, sep='\t')  # Save as tab-separated text file

            # Retain roadsign (Class: 1); Remove all other classes from df
            # Filter rows with label_semantikarto equal to 1
            road_sign_df = df[df['label_semantikarto'] == 1].copy()
            road_sign_data.append(road_sign_df)

    # Concatenate the list of filtered DataFrames into a single DataFrame
    # note: road_sign_combined is inferred point cloud after remove all but class 1
    road_sign_combined = pd.concat(road_sign_data, ignore_index=True)
    # print(road_sign_combined)
    # road_sign_combined.to_csv(output_path, index=False, sep='\t')  # Save as tab-separated text file
    jaklas.write(road_sign_combined, str(output_filename)) # wasnt in output folder

    return road_sign_combined

# def process_laz_files(input_folder, output_folder):
#     road_sign_data = []
#     for filename in os.listdir(input_folder):
#         if filename.lower().endswith('.laz') or filename.lower().endswith('.las'):
#             file_path = os.path.join(input_folder, filename)
#             df = jaklas.read_pandas(file_path)

#             # Retain roadsigns (Class: 1); Remove all other classes from df
#             road_sign_df = df[df['label_semantikarto'] == 1].copy()

#             if not road_sign_df.empty:
#                 output_filename = os.path.splitext(filename)[0] + '_filtered.laz'
#                 output_path = os.path.join(output_folder, output_filename)
#                 jaklas.write(road_sign_df, output_path)

#         if road_sign_data:
#             road_sign_combined = pd.concat(road_sign_data, ignore_index=True)
#             return road_sign_combined
#         else:
#             return None