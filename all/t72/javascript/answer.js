function get3DCoordinates(K, d, x, y) {
    /*
     * Converts 2D pixel coordinates into 3D world coordinates using camera intrinsic parameters and depth.
     * @param {Array} K - Camera intrinsic matrix.
     * @param {number} d - Depth (distance along z-axis).
     * @param {number} x - Pixel x-coordinate.
     * @param {number} y - Pixel y-coordinate.
     * @returns {Array} - 3D point coordinates in camera RDF coordinates [x, y, z].
     */

    // Calculate the inverse of K matrix
    const invK = invertMatrix(K);

    // Convert pixel coordinates to normalized image coordinates
    const u = (x - K[0][2]) / K[0][0];
    const v = (y - K[1][2]) / K[1][1];

    // Calculate the 3D point coordinates
    const x3D = d * u;
    const y3D = d * v;
    const z3D = d;

    return [x3D, y3D, z3D];
}

// Helper function to calculate the inverse of a 3x3 matrix
function invertMatrix(matrix) {
    const det = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
              - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
              + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]);

    if (det === 0) throw new Error('Matrix is not invertible');

    const invDet = 1 / det;

    return [
        [(matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) * invDet,
         -(matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1]) * invDet,
          (matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]) * invDet],

        [-(matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) * invDet,
         (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]) * invDet,
         -(matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0]) * invDet],

        [(matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]) * invDet,
         -(matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0]) * invDet,
          (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) * invDet]
    ];
}