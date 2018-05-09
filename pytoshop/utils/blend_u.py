from math import sqrt

import numpy as np


def div0(a, b):
    with np.errstate(divide='ignore', invalid='ignore'):
        c = np.true_divide(a, b)
        c[~ np.isfinite(c)] = 0
    return c


def D(x):
    if x <= .25:
        return ((16 * x - 12) * x + 4) * x
    else:
        return sqrt(x)


def normal(top, bcg):
    return top


def multiply(top, bcg):
    return top * bcg / 255


def screen(top, bcg):
    return bcg + top - (bcg * top / 255)


def darken(top, bcg):
    return min(top, bcg)


def lighten(top, bcg):
    return max(top, bcg)


def color_dodge(top, bcg):
    if top < 255:
        return min(255, bcg / (255 - top))
    else:
        return 255


def color_burn(top, bcg):
    if top > 0:
        return 255 - min(255, (255 - bcg) / top)
    else:
        return 0


def hard_light(top, bcg):
    if top <= 127:
        return multiply(bcg, 2*top)
    else:
        return screen(bcg, 2*top - 255)


def soft_light(top, bcg):
    if top <= 127:
        return top - (255 - 2*top) * bcg * (255 - bcg)
    else:
        return bcg + (2 * top - 255) * (D(bcg / 255) * 255 - bcg)


def difference(top, bcg):
    return abs(bcg - top)


def exclusion(top, bcg):
    return bcg + top - 2*bcg*top


def blend(top, top_alpha, bcg, bcg_alpha, blend_mode=normal):
    new_alpha = top_alpha + bcg_alpha * (1 - top_alpha)

    with np.errstate(divide='ignore', invalid='ignore'):
        top_div_new = div0(top_alpha, new_alpha)

    a = (1 - top_div_new) * bcg
    b = (1 - bcg_alpha) * top
    c = bcg_alpha * blend_mode(top, bcg)
    d = (b + c)
    e = top_div_new * d

    new_color = np.uint8(a + e)

    return new_color, new_alpha
