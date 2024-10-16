package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.List;

public class Tester {

    @Test
    public void testCheckDividendVariances() {
        // Test data
        List<Tuple<String, String, Double>> records = Arrays.asList(
            new Tuple<>("AAPL", "2023-10-05", 4.75),
            new Tuple<>("GOOGL", "2023-10-05", 199.99),
            new Tuple<>("AAPL", "2023-10-05", 4.80),
            new Tuple<>("MSFT", "2023-10-06", 2.99)
        );

        // Expected result
        List<Tuple<String, String>> expected = Arrays.asList(
            new Tuple<>("AAPL", "2023-10-05")
        );

        // Actual result
        List<Tuple<String, String>> actual = checkDividendVariances(records);

        // Assert the results
        assertEquals(expected, actual);
    }

    private List<Tuple<String, String>> checkDividendVariances(List<Tuple<String, String, Double>> records) {
        List<Tuple<String, String>> result = new ArrayList<>();
        Map<String, Set<Double>> tickerToAmounts = new HashMap<>();

        for (Tuple<String, String, Double> record : records) {
            String ticker = record.getFirst();
            String date = record.getSecond();
            double amount = record.getThird();

            tickerToAmounts.putIfAbsent(ticker + "-" + date, new HashSet<>());
            if (!tickerToAmounts.get(ticker + "-" + date).add(amount)) {
                result.add(new Tuple<>(ticker, date));
            }
        }

        return result;
    }

    // Helper class for tuples
    public static class Tuple<X, Y, Z> {
        private final X first;
        private final Y second;
        private final Z third;

        public Tuple(X first, Y second, Z third) {
            this.first = first;
            this.second = second;
            this.third = third;
        }

        public X getFirst() {
            return first;
        }

        public Y getSecond() {
            return second;
        }

        public Z getThird() {
            return third;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Tuple)) return false;
            Tuple<?, ?, ?> tuple = (Tuple<?, ?, ?>) o;
            return Objects.equals(first, tuple.first) &&
                   Objects.equals(second, tuple.second);
        }

        @Override
        public int hashCode() {
            return Objects.hash(first, second);
        }

        @Override
        public String toString() {
            return "(" + first + ", " + second + ")";
        }
    }
}