TEST_CASE("isKebabCase", "[kebab-case]") {
    SECTION("should return true for a valid kebab-case string") {
        REQUIRE(isKebabCase("kebab-case") == true);
    }

    SECTION("should return true for a valid kebab-case string with multiple words") {
        REQUIRE(isKebabCase("this-is-a-valid-kebab-case") == true);
    }

    SECTION("should return false for a string with uppercase letters") {
        REQUIRE(isKebabCase("Kebab-Case") == false);
    }

    SECTION("should return false for a string with consecutive hyphens") {
        REQUIRE(isKebabCase("kebab--case") == false);
    }

    SECTION("should return false for an empty string") {
        REQUIRE(isKebabCase("") == false);
    }
}