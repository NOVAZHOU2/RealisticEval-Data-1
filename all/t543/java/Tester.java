package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Tester {

    @Test
    public void testIncrementNumberInputFive() {
        assertEquals(6, incrementNumber(5));
    }

    @Test
    public void testIncrementNumberInputZero() {
        assertEquals(0, incrementNumber(0));
    }

    @Test
    public void testIncrementNumberInputNegativeThree() {
        assertEquals(-3, incrementNumber(-3));
    }

    @Test
    public void testIncrementNumberInputPointFive() {
        assertEquals(1.5, incrementNumber(0.5), 0.001);
    }

    @Test
    public void testIncrementNumberInputOne() {
        assertEquals(2, incrementNumber(1));
    }

    @Test
    public void testIncrementNumberInputNegativeOne() {
        assertEquals(-1, incrementNumber(-1));
    }
}