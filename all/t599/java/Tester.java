package org.real.temp;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Tester class to validate the functionality of MaxHeap.
 */
public class Tester {
    private MaxHeap maxHeap;

    /**
     * Set up a new MaxHeap instance before each test.
     */
    @Before
    public void setUp() {
        maxHeap = new MaxHeap();
    }

    /**
     * Test the initial state of the heap.
     */
    @Test
    public void testInitialState() {
        assertTrue(maxHeap.isEmpty());
        assertEquals(0, maxHeap.size());
    }

    /**
     * Test inserting elements into the heap.
     */
    @Test
    public void testInsertElements() {
        maxHeap.insert(10);
        maxHeap.insert(20);
        maxHeap.insert(5);

        assertFalse(maxHeap.isEmpty());
        assertEquals(3, maxHeap.size());
        assertEquals(20, maxHeap.getMax()); // The maximum should be 20
    }

    /**
     * Test extracting the maximum element from the heap.
     */
    @Test
    public void testExtractMax() {
        maxHeap.insert(10);
        maxHeap.insert(30);
        maxHeap.insert(20);

        int maxElement = maxHeap.extractMax();
        assertEquals(30, maxElement); // The maximum extracted should be 30
        assertEquals(20, maxHeap.getMax()); // The next maximum should be 20
        assertEquals(2, maxHeap.size()); // Size should be 2 after extraction
    }

    /**
     * Test that the heap maintains the max heap property after multiple operations.
     */
    @Test
    public void testMaxHeapProperty() {
        maxHeap.insert(15);
        maxHeap.insert(10);
        maxHeap.insert(30);
        maxHeap.insert(20);
        maxHeap.insert(25);

        // Current max should be 30
        assertEquals(30, maxHeap.getMax());

        maxHeap.extractMax(); // Remove 30
        // After removal, the new max should be 25
        assertEquals(25, maxHeap.getMax());

        maxHeap.extractMax(); // Remove 25
        // After removal, the new max should be 20
        assertEquals(20, maxHeap.getMax());

        // The size of the heap should be 3 now
        assertEquals(3, maxHeap.size());
    }
}