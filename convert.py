import glob
import os
import pathlib
from PIL import Image, ImageFilter, ImageSequence
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
    INPUT_DIR = pathlib.Path('./original/')
    OUTPUT_DIR = pathlib.Path('./edged/')

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    files = INPUT_DIR.glob('*')
    for file in tqdm(files):
        # RGBAで保存できないため、エラーになるのでスキップ
        if file.suffix == '.jpg':
            continue

        f = Image.open(file)
        duration, loop = f.info.get('duration', 0), f.info.get('loop', 0)

        frames = []
        for frame in ImageSequence.Iterator(f):
            bf = make_border(frame.convert('RGBA'), BORDER_SIZE)
            frames.append(bf)

        if len(frames) > 1:
            frames[0].save(OUTPUT_DIR / file.name, save_all=True,
                           append_images=frames[1:], optimize=False, duration=duration, loop=loop, transparency=255, disposal=2)
        else:
            frames[0].save(OUTPUT_DIR / file.name)


if __name__ == "__main__":
    main()
