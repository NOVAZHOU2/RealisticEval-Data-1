package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testOriginalStringShorterThanMaxLength() {
        String result = StringTruncator.truncateStringWithReplacement("Hello World", 20);
        assertEquals("Hello World", result);
    }

    @Test
    public void testTruncateLongStringWithEllipsis() {
        String result = StringTruncator.truncateStringWithReplacement("This is a long string that needs to be truncated.", 20);
        assertEquals("This is a long str...", result);
    }

    @Test
    public void testTruncateStringAtMaxLength() {
        String result = StringTruncator.truncateStringWithReplacement("Short string", 10);
        assertEquals("Short str...", result);
    }

    @Test
    public void testHandleEmptyString() {
        String result = StringTruncator.truncateStringWithReplacement("", 10);
        assertEquals("", result);
    }

    @Test
    public void testOriginalStringEqualToMaxLength() {
        String result = StringTruncator.truncateStringWithReplacement("Exact length", 12);
        assertEquals("Exact length", result);
    }

    @Test
    public void testSpecialCharactersInString() {
        String result = StringTruncator.truncateStringWithReplacement("This string has special characters: !@#$%^&*()", 30);
        assertEquals("This string has special c...", result);
    }

    @Test
    public void testMaxLengthZeroReturnsEllipsis() {
        String result = StringTruncator.truncateStringWithReplacement("Hello, world!", 0);
        assertEquals("...", result);
    }
}