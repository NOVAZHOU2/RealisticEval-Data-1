/**
 * Convert RGB color to HSV color.
 * For example:
 *     input: 0, 0, 255
 *     output: 240, 100, 100
 *
 * @param r The red component of the RGB color (integer between 0 and 255)
 * @param g The green component of the RGB color (integer between 0 and 255)
 * @param b The blue component of the RGB color (integer between 0 and 255)
 *
 * @return A tuple containing the HSV values (hue, saturation, value), where hue is in degrees (0-360),
 *         saturation and value are percentages (0-100).
 */
std::tuple<int, int, int> rgb_to_hsv(int r, int g, int b);