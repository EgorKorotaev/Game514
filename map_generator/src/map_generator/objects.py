import random
from dataclasses import dataclass, field

from nagoya.primitive import ColorA


def generate_from_distribution(object_distribution: list[(any, int)]) -> any:
    weight_all = sum(weight for _, weight in object_distribution)
    random_value = random.random() * weight_all
    i = 0
    for obj, weight in object_distribution:
        i += weight
        if i >= random_value:
            return obj


@dataclass
class Cell:
    object_textures: list[(str, int)] = field(default_factory=list)
    background_colors: list[(ColorA, int)] = field(default_factory=list)
    object_colors: list[(ColorA, int)] = field(default_factory=list)

    def get_prepared_str(self, background_color_a: int = 1, object_color_a: int = 1) -> dict:
        background_color = generate_from_distribution(self.background_colors)
        object_color = generate_from_distribution(self.object_colors)
        object_textures = generate_from_distribution(self.object_textures)
        return {
            # "type": "CompromiseShader",
            "type": "SimpleShader2",
            "background_color": {
                "r": background_color.r,
                "g": background_color.g,
                "b": background_color.b,
                "a": background_color.a,
            },
            "object_color": {
                "r": object_color.r,
                "g": object_color.g,
                "b": object_color.b,
                "a": object_color.a,
            },
            "object_texture": object_textures,
        }


def cell_prepared_str(x: int, y: int, z: int, shader: dict, priority: int) -> dict:
    return {
        "components": [
            {"type": "TransformComponent", "position": {"x": x, "y": y, "z": z}},
            {"type": "RendererComponent", "shader": shader, "priority": priority},
        ]
    }


@dataclass
class BuilderAllTheZBlocks:
    first_block: Cell
    main_block: Cell
    last_block: Cell

    def get_z_blocks(self, x: int, y: int, z_start: int, given_height: int, priority: int = 10) -> list[dict]:
        prepared_cells: list[dict] = [cell_prepared_str(x, y, z_start, self.first_block.get_prepared_str(), priority)]

        if given_height - 1 >= z_start + 1:
            for height in range(z_start + 1, given_height):
                prepared_cells.append(cell_prepared_str(x, y, height, self.main_block.get_prepared_str(), priority))

        if given_height >= z_start + 1:
            prepared_cells.append(cell_prepared_str(x, y, given_height, self.last_block.get_prepared_str(), priority))

        return prepared_cells
