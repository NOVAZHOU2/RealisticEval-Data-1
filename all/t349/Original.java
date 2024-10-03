import java.util.ArrayList;
import java.util.List;

public class Utils<T> {
    public List<List<T>> generateCombinations(List<List<T>> inputLists) {
        List<List<T>> combinations = new ArrayList<>();
        generateCombinationsRecursive(inputLists, 0, new ArrayList<>(), combinations);
        return combinations;
    }

    private void generateCombinationsRecursive(List<List<T>> inputLists, int currentIndex,
                                               List<T> currentCombination, List<List<T>> combinations) {
        if (currentIndex == inputLists.size()) {
            // We've reached the end of all lists, add the current combination to the result
            combinations.add(new ArrayList<>(currentCombination));
            return;
        }

        List<T> currentList = inputLists.get(currentIndex);

        for (T element : currentList) {
            currentCombination.add(element); // Add the current element to the combination
            generateCombinationsRecursive(inputLists, currentIndex + 1, currentCombination, combinations);
            currentCombination.remove(currentCombination.size() - 1); // Backtrack
        }
    }
}