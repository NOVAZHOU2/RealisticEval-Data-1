package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertTrue;
import java.util.Arrays;
import java.util.List;

public class Tester {

    // Helper function to check if the array is sorted
    private boolean isSorted(List<Integer> arr) {
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) < arr.get(i - 1)) {
                return false;
            }
        }
        return true;
    }

    @Test
    public void testHillSort() {
        // Test case: Sort an already sorted array
        List<Integer> arr1 = Arrays.asList(1, 2, 3, 4, 5);
        hillSort(arr1);
        assertTrue(isSorted(arr1));

        // Test case: Sort an array in reverse order
        List<Integer> arr2 = Arrays.asList(5, 4, 3, 2, 1);
        hillSort(arr2);
        assertTrue(isSorted(arr2));

        // Test case: Sort an array with duplicate values
        List<Integer> arr3 = Arrays.asList(3, 1, 2, 3, 2);
        hillSort(arr3);
        assertTrue(isSorted(arr3));

        // Test case: Sort an array with all identical values
        List<Integer> arr4 = Arrays.asList(1, 1, 1, 1, 1);
        hillSort(arr4);
        assertTrue(isSorted(arr4));

        // Test case: Sort an empty array
        List<Integer> arr5 = Arrays.asList();
        hillSort(arr5);
        assertTrue(isSorted(arr5));

        // Test case: Sort an array with one element
        List<Integer> arr6 = Arrays.asList(42);
        hillSort(arr6);
        assertTrue(isSorted(arr6));

        // Test case: Sort a large random array
        List<Integer> arr7 = Arrays.asList(3, 7, 2, 5, 1, 4, 6, 0, 9, 8);
        hillSort(arr7);
        assertTrue(isSorted(arr7));
    }
}