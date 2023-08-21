# Calculate Jakteristics features for each cluster
def calculate_jakteristics_features(point_cloud, labels):
    unique_labels = np.unique(labels)
    
    for label in unique_labels:
        if label == -1:  # Skip noise points (outliers)
            continue
        
        cluster_indices = np.where(labels == label)[0]
        cluster_points = point_cloud[cluster_indices]
        
        features = jakteristics.compute_features(cluster_points)
        
        # Print or store the features for further analysis
        print(f"Cluster {label} Features:")
        print(features)