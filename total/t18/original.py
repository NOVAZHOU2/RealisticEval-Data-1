import colorsys

def float2color(f):
    """
    Interpolate float to red-green using HSV.
    Code generated by ChatGPT.
    """
    # Ensure the input is in the valid range [0, 1]
    f = max(0, min(1, f))

    # Calculate the hue (ranging from 0 to 120) based on the input float
    hue = 120 * f

    # Convert the HSV color to RGB
    r, g, b = colorsys.hsv_to_rgb(hue/360, 1.0, 1.0)

    # Scale the RGB values to 8-bit integers (0 to 255)
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)

    # Convert the RGB values to a hexadecimal string
    hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)

    return hex_color