#include <iostream>
#include <filesystem>
#include <regex>
#include <vector>
#include <string>

namespace fs = std::filesystem;

void rename_files(const std::string& directory) {
    // Convert directory to Path object for easier handling
    fs::path dir_path(directory);

    if (!fs::exists(dir_path) || !fs::is_directory(dir_path)) {
        throw std::invalid_argument("The directory '" + directory + "' does not exist or is not a directory.");
    }

    // Get list of PNG files in the directory
    std::vector<fs::path> png_files;
    for (const auto& entry : fs::directory_iterator(dir_path)) {
        if (entry.is_regular_file() && entry.path().extension() == ".png") {
            png_files.push_back(entry.path());
        }
    }

    // Sort files alphabetically by their names
    std::sort(png_files.begin(), png_files.end());

    // Print the sorted list of files (for debugging)
    std::cout << "Sorted files:" << std::endl;
    for (const auto& file : png_files) {
        std::cout << file.filename().string() << std::endl;
    }

    // Rename files with sequence numbers
    std::string prev_base_name;
    int count = 1;

    std::regex re_pattern(R"((\d{3})(-\d)?(?=\.png$))");

    for (const auto& file : png_files) {
        // Extract base name without postfix and number
        std::string base_name = std::regex_replace(file.stem().string(), re_pattern, "");

        if (base_name != prev_base_name) {
            count = 1;
        }

        std::string new_filename = base_name + std::to_string(count).substr(1, 3) + ".png";
        fs::path new_file_path = file.parent_path() / new_filename;
        fs::rename(file, new_file_path);
        std::cout << "Renaming " << file.filename().string() << " to " << new_filename << std::endl;

        prev_base_name = base_name;
        ++count;
    }
}
