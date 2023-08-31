import os
import pandas as pd
import numpy as np

def get_position(plots_folder, roadsign_position):
    print("estimating position of roadsigns")
    center_points = []

    for filename in os.listdir(plots_folder):
        if filename.lower().endswith('.csv'):
            csv_path = os.path.join(plots_folder, filename)
            df = pd.read_csv(csv_path)  # Read the clustered CSV file
            
            if not df.empty:
                # Calculate the center point
                center_point = df[['x', 'y', 'z']].mean()

                center_points.append({'filename': filename, 'center_x': center_point['x'], 'center_y': center_point['y'], 'center_z': center_point['z']})

    # Create a DataFrame from the collected center points
    center_df = pd.DataFrame(center_points)

    # Write the center points DataFrame to a CSV file
    center_csv_path = os.path.join(roadsign_position, 'center_points.csv')
    center_df.to_csv(center_csv_path, index=False)

