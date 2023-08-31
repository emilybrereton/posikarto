import laspy
import jaklas
import pandas as pd
import math
import argparse

def read_las_file(las_file_path):
    df = jaklas.read_pandas(las_file_path)
    # print("df: ", df)
    return df

def normalize_coordinates(df):
    centroid = df[['x', 'y', 'z']].mean()
    df['x'] -= centroid['x']
    df['y'] -= centroid['y']
    df['z'] -= centroid['z']
    max_distance = max(df[['x', 'y', 'z']].apply(lambda row: row.dot(row), axis=1))
    scaling_factor = 1.0 / math.sqrt(max_distance)
    df['x'] *= scaling_factor
    df['y'] *= scaling_factor
    df['z'] *= scaling_factor
    # print(df)
    return df

def calculate_average_coordinates(df):
    average_x = df['x'].mean()
    average_y = df['y'].mean()
    average_z = df['z'].mean()
    return pd.DataFrame({'x': [average_x], 'y': [average_y], 'z': [average_z]})

def evaluate_positions(ground_truth_df, estimated_positions_df):
    diff_df = estimated_positions_df.copy()
    gt_df = ground_truth_df.reset_index(drop=True)
    x_diff = estimated_positions_df['center_x'] - gt_df['x']
    y_diff = estimated_positions_df['center_y'] - gt_df['y']
    z_diff = estimated_positions_df['center_z'] - gt_df['z']
    diff_df = [x_diff, y_diff, z_diff]
    
    return diff_df

def main(las_file_path, estimated_position_file_path):
    # Read LAS file and create DataFrame
    original_df = read_las_file(las_file_path)

    # Normalize coordinates to get ground truth
    # ground_truth_df = normalize_coordinates(original_df)
    ground_truth_df = calculate_average_coordinates(original_df)


    # # Read estimated positions CSV file
    estimated_positions_df = pd.read_csv(estimated_position_file_path)

    # # Evaluate positions
    diff_df = evaluate_positions(ground_truth_df, estimated_positions_df)

    # print("Difference between Ground Truth and Estimated Positions:")
    print(diff_df)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate road sign position estimations.")
    parser.add_argument("las_file_path", type=str, help="Path to the LAS/LAZ file.")
    parser.add_argument("estimated_position_file_path", type=str, help="Path to the estimated position CSV file.")
    args = parser.parse_args()

    main(args.las_file_path, args.estimated_position_file_path)
