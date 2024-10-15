#include <iostream>
#include <string>
#include <vector>

std::string arrayBufferToString(const std::vector<uint8_t>& buffer) {
    return std::string(buffer.begin(), buffer.end());
}

int main() {
    // Example usage
    std::vector<uint8_t> buffer = {72, 101, 108, 108, 111}; // Example buffer
    std::string result = arrayBufferToString(buffer);
    std::cout << result << std::endl; // Output: Hello
    return 0;
}