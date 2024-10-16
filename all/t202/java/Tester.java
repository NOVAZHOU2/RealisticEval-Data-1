package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.junit.Assert.assertThrows;

public class Tester {

    @Test
    public void testLeapYearFebruary() {
        assertEquals(29, Answer.getDaysInMonth(2024, 2)); // 2024 is a leap year
    }

    @Test
    public void testNonLeapYearFebruary() {
        assertEquals(28, Answer.getDaysInMonth(2023, 2)); // 2023 is not a leap year
    }

    @Test
    public void testMonthWith31Days() {
        assertEquals(31, Answer.getDaysInMonth(2023, 1)); // January has 31 days
        assertEquals(31, Answer.getDaysInMonth(2023, 7)); // July has 31 days
    }

    @Test
    public void testMonthWith30Days() {
        assertEquals(30, Answer.getDaysInMonth(2023, 4)); // April has 30 days
        assertEquals(30, Answer.getDaysInMonth(2023, 11)); // November has 30 days
    }

    @Test
    public void testInvalidMonth() {
        assertThrows(IllegalArgumentException.class, () -> {
            Answer.getDaysInMonth(2023, 0); // Month less than 1
        });
        assertThrows(IllegalArgumentException.class, () -> {
            Answer.getDaysInMonth(2023, 13); // Month greater than 12
        });
    }
}