from ..sprite.simple_sprite import SimpleSprite
from ..sprite.sprite import Sprite


def load_sprite(sprite: dict) -> Sprite:
    match sprite["type"]:
        case "SimpleSprite":
            return _load_simple_sprite(sprite)


def _load_simple_sprite(sprite) -> SimpleSprite:
    return SimpleSprite(
        assets_folder=sprite["assets_folder"],
        assets_file=sprite["assets_file"],
        assets_image=sprite["assets_image"],
    )
