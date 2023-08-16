import os
import jaklas

def load_point_cloud_data(input_folder):
    point_cloud_data = []

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.laz') or filename.lower().endswith('.las'):
            file_path = os.path.join(input_folder, filename)
            df = jaklas.read_pandas(file_path)
            point_cloud_data.append(df)
            # print(df)

    return point_cloud_data