package org.real.temp;

/**
 * Convert a hexadecimal string representing an unsigned integer to its corresponding unsigned integer value.
 * @param hexString the hexadecimal string to convert
 * @return the unsigned integer value
 */
public class Answer {
    public static int hexStringToUnsignedInt(String hexString) {
        return Integer.parseUnsignedInt(hexString, 16);
    }
}