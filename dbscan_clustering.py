import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import DBSCAN

def perform_dbscan_clustering(point_cloud_data, eps, min_samples):
    clustered_data = []

    save_folder = "C:\\Users\\ebrereton\\posikarto\\clusters"
    output_csv_path = "C:\\Users\\ebrereton\\posikarto\\clusters\\reformatted_clustered_data_3.csv"


    for df in point_cloud_data:
        # extract features from df
        # apply dbscan
        db = DBSCAN(eps=eps, min_samples=min_samples).fit(df[['x', 'y', 'z']])
        
        # store labels and cluster centers in data struct
        clustered_data.append({'labels': db.labels_, 'cluster_centers': db.components_})
        print("Clustered data:", clustered_data)

    # txt_filename = f'clustered_data.csv'
    # txt_path = save_folder + "\\" + txt_filename
    # with open(txt_path, 'w') as txt_file:
    #     txt_file.write(pd.DataFrame(clustered_data).to_string())
      # Create a list to store the reformatted data
    reformatted_data = []

    # Iterate through the clustered data and extract information
    for data in clustered_data:
        labels = data['labels']
        cluster_centers = data['cluster_centers']
        for label, center in zip(labels, cluster_centers):
            x, y, z = center
            reformatted_data.append({'labels': label, 'x': x, 'y': y, 'z': z})

    # Create a DataFrame from the reformatted data
    final_df = pd.DataFrame(reformatted_data)

    # Save the DataFrame to a CSV file
    final_df.to_csv(output_csv_path, index=False)

    # return clustered_data
    return final_df



# def plot_clustered_data(clustered_data):
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection = '3d')

#     for cluster_data in clustered_data:
#         labels = cluster_data['labels']
#         cluster_centers = cluster_data['cluster_centers']

#         unique_labels = np.unique(labels)
#         for label in unique_labels:
#             # if label == -1:
#             #     ax.scatter(cluster_centers[label == labels][:, 0],
#             #                cluster_centers[label == labels][:, 1],
#             #                cluster_centers[label == labels][:, 2], marker='o', s=30, label='Noise')
#             # else:
#             #     ax.scatter(cluster_centers[label == labels][:, 0],
#             #                cluster_centers[label == labels][:, 1],
#             #                cluster_centers[label == labels][:, 2], marker='o', s=30, label=f'Cluster {label}')
#             if label == -1:
#                 noise_points = cluster_centers[labels == label]
#                 ax.scatter(noise_points[:, 0], noise_points[:, 1], noise_points[:, 2], marker='o', s=30, label='Noise')
#             else:
#                 cluster_points = cluster_centers[labels == label]
#                 ax.scatter(cluster_points[:, 0], cluster_points[:, 1], cluster_points[:, 2], marker='o', s=30, label=f'Cluster {label}')

#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Z')
#     ax.set_title('DBSCAN Clustering Results')
#     ax.legend()

#     plt.show()