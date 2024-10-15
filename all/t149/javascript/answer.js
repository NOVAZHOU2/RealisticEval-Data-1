function hslToRgb(hue, saturation, lightness) {
    let r, g, b;

    if (saturation === 0) {
        // Achromatic case (saturation = 0), r, g, and b are the same.
        r = g = b = lightness; // all equal to lightness
    } else {
        // Chromatic case (saturation != 0)
        const hueToRgb = (p, q, t) => {
            if (t < 0) t += 1;
            if (t > 1) t -= 1;
            if (t < 1 / 6) return p + (q - p) * 6 * t;
            if (t < 1 / 2) return q;
            if (t < 2 / 3) return p + (q - p) * (2 / 3 - t) * 6;
            return p;
        };

        const q = lightness < 0.5 ? lightness * (1 + saturation) : lightness + saturation - lightness * saturation;
        const p = 2 * lightness - q;
        r = hueToRgb(p, q, hue / 360 + 1 / 3);
        g = hueToRgb(p, q, hue / 360);
        b = hueToRgb(p, q, hue / 360 - 1 / 3);
    }

    // Convert r, g, b from [0,1] range to [0,255] range
    return { r: Math.round(r * 255), g: Math.round(g * 255), b: Math.round(b * 255) };
}