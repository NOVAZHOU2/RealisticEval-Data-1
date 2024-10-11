/**
 * Implementing matrix multiplication
 *
 * @param {Array<Array<number>>} matrixA - Matrix A
 * @param {Array<Array<number>>} matrixB - Matrix B
 * @returns {Array<Array<number>>} - The result of multiplying matrixA and matrixB
 */
function matrixMultiply(matrixA, matrixB) {
    // Check if the number of columns in matrixA is equal to the number of rows in matrixB
    if (matrixA[0].length !== matrixB.length) {
        throw new Error('The number of columns in matrixA must be equal to the number of rows in matrixB');
    }

    // Initialize the result matrix with zeros
    const result = Array.from({ length: matrixA.length }, () => 
        Array.from({ length: matrixB[0].length }, () => 0)
    );

    // Perform matrix multiplication
    for (let i = 0; i < matrixA.length; i++) {
        for (let j = 0; j < matrixB[0].length; j++) {
            for (let k = 0; k < matrixB.length; k++) {
                result[i][j] += matrixA[i][k] * matrixB[k][j];
            }
        }
    }

    return result;
}