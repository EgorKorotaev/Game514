from dataclasses import dataclass

from ascii_game.component.component import Component


@dataclass
class RendererPriority(Component):
    priority: int = 0
