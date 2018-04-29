import numpy as np


def blend(top, top_alpha, bcg, bcg_alpha, blend_mode):
    new_alpha = top_alpha + bcg_alpha * (1 - top_alpha)

    a = (1 - top_alpha / new_alpha) * bcg
    b = (1 - bcg_alpha) * top
    c = bcg_alpha * blend_mode(top, bcg)
    d = (b + c)
    e = top_alpha / new_alpha * d

    new_color = np.uint8(a + e)
    return new_color, new_alpha


def normal(top, bcg):
    return bcg


def multiply(top, bcg):
    return top * bcg