from dataclasses import dataclass


@dataclass
class BackgroundTexture:
    color_id: str = "default"


@dataclass
class ObjectTexture:
    object_id: str = "default"
