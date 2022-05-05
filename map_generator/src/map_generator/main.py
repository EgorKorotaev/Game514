import datetime
import json
import random

from map_generator.objects_prefab import get_z_blocks, zBlocksPrefab
from map_generator.perlin_noise import get_perlin_noise_list


def generate_from_distribution(object_distribution: list[(any, int)]) -> any:
    weight_all = sum(weight for _, weight in object_distribution)
    random_value = random.random() * weight_all
    i = 0
    for obj, weight in object_distribution:
        i += weight
        if i >= random_value:
            return obj


def get_all_the_z_blocks(given_height: int, sea_level_height: int, max_height: int, x: int, y: int):
    cells = []
    if given_height <= 0:
        blocks = get_z_blocks(zBlocksPrefab.DEEP_WATER_BLOCK)
        cells += blocks.get_z_blocks(x=x, y=y, z_start=0, given_height=sea_level_height)

        entities = get_z_blocks(zBlocksPrefab.DEEP_WATER_ENTITY)
        cells += entities.get_z_blocks(x=x, y=y, z_start=0, given_height=sea_level_height)

    elif given_height <= 1:
        blocks = get_z_blocks(zBlocksPrefab.SHOAL_BLOCK)
        cells += blocks.get_z_blocks(x=x, y=y, z_start=0, given_height=sea_level_height)

        entities = get_z_blocks(zBlocksPrefab.SHOAL_ENTITY)
        cells += entities.get_z_blocks(x=x, y=y, z_start=0, given_height=sea_level_height)

    elif given_height <= 2:
        blocks = get_z_blocks(zBlocksPrefab.BEACH_BLOCK)
        cells += blocks.get_z_blocks(x=x, y=y, z_start=0, given_height=given_height)

        entities = get_z_blocks(zBlocksPrefab.BEACH_ENTITY)
        cells += entities.get_z_blocks(x=x, y=y, z_start=given_height, given_height=given_height)

    elif given_height <= 4:
        blocks = get_z_blocks(zBlocksPrefab.GRASS_MEADOW_BLOCK)
        cells += blocks.get_z_blocks(x=x, y=y, z_start=0, given_height=given_height)

        entities = get_z_blocks(zBlocksPrefab.GRASS_MEADOW_ENTITY)
        cells += entities.get_z_blocks(x=x, y=y, z_start=given_height, given_height=given_height)

    elif given_height <= 6:
        blocks = get_z_blocks(zBlocksPrefab.FOREST_BLOCK)
        cells += blocks.get_z_blocks(x=x, y=y, z_start=0, given_height=given_height)

        entities = get_z_blocks(zBlocksPrefab.FOREST_ENTITY)
        cells += entities.get_z_blocks(x=x, y=y, z_start=given_height, given_height=given_height)

    return cells


def generation_map(
    seed: str = datetime.datetime.today().strftime("%Y_%m_%d-%H_%M_%S"),
    sea_level_height=2,
    max_height=7,
    map_size=32,
    viewport_size=15,
):
    random.seed(seed)

    map_json = {
        "objects": [
            create_camera(viewport_size),
            create_keyboard_subject(),
            create_player(),
        ],
        "camera_id": 0,
        "keyboard_subject_id": 1,
    }

    perlin_array: list[list[float]] = get_perlin_noise_list(size=map_size, octaves=1, res=20)
    for y in range(len(perlin_array)):
        for x in range(len(perlin_array[y])):
            given_height = int((perlin_array[y][x] * 100) / (101 / max_height))
            z_blocs = get_all_the_z_blocks(
                given_height=given_height,
                sea_level_height=sea_level_height,
                max_height=max_height,
                x=x,
                y=y,
            )
            map_json["objects"] += z_blocs

    return json.dumps(map_json)


def create_player() -> dict:
    return {
        "components": [
            {
                "type": "TransformComponent",
                "position": {"x": 0, "y": 0, "z": 4},
            },
            {
                "type": "RendererComponent",
                "shader": {
                    "type": "CompromiseShader",
                    "background_color": {"r": 0, "g": 0, "b": 0, "a": 0},
                    "object_color": {"r": 1, "g": 1, "b": 0, "a": 1.0},
                    "object_texture": "🧚",
                },
                "priority": 1000,
            },
            {"type": "PlayerController", "fields": {}},
        ]
    }


def create_keyboard_subject() -> dict:
    return {
        "components": [
            {
                "type": "TransformComponent",
                "position": {"x": 0, "y": 0, "z": 0},
            },
            {"type": "KeyboardSubjectComponent"},
        ]
    }


def create_camera(viewport_size) -> dict:
    return {
        "components": [
            {
                "type": "TransformComponent",
                "position": {
                    "x": int(-viewport_size / 4),
                    "y": int(-viewport_size / 4),
                    "z": 0,
                },
            },
            {
                "type": "CameraComponent",
                "viewport": {"x": viewport_size, "y": viewport_size, "z": 8},
                "center": {"x": viewport_size / 2, "y": viewport_size / 2, "z": 1},
                "default_rendered_shader": {
                    "type": "SimpleShader",
                    "background_color": {
                        "r": 0.0,
                        "g": 0.0,
                        "b": 0.0,
                        "a": 1,
                    },
                    "object_color": {"r": 0.0, "g": 0.0, "b": 0.0, "a": 1.0},
                    "object_texture": " ",
                },
            },
            {"type": "PlayerController", "fields": {}},
        ]
    }


if __name__ == "__main__":
    generation_map()
