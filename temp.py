import pandas as pd

# Path to the saved text file
input_file_path = '/Users/emilybrereton/posikarto/outputs/road_signs_anotation_data_680_semantikarto_filtered.txt'

# Read the DataFrame from the text file
road_sign_dataframe = pd.read_csv(input_file_path, sep='\t')

# Extract the label_semantikarto column as a separate DataFrame
label_column = road_sign_dataframe[['label_semantikarto']]

# Save the label_semantikarto column to a CSV file
output_csv_path = '/Users/emilybrereton/posikarto/outputs/just_label_semantikarto.csv'
label_column.to_csv(output_csv_path, index=False)