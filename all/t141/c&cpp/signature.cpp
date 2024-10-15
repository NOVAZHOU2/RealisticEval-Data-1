/**
 * Compares two arrays to determine if they contain the same unique elements, irrespective of order.
 *
 * @param arr1 - The first array to compare. Elements can be of any type T.
 * @param arr2 - The second array to compare. Elements should be of the same type as the first array.
 * @returns - Returns true if both arrays contain the same unique elements, otherwise returns false.
 *
 * @tparam T - The type of the elements in the arrays.
 *
 */
template <typename T>
bool compareArrays(const std::vector<T>& arr1, const std::vector<T>& arr2);