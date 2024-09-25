def get_translation(matrix: 'rai.typing.Affine') -> np.typing.NDArray[np.float64]:
    """
    Given an affine matrix, return the corresponding translation.
    Written by ChatGPT
    """
    return matrix[:2, 2]