import os
import numpy as np
import shutil
from datetime import datetime

import keyboard as keyboard

from gif_maker.resources import temp_root, load_sprites
from map_generator.main import generation_map
from nagoya.component import KeyboardSubjectComponent
from nagoya.render.terminal_renderer import render_to_terminal
from nagoya.render.gif_renderer import render_scene
from nagoya.scene import Scene
from nagoya.serialization.load_scene import load_scene
from nagoya.serialization.serialize_scene import serialize_scene
from PIL import Image


def clear_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def run_game():
    scene = load_scene(generation_map(seed="2022_05_04-23_15_07", max_height=8, map_size=64, viewport_size=64))
    game_loop(scene)


def game_loop(scene: Scene) -> None:
    def print_pressed_keys(e):
        if e.event_type != "down":
            return
        e_ = e.name
        match e_:
            case "1":
                e_ = "7"
            case "2":
                e_ = "8"
            case "3":
                e_ = "9"
            case "9":
                e_ = "3"
            case "8":
                e_ = "2"
            case "7":
                e_ = "1"
            case "4":
                e_ = "4"
            case "6":
                e_ = "6"
            case "+":
                e_ = "+"
            case "-":
                e_ = "-"
        scene._objects[scene.keyboard_subject_id].get_component(KeyboardSubjectComponent).move(e_)
        buffer = render_scene(scene)
        pil_img = Image.fromarray(np.uint8(buffer.rendered_tiles))
        pil_img.save(f"{temp_root()}{os.sep}test.png")

    # clear_folder(temp_root())
    # while True:
    #     keyboard.hook(print_pressed_keys)
    #     keyboard.wait()

    buffer = render_scene(scene)
    pil_img = Image.fromarray(np.uint8(buffer.rendered_tiles))
    pil_img.save(f"{temp_root()}{os.sep}test.png")


def save_scene(scene):
    with open("data.json", "w") as f:
        f.write(serialize_scene(scene))
