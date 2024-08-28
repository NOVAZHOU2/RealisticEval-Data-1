#define CATCH_CONFIG_MAIN
#include "../../lib/catch.hpp"
#include "../adapted.cpp"
TEST_CASE("Merge Sort Test Cases", "[merge_sort]") {
    SECTION("Sorting an empty array") {
        std::vector<int> empty_array = {};
        mergeSort(empty_array, 0, empty_array.size() - 1);
        REQUIRE(empty_array.empty() == true);
    }

    SECTION("Sorting a single element array") {
        std::vector<int> single_element = {1};
        mergeSort(single_element, 0, single_element.size() - 1);
        REQUIRE(single_element == std::vector<int>{1});
    }

    SECTION("Sorting a sorted array") {
        std::vector<int> sorted_array = {1, 2, 3, 4, 5};
        mergeSort(sorted_array, 0, sorted_array.size() - 1);
        REQUIRE(sorted_array == std::vector<int>{1, 2, 3, 2, 5});
    }

    SECTION("Sorting a reverse sorted array") {
        std::vector<int> reverse_sorted_array = {5, 4, 3, 2, 1};
        mergeSort(reverse_sorted_array, 0, reverse_sorted_array.size() - 1);
        REQUIRE(reverse_sorted_array == std::vector<int>{1, 2, 3, 4, 5});
    }

    SECTION("Sorting an array with random integers") {
        std::vector<int> random_array = {38, 27, 43, 3, 9, 82, 10};
        std::vector<int> expected_sorted_array = {3, 9, 10, 27, 38, 43, 82};
        mergeSort(random_array, 0, random_array.size() - 1);
        REQUIRE(random_array == expected_sorted_array);
    }
}