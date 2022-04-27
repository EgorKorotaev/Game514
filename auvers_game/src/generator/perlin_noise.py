import random


import PIL.Image

from generator.perlin import PerlinNoiseFactory


def get_perlin_noise_list(
    size: int = 16,
    res: int = 10,
    min_z: float = 0,
    max_z: float = 1,
    octaves: int = 1,
    seed: any = None,
) -> list[list[float]]:
    pnf = PerlinNoiseFactory(2, octaves=octaves)
    noise_img = PIL.Image.new("L", (size, size))
    noise_list = []
    for x in range(size):
        noise_list.append([])
        for y in range(size):
            n = pnf(x / res, y / res)
            value = ((n + 1) / 2 * (max_z - min_z)) + min_z
            noise_list[x].append(value)
            # print(value)
            noise_img.putpixel((x, y), int(value * 255 + 0.5))
    # noise_img.save("data/img__seed-" + str(seed) + ".png".format(0))
    return noise_list
