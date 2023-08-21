import pandas as pd
import jaklas
from sklearn.cluster import KMeans

def perform_kmeans_clustering(kmeans_input_path, output_file_path, n_clusters, feature_columns):
    # Read the data from a file into a DataFrame
    df = jaklas.read_pandas(kmeans_input_path)

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    df['cluster_label'] = kmeans.fit_predict(df[feature_columns])

    # Get cluster centers
    cluster_centers = kmeans.cluster_centers_

    # Add cluster center information to DataFrame
    df_centers = pd.DataFrame(cluster_centers, columns=feature_columns)
    df_centers['cluster_label'] = range(n_clusters)

    # Merge cluster center information with original DataFrame
    df = df.merge(df_centers, on='cluster_label')

    # Save the DataFrame with cluster information to a new CSV file
    # df.to_csv(output_file_path, index=False)

    print("DataFrame with cluster information saved to:", output_file_path)
    print(df)
    # print(df["cluster_label"])


