def spatial_weight(spatial_diff: float, sigma_space: float) -> float:
    """
    Calculate the spatial weight based on the difference in spatial coordinates and a space standard deviation.

    The spatial weight is calculated using the formula:
    weight = exp(- (spatial_diff^2) / (2 * sigma_space^2))

    Args:
        spatial_diff (float): The difference in spatial coordinates, which is used to compute the weight.
        sigma_space (float): The standard deviation for spatial distance, affecting the spread of the weight.

    Returns:
        float: The spatial weight.
    """
