TEST_CASE("isBase64Image") {
    SECTION("should return true for a valid PNG Base64 image string") {
        std::string validPng = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA";
        REQUIRE(isBase64Image(validPng) == true);
    }

    SECTION("should return true for a valid JPEG Base64 image string") {
        std::string validJpeg = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAAAAAA";
        REQUIRE(isBase64Image(validJpeg) == true);
    }

    SECTION("should return false for a string without the image data prefix") {
        std::string invalidFormat = "data:text/plain;base64,SGVsbG8gd29ybGQ=";
        REQUIRE(isBase64Image(invalidFormat) == false);
    }

    SECTION("should return false for a string with invalid Base64 characters") {
        std::string invalidBase64 = "data:image/png;base64,invalidBase64String@#%";
        REQUIRE(isBase64Image(invalidBase64) == false);
    }

    SECTION("should return false for an empty string") {
        REQUIRE(isBase64Image("") == false);
    }

    SECTION("should return false for a null input") {
        // Since we can't pass nullptr for a std::string, we can check with an empty string or modify the function to handle nullptr
        REQUIRE(isBase64Image("") == false);  // Adjust as necessary for null handling
    }
}