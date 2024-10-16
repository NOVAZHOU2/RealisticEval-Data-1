public class LoudnessDensity {
    // written by chatgpt, lesgo
    private int findIndex(double target) {
        int left = 0;
        int right = totalMassUpToCurrentIndex.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            // Check if the middle element is the target
            if (totalMassUpToCurrentIndex[mid] == target) {
                return mid;
            }

            // Check if the target is in the left half of the array
            if (totalMassUpToCurrentIndex[mid] > target) {
                right = mid - 1;
            }
            // Check if the target is in the right half of the array
            else {
                left = mid + 1;
            }
        }

        // At this point, the target was not found in the array
        // Return the index of the element closest to the target
        // TODO check to see if this causes problems
        if (Math.abs(totalMassUpToCurrentIndex[left] - target) < Math.abs(totalMassUpToCurrentIndex[right] - target)) {
            return left;
        } else {
            return right;
        }
    }
}
