from ..sprite.simple_sprite import SimpleSprite
from ..sprite.sprite import Sprite
from ..sprite.sprite_visitor import SpriteVisitor


def serialize_sprite(sprite: Sprite) -> dict:
    json_sprite_visitor = JSONExportSpriteVisitor()
    sprite.accept(json_sprite_visitor)
    return json_sprite_visitor.serialized_sprite


class JSONExportSpriteVisitor(SpriteVisitor):
    def __init__(self):
        self.serialized_sprite: dict = {}

    def visit_simple(self, element: SimpleSprite) -> None:
        self.serialized_sprite = {
            "type": "SimpleSprite",
            "assets_folder": element.assets_folder,
            "assets_file": element.assets_file,
            "assets_image": element.assets_image,
        }
