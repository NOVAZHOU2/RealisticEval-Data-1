package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {

    /**
     * Implement decryption based on polynomials and keys.
     * 
     * @param degree The highest degree of a polynomial is added by one.
     * @param modulus Modulus to use when encrypting the question.
     * @param key An array of encrypted keys.
     * @param encryptedData An array of encrypted question.
     * @return Decrypted question as a List of integers.
     */
    public static List<Integer> performPolynomialDecryption(int degree, int modulus, List<Integer> key, List<Integer> encryptedData) {
        // Decrypts the polynomial based encryption by reversing the encryption steps
        List<Integer> decryptedData = new ArrayList<>();

        for (int index = 0; index < degree; index++) {
            // Calculate the decrypted value considering positive modulus range
            int decryptedValue = (encryptedData.get(index) - key.get(index)) % modulus;
            
            // Adjust for Java's behavior with negative numbers
            if (decryptedValue < 0) {
                decryptedValue += modulus;
            }
            
            decryptedData.add(decryptedValue);
        }

        return decryptedData;
    }

    public static void main(String[] args) {
        // Example usage
        int degree = 3;
        int modulus = 26;
        List<Integer> key = new ArrayList<>();
        key.add(5);
        key.add(11);
        key.add(17);

        List<Integer> encryptedData = new ArrayList<>();
        encryptedData.add(10);
        encryptedData.add(20);
        encryptedData.add(30);

        List<Integer> decryptedData = performPolynomialDecryption(degree, modulus, key, encryptedData);
        System.out.println("Decrypted Data: " + decryptedData);
    }
}