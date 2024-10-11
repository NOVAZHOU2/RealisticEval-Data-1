package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Tester {

    @Test
    public void testConvertHmsToMilliseconds() {
        // Test cases for the convertHmsToMilliseconds method

        // Case 1: Valid input with all parts
        assertEquals(5070000, convertHmsToMilliseconds("1h20min30s"));

        // Case 2: Valid input with only hours
        assertEquals(3600000, convertHmsToMilliseconds("1h"));

        // Case 3: Valid input with only minutes
        assertEquals(1200000, convertHmsToMilliseconds("20min"));

        // Case 4: Valid input with only seconds
        assertEquals(30000, convertHmsToMilliseconds("30s"));

        // Case 5: Invalid input with non-numeric characters
        assertNull(convertHmsToMilliseconds("1h20min30m"));

        // Case 6: Invalid input with negative values
        assertNull(convertHmsToMilliseconds("-1h20min30s"));

        // Case 7: Empty string
        assertNull(convertHmsToMilliseconds(""));

        // Add more test cases as needed
    }

    private Integer convertHmsToMilliseconds(String timeStr) {
        if (timeStr == null || timeStr.isEmpty()) {
            return null;
        }

        int hours = 0;
        int minutes = 0;
        int seconds = 0;
        boolean foundHours = false;
        boolean foundMinutes = false;
        boolean foundSeconds = false;

        String[] parts = timeStr.split("[^a-zA-Z]+");

        for (String part : parts) {
            if (part.endsWith("h")) {
                try {
                    hours = Integer.parseInt(part.substring(0, part.length() - 1));
                    foundHours = true;
                } catch (NumberFormatException e) {
                    return null;
                }
            } else if (part.endsWith("min")) {
                try {
                    minutes = Integer.parseInt(part.substring(0, part.length() - 3));
                    foundMinutes = true;
                } catch (NumberFormatException e) {
                    return null;
                }
            } else if (part.endsWith("s")) {
                try {
                    seconds = Integer.parseInt(part.substring(0, part.length() - 1));
                    foundSeconds = true;
                } catch (NumberFormatException e) {
                    return null;
                }
            }
        }

        if (!foundHours && !foundMinutes && !foundSeconds) {
            return null;
        }

        return (hours * 3600 + minutes * 60 + seconds) * 1000;
    }
}