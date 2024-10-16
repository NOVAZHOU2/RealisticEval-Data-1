package org.real.temp;

import org.junit.Test;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testReverseRangeEntireVector() {
        List<Integer> v = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        Answer.reverseRange(v, 0, 4);
        List<Integer> expected = Arrays.asList(5, 4, 3, 2, 1);
        assertEquals(expected, v);
    }

    @Test
    public void testReverseSubrangeInTheMiddle() {
        List<Integer> v = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8));
        Answer.reverseRange(v, 2, 5);
        List<Integer> expected = Arrays.asList(1, 2, 6, 5, 4, 3, 7, 8);
        assertEquals(expected, v);
    }

    @Test
    public void testReverseSingleElementRange() {
        List<Integer> v = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        Answer.reverseRange(v, 2, 2);
        List<Integer> expected = Arrays.asList(1, 2, 3, 4, 5);
        assertEquals(expected, v);
    }

    @Test
    public void testReverseRangeWithInvalidIndices() {
        List<Integer> v = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        Answer.reverseRange(v, -1, 3);  // Invalid start index
        List<Integer> expected = Arrays.asList(1, 2, 3, 4, 5); // No change
        assertEquals(expected, v);
    }

    @Test
    public void testReverseRangeAtTheEndOfVector() {
        List<Integer> v = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6));
        Answer.reverseRange(v, 3, 5);
        List<Integer> expected = Arrays.asList(1, 2, 3, 6, 5, 4);
        assertEquals(expected, v);
    }
}