import numpy as np


def blend(top, top_alpha, bcg, bcg_alpha, blend_mode):
    top_alpha = top_alpha / 255
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


def div0(a, b):
    with np.errstate(divide='ignore', invalid='ignore'):
        c = np.true_divide(a, b)
        c[~ np.isfinite(c)] = 0
    return c


def normal(top, bcg):
    return bcg


def multiply(top, bcg):
    return top * bcg
