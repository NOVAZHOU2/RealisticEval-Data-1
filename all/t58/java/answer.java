package org.real.temp;

import java.math.BigDecimal;
import java.math.RoundingMode;

public class Answer {

    public static double probabilityOfRedBalls(int n, int x, int y) {
        /*
         * Calculate the probability that n red balls will be drawn when 15 balls are randomly returned from a jar containing x red balls and y blue balls.
         *
         * @param n Number of red balls to be drawn.
         * @param x Number of red balls in the jar.
         * @param y Number of blue balls in the jar.
         * @return The probability of drawing exactly n red balls.
         */
        if (n > 15 || n < 0 || x < 0 || y < 0) {
            throw new IllegalArgumentException("Invalid input values");
        }

        BigDecimal totalWays = factorial(15).divide(factorial(15 - n).multiply(factorial(n)), 20, RoundingMode.HALF_UP);
        BigDecimal redWays = factorial(x).divide(factorial(x - n).multiply(factorial(n)), 20, RoundingMode.HALF_UP);
        BigDecimal blueWays = factorial(y).divide(factorial(y - 15 + n).multiply(factorial(15 - n)), 20, RoundingMode.HALF_UP);

        return redWays.multiply(blueWays).divide(totalWays, 20, RoundingMode.HALF_UP).doubleValue();
    }

    private static BigDecimal factorial(int number) {
        BigDecimal result = BigDecimal.ONE;
        for (int i = 2; i <= number; i++) {
            result = result.multiply(BigDecimal.valueOf(i));
        }
        return result;
    }
}