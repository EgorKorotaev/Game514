from enum import Enum, auto

from nagoya.primitive import ColorA
from generator.objects import Cell, BuilderAllTheZBlocks


class CellPrefab(Enum):
    BEDROCK = auto()
    DEEP_WATER_BLOCK = auto()
    DEEP_WATER_ENTITY = auto()
    SHOAL_BLOCK = auto()
    SHOAL_ENTITY = auto()
    BEACH_BLOCK = auto()
    BEACH_ENTITY = auto()
    GRASS_MEADOW_BLOCK = auto()
    GRASS_MEADOW_ENTITY = auto()
    FOREST_BLOCK = auto()
    FOREST_ENTITY = auto()


def get_cell(cell_prefab: CellPrefab) -> Cell:
    match cell_prefab:
        case CellPrefab.BEDROCK:
            return Cell(
                background_colors=[(ColorA(0.5, 0.5, 0.5), 1)],
                object_colors=[(ColorA(a=0), 1)],
                object_textures=[("", 1)],
            )
        case CellPrefab.DEEP_WATER_BLOCK:
            return Cell(
                background_colors=[
                    (ColorA(0 / 255, 105 / 255, 148 / 255, 0.80), 1),
                    (ColorA(1 / 255, 84 / 255, 130 / 255, 0.80), 1),
                    (ColorA(4 / 255, 116 / 255, 149 / 255, 0.80), 1),
                ],
                object_colors=[(ColorA(a=0), 1)],
                object_textures=[("", 1)],
            )
        case CellPrefab.DEEP_WATER_ENTITY:
            return Cell(
                background_colors=[(ColorA(a=0), 1)],
                object_colors=[(ColorA(1, 1, 1), 1)],
                object_textures=[
                    ("", 24),
                    ("🌊", 1),
                    ("🐋", 1),
                    ("🦈", 1),
                    ("🐳", 1),
                    ("🐙", 1),
                    ("🐬", 1),
                ],
            )
        case CellPrefab.SHOAL_BLOCK:
            return Cell(
                background_colors=[
                    (ColorA(32 / 255, 178 / 255, 170 / 255, 0.60), 1),
                    (ColorA(60 / 255, 153 / 255, 146 / 255, 0.60), 1),
                    (ColorA(27 / 255, 163 / 255, 156 / 255, 0.60), 1),
                ],
                object_colors=[(ColorA(a=0), 1)],
                object_textures=[("", 1)],
            )
        case CellPrefab.SHOAL_ENTITY:
            return Cell(
                background_colors=[(ColorA(a=0), 1)],
                object_colors=[(ColorA(1, 1, 1), 1)],
                object_textures=[
                    ("", 24),
                    ("🦈", 1),
                    ("🐬", 1),
                    ("🐟", 1),
                    ("🐡", 1),
                    ("🐠", 1),
                ],
            )
        case CellPrefab.BEACH_BLOCK:
            return Cell(
                background_colors=[
                    (ColorA(r=226 / 255, g=202 / 255, b=118 / 255), 1),
                    (ColorA(r=241 / 255, g=218 / 255, b=122 / 255), 1),
                    (ColorA(r=201 / 255, g=174 / 255, b=116 / 255), 1),
                    (ColorA(r=240 / 255, g=219 / 255, b=125 / 255), 1),
                    (ColorA(r=245 / 255, g=231 / 255, b=162 / 255), 1),
                ],
                object_colors=[(ColorA(a=0), 1)],
                object_textures=[("", 1)],
            )
        case CellPrefab.BEACH_ENTITY:
            return Cell(
                background_colors=[(ColorA(a=0), 1)],
                object_colors=[(ColorA(1, 1, 1), 1)],
                object_textures=[
                    ("", 80),
                    ("🐚", 5),
                    ("🐢", 2),
                    ("🦎", 2),
                    ("🌴", 1),
                ],
            )
        case CellPrefab.GRASS_MEADOW_BLOCK:
            return Cell(
                background_colors=[
                    (ColorA(r=127 / 255, g=255 / 255, b=0 / 255), 1),
                    (ColorA(r=50 / 255, g=205 / 255, b=50 / 255), 1),
                    (ColorA(r=107 / 255, g=142 / 255, b=35 / 255), 1),
                    (ColorA(r=85 / 255, g=107 / 255, b=47 / 255), 1),
                    (ColorA(r=34 / 255, g=139 / 255, b=34 / 255), 1),
                ],
                object_colors=[(ColorA(a=0), 1)],
                object_textures=[("", 1)],
            )
        case CellPrefab.GRASS_MEADOW_ENTITY:
            return Cell(
                background_colors=[(ColorA(a=0), 1)],
                object_colors=[(ColorA(1, 1, 1), 1)],
                object_textures=[
                    ("", 80),
                    ("🐜", 2),
                    ("🌿", 2),
                    ("🪱", 2),
                    ("🐛", 2),
                ],
            )
        case CellPrefab.FOREST_BLOCK:
            return Cell(
                background_colors=[
                    (ColorA(r=128 / 255, g=128 / 255, b=0 / 255), 1),
                    (ColorA(r=0 / 255, g=255 / 255, b=0 / 255), 1),
                    (ColorA(r=34 / 255, g=139 / 255, b=34 / 255), 1),
                    (ColorA(r=173 / 255, g=255 / 255, b=47 / 255), 1),
                    (ColorA(r=139 / 255, g=69 / 255, b=19 / 255), 1),
                ],
                object_colors=[(ColorA(a=0), 1)],
                object_textures=[("", 1)],
            )
        case CellPrefab.FOREST_ENTITY:
            return Cell(
                background_colors=[(ColorA(a=0), 1)],
                object_colors=[(ColorA(1, 1, 1), 1)],
                object_textures=[
                    ("", 80),
                    ("🌾", 20),
                    ("🪨", 10),
                    ("🍀", 5),
                    ("🌈", 5),
                    ("🌱", 20),
                    ("🌳", 30),
                    ("🌲", 20),
                    ("🌧", 1),
                    ("⛈", 1),
                    ("🌪", 1),
                    ("🌩", 1),
                ],
            )


class zBlocksPrefab(Enum):
    BOTTOM_SEA_BLOCK = auto()
    DEEP_WATER_BLOCK = auto()
    SHOAL_BLOCK = auto()
    BEACH_BLOCK = auto()
    GRASS_MEADOW_BLOCK = auto()
    FOREST_BLOCK = auto()
    DEEP_WATER_ENTITY = auto()
    SHOAL_ENTITY = auto()
    BEACH_ENTITY = auto()
    GRASS_MEADOW_ENTITY = auto()
    FOREST_ENTITY = auto()


def get_z_blocks(builder_all_the_z_blocks: zBlocksPrefab) -> BuilderAllTheZBlocks:
    match builder_all_the_z_blocks:
        case zBlocksPrefab.BOTTOM_SEA_BLOCK:
            return BuilderAllTheZBlocks(
                first_block=get_cell(CellPrefab.BEDROCK),
                main_block=get_cell(CellPrefab.BEACH_BLOCK),
                last_block=get_cell(CellPrefab.BEACH_BLOCK),
            )
        case zBlocksPrefab.DEEP_WATER_BLOCK:
            return BuilderAllTheZBlocks(
                first_block=get_cell(CellPrefab.BEDROCK),
                main_block=get_cell(CellPrefab.DEEP_WATER_BLOCK),
                last_block=get_cell(CellPrefab.DEEP_WATER_BLOCK),
            )
        case zBlocksPrefab.DEEP_WATER_ENTITY:
            return BuilderAllTheZBlocks(
                first_block=get_cell(CellPrefab.DEEP_WATER_ENTITY),
                main_block=get_cell(CellPrefab.DEEP_WATER_ENTITY),
                last_block=get_cell(CellPrefab.DEEP_WATER_ENTITY),
            )
        case zBlocksPrefab.SHOAL_BLOCK:
            return BuilderAllTheZBlocks(
                first_block=get_cell(CellPrefab.BEDROCK),
                main_block=get_cell(CellPrefab.SHOAL_BLOCK),
                last_block=get_cell(CellPrefab.SHOAL_BLOCK),
            )
        case zBlocksPrefab.SHOAL_ENTITY:
            return BuilderAllTheZBlocks(
                first_block=get_cell(CellPrefab.SHOAL_ENTITY),
                main_block=get_cell(CellPrefab.SHOAL_ENTITY),
                last_block=get_cell(CellPrefab.SHOAL_ENTITY),
            )
        case zBlocksPrefab.BEACH_BLOCK:
            return BuilderAllTheZBlocks(
                first_block=get_cell(CellPrefab.BEDROCK),
                main_block=get_cell(CellPrefab.BEACH_BLOCK),
                last_block=get_cell(CellPrefab.BEACH_BLOCK),
            )
        case zBlocksPrefab.BEACH_ENTITY:
            return BuilderAllTheZBlocks(
                first_block=get_cell(CellPrefab.BEACH_ENTITY),
                main_block=get_cell(CellPrefab.BEACH_ENTITY),
                last_block=get_cell(CellPrefab.BEACH_ENTITY),
            )
        case zBlocksPrefab.GRASS_MEADOW_BLOCK:
            return BuilderAllTheZBlocks(
                first_block=get_cell(CellPrefab.BEDROCK),
                main_block=get_cell(CellPrefab.GRASS_MEADOW_BLOCK),
                last_block=get_cell(CellPrefab.GRASS_MEADOW_BLOCK),
            )
        case zBlocksPrefab.GRASS_MEADOW_ENTITY:
            return BuilderAllTheZBlocks(
                first_block=get_cell(CellPrefab.GRASS_MEADOW_ENTITY),
                main_block=get_cell(CellPrefab.GRASS_MEADOW_ENTITY),
                last_block=get_cell(CellPrefab.GRASS_MEADOW_ENTITY),
            )
        case zBlocksPrefab.FOREST_BLOCK:
            return BuilderAllTheZBlocks(
                first_block=get_cell(CellPrefab.BEDROCK),
                main_block=get_cell(CellPrefab.FOREST_BLOCK),
                last_block=get_cell(CellPrefab.FOREST_BLOCK),
            )
        case zBlocksPrefab.FOREST_ENTITY:
            return BuilderAllTheZBlocks(
                first_block=get_cell(CellPrefab.FOREST_ENTITY),
                main_block=get_cell(CellPrefab.FOREST_ENTITY),
                last_block=get_cell(CellPrefab.FOREST_ENTITY),
            )


#         case 'desert':
#             background_color_1 = ColorA()
#             background_color_1.set_rgb_255(236, 213, 64)
#
#             background_color_2 = ColorA()
#             background_color_2.set_rgb_255(241, 218, 122)
#
#             background_color_3 = ColorA()
#             background_color_3.set_rgb_255(252, 225, 102)
#
#             background_color_4 = ColorA()
#             background_color_4.set_rgb_255(253, 238, 115)
#
#             background_color_5 = ColorA()
#             background_color_5.set_rgb_255(241, 231, 136)
#
#             background_color = random.choice(
#                 [background_color_1, background_color_2, background_color_3, background_color_4, background_color_5])
#
#             object_color = ColorA()
#             object_color.set_rgb_255(255, 255, 255)
#             simple_shader = {
#                 "type": "SimpleShader",
#                 "background_color": {
#                     "r": background_color.r,
#                     "g": background_color.g,
#                     "b": background_color.b,
#                     "a": 0.25
#                 },
#                 "object_color": {
#                     "r": object_color.r,
#                     "g": object_color.g,
#                     "b": object_color.b,
#                     "a": 0
#                 },
#                 "object_texture": ""
#             }
#
#             texture_distribution = [
#                 ("", 80),
#                 ("🦂", 5),
#                 ("🌵", 20),
#                 ("☀", 1),
#                 ("🌞", 1),
#             ]
#             simple_shader["object_texture"] = generate_from_distribution(texture_distribution)
#
#             return simple_shader
#
#         case 'mountains':
#             background_color_1 = ColorA()
#             background_color_1.set_rgb_255(220, 220, 220)
#
#             background_color_2 = ColorA()
#             background_color_2.set_rgb_255(248, 248, 255)
#
#             background_color_3 = ColorA()
#             background_color_3.set_rgb_255(169, 169, 169)
#
#             background_color_4 = ColorA()
#             background_color_4.set_rgb_255(105, 105, 105)
#
#             background_color_5 = ColorA()
#             background_color_5.set_rgb_255(255, 255, 255)
#
#             background_color = random.choice(
#                 [background_color_1, background_color_2, background_color_3, background_color_4, background_color_5])
#
#             object_color = ColorA()
#             object_color.set_rgb_255(255, 255, 255)
#             simple_shader = {
#                 "type": "SimpleShader",
#                 "background_color": {
#                     "r": background_color.r,
#                     "g": background_color.g,
#                     "b": background_color.b,
#                     "a": 0.25
#                 },
#                 "object_color": {
#                     "r": object_color.r,
#                     "g": object_color.g,
#                     "b": object_color.b,
#                     "a": 0
#                 },
#                 "object_texture": ""
#             }
#
#             texture_distribution = [
#                 ("", 8000),
#                 ("🪴", 1),
#                 ("☃", 200),
#                 ("🌬", 100),
#                 ("❄", 1000),
#                 ("🌑", 10),
#                 ("🌚", 1),
#                 ("🌒", 10),
#                 ("🌛", 1),
#                 ("⯝", 10),
#                 ("🌓", 10),
#                 ("🌔", 10),
#                 ("🌕", 10),
#                 ("🌝", 1),
#                 ("🌖", 10),
#                 ("🌗", 10),
#                 ("🌘", 10),
#                 ("🌜", 1),
#                 ("⚸", 1),
#             ]
#             simple_shader["object_texture"] = generate_from_distribution(texture_distribution)
#
#             return simple_shader
