package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Power function test cases.
 */
public class Tester {

    @Test
    public void testBaseCases() {
        // Test 0^0, should return 1 (by convention)
        assertEquals(1, Answer.powerTail(0, 0, 1));

        // Test x^0 for any x, should return 1
        assertEquals(1, Answer.powerTail(5, 0, 1));
        assertEquals(1, Answer.powerTail(12345, 0, 1));
    }

    @Test
    public void testPowerOfOne() {
        // Test 1^y for any y, should return 1
        assertEquals(1, Answer.powerTail(1, 5, 1));
        assertEquals(1, Answer.powerTail(1, 123, 1));
    }

    @Test
    public void testPowerOfZero() {
        // Test 0^y for any y > 0, should return 0
        assertEquals(0, Answer.powerTail(0, 5, 1));
        assertEquals(0, Answer.powerTail(0, 100, 1));
    }

    @Test
    public void testPositivePowers() {
        // Test some positive powers
        assertEquals(8, Answer.powerTail(2, 3, 1));     // 2^3 = 8
        assertEquals(81, Answer.powerTail(3, 4, 1));    // 3^4 = 81
        assertEquals(25, Answer.powerTail(5, 2, 1));     // 5^2 = 25
    }
}