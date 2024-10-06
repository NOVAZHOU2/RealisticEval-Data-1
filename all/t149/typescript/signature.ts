/**
 * Converts an HSL color value to RGB.
 * Assumes h, s, and l are contained in the set [0, 1] and
 * returns r, g, and b in the set [0, 255].
 *
 * @param hue The hue of the color (0-360)
 * @param saturation The saturation of the color (0-1)
 * @param lightness The lightness of the color (0-1)
 * @return An object containing the red, green, and blue channels.
 */
function hslToRgb(hue: number, saturation: number, lightness: number): { r: number, g: number, b: number } {
}