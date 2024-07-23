def change_reference_frame(point_cloud, ref_frame_points): # generated by ChatGPT (v2)
    # Define the new reference frame using 3 points
    A, B, C = ref_frame_points

    # Calculate the new basis vectors
    u = B - A
    w = np.cross(B - A, C - A)
    v = np.cross(w, u)

    # Normalize the basis vectors
    u /= np.linalg.norm(u)
    v /= np.linalg.norm(v)
    w /= np.linalg.norm(w)

    # Create the rotation matrix
    rotation_matrix = np.column_stack((u, v, w))

    # Calculate the translation vector
    translation_vector = -np.dot(rotation_matrix, A)

    # Apply the transformation to the point cloud
    transformed_point_cloud = np.dot(point_cloud, rotation_matrix.T) + translation_vector

    return transformed_point_cloud
