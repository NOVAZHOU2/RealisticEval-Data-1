#include <iostream>
#include <string>
#include <cctype>
#include <algorithm>

bool isSignificantNumber(const std::string& input) {
    // Check if input is empty
    if (input.empty()) {
        return false;
    }

    // Trim whitespace from the input (note: std::string does not have a built-in trim function)
    std::string trimmedInput = input;
    trimmedInput.erase(trimmedInput.begin(), std::find_if(trimmedInput.begin(), trimmedInput.end(), [](unsigned char c) { return !std::isspace(c); }));
    trimmedInput.erase(std::find_if(trimmedInput.rbegin(), trimmedInput.rend(), [](unsigned char c) { return !std::isspace(c); }).base(), trimmedInput.end());

    // Check the length
    const size_t length = trimmedInput.length();
    if (length < 5 || length > 18) {
        return false;
    }

    // Check for significant number: all characters must be digits
    // and cannot start with '0' if the length is greater than 1
    if (!std::all_of(trimmedInput.begin(), trimmedInput.end(), ::isdigit) || (length > 1 && trimmedInput[0] == '0')) {
        return false;
    }

    return true;
}

int main() {
    std::string testInput;
    std::cout << "Enter a number: ";
    std::getline(std::cin, testInput);

    if (isSignificantNumber(testInput)) {
        std::cout << "The input is a significant number." << std::endl;
    } else {
        std::cout << "The input is NOT a significant number." << std::endl;
    }

    return 0;
}