from scipy.signal import convolve2d
from PIL import Image, ImageFilter
import numpy as np


def make_border(f, border_size):
    """
    Edge emoji with white.
    """
    assert border_size > 0

    gf = f.convert('LA')
    edge = gf.filter(ImageFilter.FIND_EDGES).filter(ImageFilter.SMOOTH)
    l, a = edge.split()
    _l = l.point(lambda x: 255)
    border = Image.merge("LA", (_l, a))

    border_color = border.convert('RGBA')
    diff = [-border_size, border_size]
    res = f
    for xd in range(-border_size, border_size + 1):
        for yd in range(-border_size, border_size + 1):
            b = border_color.rotate(0, translate=(xd, yd))
            res = Image.alpha_composite(b, res)

    return res


def main():
    border_size = 2
    f = Image.open('./test.png')
    bf = make_border(f, border_size)
    bf.save('./test_output.png')


if __name__ == "__main__":
    main()
