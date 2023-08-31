import pandas as pd
import math
import argparse

def evaluate_positions(ground_truth_df, estimated_positions_df):
    diff_df = estimated_positions_df.copy()
    diff_df[['center_x', 'center_y', 'center_z']] = estimated_positions_df[['center_x', 'center_y', 'center_z']] - ground_truth_df[['center_x', 'center_y', 'center_z']]
    return diff_df

def main(ground_truth_file_path, estimated_position_file_path):
    # Read ground truth CSV file
    ground_truth_df = pd.read_csv(ground_truth_file_path)

    # Read estimated positions CSV file
    estimated_positions_df = pd.read_csv(estimated_position_file_path)

    # Evaluate positions
    diff_df = evaluate_positions(ground_truth_df, estimated_positions_df)

    print("Difference between Ground Truth and Estimated Positions:")
    print(diff_df)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate road sign position estimations.")
    parser.add_argument("ground_truth_file_path", type=str, help="Path to the ground truth CSV file.")
    parser.add_argument("estimated_position_file_path", type=str, help="Path to the estimated position CSV file.")
    args = parser.parse_args()

    main(args.ground_truth_file_path, args.estimated_position_file_path)
