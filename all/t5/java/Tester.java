package org.real.temp;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.List;
import java.util.ArrayList;

public class Tester {

    private static final List<List<Integer>> matrixMultiply(List<List<Integer>> matrixA, List<List<Integer>> matrixB) {
        // Implementation of matrixMultiply method (same as before)
        if (matrixA == null || matrixB == null || matrixA.isEmpty() || matrixB.isEmpty() || matrixA.get(0).isEmpty() || matrixB.get(0).isEmpty()) {
            return new ArrayList<>();
        }

        if (matrixA.get(0).size() != matrixB.size()) {
            throw new IllegalArgumentException(
                "The number of columns in the first matrix must be equal to the number of rows in the second matrix.");
        }

        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < matrixA.size(); i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < matrixB.get(0).size(); j++) {
                row.add(0);
            }
            result.add(row);
        }

        for (int i = 0; i < matrixA.size(); i++) {
            for (int j = 0; j < matrixB.get(0).size(); j++) {
                for (int k = 0; k < matrixB.size(); k++) {
                    result.get(i).set(j, result.get(i).get(j) + matrixA.get(i).get(k) * matrixB.get(k).get(j));
                }
            }
        }

        return result;
    }

    @Test
    public void testStandardMatrices() {
        List<List<Integer>> mat1 = new ArrayList<>();
        mat1.add(new ArrayList<>(List.of(1, 2)));
        mat1.add(new ArrayList<>(List.of(3, 4)));

        List<List<Integer>> mat2 = new ArrayList<>();
        mat2.add(new ArrayList<>(List.of(5, 6)));
        mat2.add(new ArrayList<>(List.of(7, 8)));

        List<List<Integer>> expected = new ArrayList<>();
        expected.add(new ArrayList<>(List.of(19, 22)));
        expected.add(new ArrayList<>(List.of(43, 50)));

        assertEquals(expected, matrixMultiply(mat1, mat2), "Should correctly multiply standard matrices");
    }

    @Test
    public void testIdentityMatrix() {
        List<List<Integer>> mat1 = new ArrayList<>();
        mat1.add(new ArrayList<>(List.of(1, 0)));
        mat1.add(new ArrayList<>(List.of(0, 1)));

        List<List<Integer>> mat2 = new ArrayList<>();
        mat2.add(new ArrayList<>(List.of(5, 6)));
        mat2.add(new ArrayList<>(List.of(7, 8)));

        List<List<Integer>> expected = new ArrayList<>();
        expected.add(new ArrayList<>(List.of(5, 6)));
        expected.add(new ArrayList<>(List.of(7, 8)));

        assertEquals(expected, matrixMultiply(mat1, mat2), "Multiplying by the identity matrix should yield the answer matrix");
    }

    @Test
    public void testZeroMatrix() {
        List<List<Integer>> mat1 = new ArrayList<>();
        mat1.add(new ArrayList<>(List.of(0, 0)));
        mat1.add(new ArrayList<>(List.of(0, 0)));

        List<List<Integer>> mat2 = new ArrayList<>();
        mat2.add(new ArrayList<>(List.of(5, 6)));
        mat2.add(new ArrayList<>(List.of(7, 8)));

        List<List<Integer>> expected = new ArrayList<>();
        expected.add(new ArrayList<>(List.of(0, 0)));
        expected.add(new ArrayList<>(List.of(0, 0)));

        assertEquals(expected, matrixMultiply(mat1, mat2), "Multiplying by the zero matrix should yield a zero matrix");
    }

    @Test
    public void testSquareMatrixMultiplication() {
        List<List<Integer>> mat1 = new ArrayList<>();
        mat1.add(new ArrayList<>(List.of(1, 2)));
        mat1.add(new ArrayList<>(List.of(3, 4)));

        List<List<Integer>> mat2 = new ArrayList<>();
        mat2.add(new ArrayList<>(List.of(5, 6)));
        mat2.add(new ArrayList<>(List.of(7, 8)));

        List<List<Integer>> expected = new ArrayList<>();
        expected.add(new ArrayList<>(List.of(19, 22)));
        expected.add(new ArrayList<>(List.of(43, 50)));

        assertEquals(expected, matrixMultiply(mat1, mat2), "The multiplication of two square matrices should yield the correct product");
    }

    @Test
    public void testLargeIdentityMatrix() {
        List<List<Integer>> mat1 = new ArrayList<>();
        mat1.add(new ArrayList<>(List.of(1, 0, 0)));
        mat1.add(new ArrayList<>(List.of(0, 1, 0)));
        mat1.add(new ArrayList<>(List.of(0, 0, 1)));

        List<List<Integer>> mat2 = new ArrayList<>();
        mat2.add(new ArrayList<>(List.of(5, 6, 7)));
        mat2.add(new ArrayList<>(List.of(8, 9, 10)));
        mat2.add(new ArrayList<>(List.of(11, 12, 13)));

        List<List<Integer>> expected = new ArrayList<>();
        expected.add(new ArrayList<>(List.of(5, 6, 7)));
        expected.add(new ArrayList<>(List.of(8, 9, 10)));
        expected.add(new ArrayList<>(List.of(11, 12, 13)));

        assertEquals(expected, matrixMultiply(mat1, mat2), "Multiplying by the larger identity matrix should yield the answer matrix");
    }
}