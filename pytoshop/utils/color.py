def color_add(base_rgba, color_rgb, alpha):
    if base_rgba[3] != 0 and alpha != 0:
        mix = [0, 0, 0, 0]
        base_alpha = base_rgba[3] / 255

        mix[3] = 1 - (1 - alpha) * (1 - base_alpha)
        mix[0] = int(color_rgb[0] * alpha / mix[3] + base_rgba[0] * base_alpha * (1 - alpha) / mix[3])
        mix[1] = int(color_rgb[1] * alpha / mix[3] + base_rgba[1] * base_alpha * (1 - alpha) / mix[3])
        mix[2] = int(color_rgb[2] * alpha / mix[3] + base_rgba[2] * base_alpha * (1 - alpha) / mix[3])
        mix[3] *= 255

        return mix
    elif alpha != 0:
        return [color_rgb[0], color_rgb[1], color_rgb[2], alpha * 255]
    else:
        return base_rgba