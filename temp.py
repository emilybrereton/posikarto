import pandas as pd
import jaklas

# Path to the saved text file
input_file_path = 'C:\\Users\\ebrereton\\posikarto\\posikarto\\jakteristics\\road_signs_anotation_data_1_semantikarto_filtered_clustered.laz'
df = jaklas.read_pandas(input_file_path)
# Read the DataFrame from the text file
# road_sign_dataframe = pd.read_csv(input_file_path, sep='\t')


# Extract the label_semantikarto column as a separate DataFrame
# label_column = road_sign_dataframe[['label_semantikarto']]

# Save the label_semantikarto column to a CSV file
output_csv_path = 'C:\\Users\\ebrereton\\posikarto\\posikarto\\outputs\\clustered_roadsign1.csv'
df.to_csv(output_csv_path, index=False)