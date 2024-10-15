package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

public class Tester {

    @Test
    public void generatesConsistentNumbersWithSameSeed() {
        SeededRandom seededRand1 = new SeededRandom(42);
        SeededRandom seededRand2 = new SeededRandom(42);

        assertEquals(seededRand1.rand(), seededRand2.rand(), 1e-10);
        assertEquals(seededRand1.rand(), seededRand2.rand(), 1e-10);
        assertEquals(seededRand1.rand(), seededRand2.rand(), 1e-10);
    }

    @Test
    public void generatesDifferentNumbersWithDifferentSeeds() {
        SeededRandom seededRand1 = new SeededRandom(42);
        SeededRandom seededRand2 = new SeededRandom(24);

        assertNotEquals(seededRand1.rand(), seededRand2.rand(), 1e-10);
    }

    @Test
    public void returnsNumbersBetween0And1() {
        SeededRandom seededRand = new SeededRandom(123456);

        for (int i = 0; i < 1000; i++) {
            double randValue = seededRand.rand();
            assertTrue(randValue >= 0);
            assertTrue(randValue < 1);
        }
    }

    @Test
    public void producesDifferentSequencesWithDifferentSeeds() {
        SeededRandom seededRand1 = new SeededRandom(123);
        SeededRandom seededRand2 = new SeededRandom(456);

        double[] sequence1 = new double[5];
        double[] sequence2 = new double[5];

        for (int i = 0; i < 5; i++) {
            sequence1[i] = seededRand1.rand();
            sequence2[i] = seededRand2.rand();
        }

        assertFalse(java.util.Arrays.equals(sequence1, sequence2));
    }

    @Test
    public void consistentSequenceWithSameSeedOverMultipleCalls() {
        SeededRandom seededRand = new SeededRandom(987654321);

        double[] sequence1 = { seededRand.rand(), seededRand.rand(), seededRand.rand() };

        // Re-initialize with the same seed to test consistency
        SeededRandom seededRand2 = new SeededRandom(987654321);
        double[] sequence2 = { seededRand2.rand(), seededRand2.rand(), seededRand2.rand() };

        assertArrayEquals(sequence1, sequence2, 1e-10);
    }
}