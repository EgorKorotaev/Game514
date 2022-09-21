import json
import os

from PIL import Image
import numpy as np


def temp_root() -> str:
    return os.path.join(os.path.dirname(__file__), os.path.pardir, "temp")


def resources_root() -> str:
    return os.path.join(os.path.dirname(__file__), os.path.pardir, "resources")


def get_resource(resource_name: str) -> str:
    return os.path.join(resources_root(), resource_name)


def load_sprites() -> dict:
    _sprites = {}

    assets_folders = os.listdir(get_resource('assets'))
    for assets_folder in assets_folders:
        _sprites[assets_folder] = {}

        assets_folder_path = f"{get_resource('assets')}{os.sep}{assets_folder}"
        assets_files = os.listdir(assets_folder_path)

        parser_config = {}
        with open(f"{assets_folder_path}{os.sep}parser_config.json") as json_parser_config:
            parser_config = json.load(json_parser_config)

        assets_files.remove('parser_config.json')
        for assets_file in assets_files:
            _sprites[assets_folder][assets_file] = {}

            assets_file_path = f"{assets_folder_path}{os.sep}{assets_file}"
            im = np.array(Image.open(assets_file_path))
            height, withe, count_color = im.shape

            for h in range(height // parser_config["h"]):
                h_s = h * parser_config["h"] + 4
                h_f = h_s + parser_config["h"] - 8
                for w in range(withe // parser_config["w"]):
                    w_s = w * parser_config["w"] + 4
                    w_f = w_s + parser_config["w"] - 8
                    _sprites[assets_folder][assets_file][f'{h}_{w}'] = im[h_s:h_f, w_s:w_f]

    return _sprites


GLOB_SPRITES = load_sprites()
