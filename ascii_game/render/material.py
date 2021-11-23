from abc import ABC, abstractmethod
from dataclasses import dataclass

from ascii_game.render.shader import Shader, DefaultShader, RenderedTile
from ascii_game.render.texture import BackgroundTexture, ObjectTexture


class Material(ABC):
    background_texture: BackgroundTexture
    object_texture: ObjectTexture
    shader: Shader

    @abstractmethod
    def render(self, underlying_tile, position_z):
        pass


@dataclass
class DefaultMaterial(Material):
    background_texture: BackgroundTexture = BackgroundTexture()
    object_texture: ObjectTexture = ObjectTexture()
    shader: Shader = DefaultShader()

    def render(self, underlying_tile: RenderedTile, position_z: int) -> RenderedTile:
        return self.shader.render(self.background_texture, self.object_texture, underlying_tile, position_z)
