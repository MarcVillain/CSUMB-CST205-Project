def color_add_rgb(base_rgba, color_rgb, alpha):
    return color_add_rgba(base_rgba, [color_rgb[0], color_rgb[1], color_rgb[2], alpha*255])


def color_add_rgba(base_rgba, add_rgba):
    if base_rgba[3] != 0 and add_rgba[3] != 0:
        mix = [0, 0, 0, 0]
        base_alpha = base_rgba[3] / 255
        add_alpha = add_rgba[3] / 255

        mix[3] = 1 - (1 - add_alpha) * (1 - base_alpha)
        mix[0] = int(add_rgba[0] * add_alpha / mix[3] + base_rgba[0] * base_alpha * (1 - add_alpha) / mix[3])
        mix[1] = int(add_rgba[1] * add_alpha / mix[3] + base_rgba[1] * base_alpha * (1 - add_alpha) / mix[3])
        mix[2] = int(add_rgba[2] * add_alpha / mix[3] + base_rgba[2] * base_alpha * (1 - add_alpha) / mix[3])
        mix[3] *= 255

        return mix
    elif add_rgba[3] != 0:
        return add_rgba
    else:
        return base_rgba
