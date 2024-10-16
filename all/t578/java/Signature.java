/**
 * Detects whether the string is in KEBAB_CASE.
 *
 * @param input - The string to check.
 * @returns True if the string is in KEBAB_CASE, otherwise false.
 */
public boolean isKebabCase(String input) {
    // Regular expression to match KEBAB_CASE
    String kebabCaseRegex = "^[a-z]+(-[a-z]+)*$";
    return input.matches(kebabCaseRegex);
}