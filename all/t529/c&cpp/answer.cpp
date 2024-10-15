#include <iostream>
#include <fstream>
#include <nlohmann/json.hpp> // Make sure to include the nlohmann/json library

/**
 * Converts the data object to JSON format and saves it to the specified file path.
 * @param data - The data object to be converted to JSON.
 * @param outputFilePath - The file path where the JSON will be saved.
 */
void saveAsJSON(const nlohmann::json& data, const std::string& outputFilePath) {
    try {
        // Write the JSON string to the specified file path with 2-space indentation
        std::ofstream outputFile(outputFilePath);
        if (!outputFile.is_open()) {
            throw std::ios_base::failure("Unable to open file");
        }

        outputFile << data.dump(2); // 2-space indentation
        outputFile.close();

        std::cout << "Data successfully saved to " << outputFilePath << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error saving data to file: " << e.what() << std::endl;
    }
}

int main() {
    // Example usage
    nlohmann::json exampleData = {
        {"name", "John"},
        {"age", 30},
        {"city", "New York"}
    };

    saveAsJSON(exampleData, "output.json");

    return 0;
}