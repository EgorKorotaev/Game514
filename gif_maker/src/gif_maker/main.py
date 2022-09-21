import json
import os
import shutil

from PIL import Image
import numpy as np


def load_tiles() -> dict:
    _tiles = {}

    assets_folders = os.listdir('assets')
    for assets_folder in assets_folders:
        _tiles[assets_folder] = {}

        assets_folder_path = f"assets{os.sep}{assets_folder}"
        assets_files = os.listdir(assets_folder_path)

        parser_config = {}
        with open(f"{assets_folder_path}{os.sep}parser_config.json") as json_parser_config:
            parser_config = json.load(json_parser_config)

        assets_files.remove('parser_config.json')
        for assets_file in assets_files:
            _tiles[assets_folder][assets_file] = {}

            assets_file_path = f"{assets_folder_path}{os.sep}{assets_file}"
            im = np.array(Image.open(assets_file_path))
            height, withe, count_color = im.shape

            for h in range(height // parser_config["h"]):
                h_s = h * parser_config["h"]
                h_f = h_s + parser_config["h"]
                for w in range(withe // parser_config["w"]):
                    w_s = w * parser_config["w"]
                    w_f = w_s + parser_config["w"]
                    _tiles[assets_folder][assets_file][f'{h}_{w}'] = im[h_s:h_f, w_s:w_f]

    return _tiles


def clear_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def safe_tiles_in_temp(_tiles: dict):
    clear_folder("temp")

    for assets_folder in _tiles:
        for assets_file in _tiles[assets_folder]:
            for im_name in _tiles[assets_folder][assets_file]:
                pil_img = Image.fromarray(_tiles[assets_folder][assets_file][im_name])
                # TODO Сделать адаптивное расширение
                pil_img.save(f"temp{os.sep}{assets_folder}_{assets_file}_{im_name}.png")


if __name__ == "__main__":
    tiles = load_tiles()
    safe_tiles_in_temp(tiles)
