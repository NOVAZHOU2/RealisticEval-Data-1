package org.real.temp;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Tester {

    @Test
    public void testDayOfWeekCalculation() {
        // January 1, 2024 is a Monday
        assertEquals(1, Answer.dayOfWeek(2024, 1, 1));
        
        // August 29, 2023 is a Tuesday
        assertEquals(2, Answer.dayOfWeek(2023, 8, 29));
        
        // December 25, 2022 is a Sunday
        assertEquals(7, Answer.dayOfWeek(2022, 12, 25));
        
        // November 9, 1989 is a Thursday
        assertEquals(4, Answer.dayOfWeek(1989, 11, 9));
        
        // February 29, 2000 is a Tuesday
        assertEquals(2, Answer.dayOfWeek(2000, 2, 29));
    }
}