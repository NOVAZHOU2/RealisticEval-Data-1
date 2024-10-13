#include <iostream>
#include <vector>
#include <algorithm> // For std::vector

std::vector<std::vector<int>> divide_list(const std::vector<int>& lst, int n) {
    /**
     * Divide a vector into n parts as evenly as possible. Excess elements are distributed to earlier subvectors.
     *
     * Args:
     * lst (std::vector<int>): The vector to be divided.
     * n (int): The number of parts to divide the vector into.
     *
     * Returns:
     * std::vector<std::vector<int>>: A vector containing n subvectors, where each subvector represents a part of the original vector.
     */
    // Total number of elements in the vector
    int L = lst.size();
    // Calculate the size of each part
    int base_size = L / n;
    // Calculate the number of sections that will have an additional element
    int remainder = L % n;

    std::vector<std::vector<int>> result;
    // Start index of the subvector
    int start_index = 0;

    for (int i = 0; i < n; ++i) {
        // Determine the size of the current part
        int part_size = base_size + (i < remainder ? 1 : 0);
        // Create a new subvector from the original vector
        std::vector<int> subvector(lst.begin() + start_index, lst.begin() + start_index + part_size);
        // Append the subvector to the result vector
        result.push_back(subvector);
        // Update the start index for the next part
        start_index += part_size;
    }

    return result;
}

// Example usage
int main() {
    std::vector<int> lst = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int n = 3;
    std::vector<std::vector<int>> result = divide_list(lst, n);

    // Print the result
    for (const auto& subvector : result) {
        for (int elem : subvector) {
            std::cout << elem << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}