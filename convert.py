import glob
import os
from scipy.signal import convolve2d
from PIL import Image, ImageFilter
import numpy as np
from tqdm import tqdm


def make_border(f, border_size):
    gf = f.convert('LA')
    edge = gf.filter(ImageFilter.FIND_EDGES).filter(ImageFilter.SMOOTH)

    l, a = edge.split()
    _l, _a = np.full_like(a, 255), np.array(a)
    img_array = np.stack([_l, _a], 2)
    border = Image.fromarray(np.uint8(img_array), "LA")

    border_color = border.convert('RGBA')
    diff = [-border_size, border_size]
    res = f
    for xd in range(-border_size, border_size + 1):
        for yd in range(-border_size, border_size + 1):
            b = border_color.rotate(0, translate=(xd, yd))
            res = Image.alpha_composite(b, res)

    return res


def main():
    BORDER_SIZE = 2
    INPUT_DIR = './original/'
    OUTPUT_DIR = './edged/'

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    files = glob.glob(INPUT_DIR + '*')
    for filename in tqdm(files):
        f = Image.open(filename)
        bf = make_border(f, BORDER_SIZE)
        bf.save(os.path.join(OUTPUT_DIR, os.path.basename(filename)))


if __name__ == "__main__":
    main()
