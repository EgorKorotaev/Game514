from abc import ABC, abstractmethod
from dataclasses import dataclass

from ascii_game.render.texture import BackgroundTexture, ObjectTexture


@dataclass
class RenderedTile:
    background_texture: BackgroundTexture
    object_texture: ObjectTexture


class Shader(ABC):
    @abstractmethod
    def render(self, underlying_tile: RenderedTile | None, position_z: int) -> RenderedTile:
        pass


@dataclass
class DefaultShader(Shader):
    background_texture: BackgroundTexture = BackgroundTexture()
    object_texture: ObjectTexture = ObjectTexture()

    def render(self, underlying_tile: RenderedTile, position_z: int) -> RenderedTile:
        return RenderedTile(self.background_texture, self.object_texture)
