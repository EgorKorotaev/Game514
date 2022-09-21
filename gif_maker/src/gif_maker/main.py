import os
import shutil

from PIL import Image

from gif_maker.game.run_game import run_game
from gif_maker.resources import temp_root, load_sprites


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


def safe_sprites_in_temp(_sprites: dict):
    clear_folder(temp_root())

    for assets_folder in _sprites:
        for assets_file in _sprites[assets_folder]:
            for im_name in _sprites[assets_folder][assets_file]:
                pil_img = Image.fromarray(_sprites[assets_folder][assets_file][im_name])
                # TODO Сделать адаптивное расширение
                pil_img.save(f"{temp_root()}{os.sep}{assets_folder}-{assets_file}-{im_name}.png")


def main():
    run_game()


if __name__ == "__main__":
    sprites = load_sprites()
    safe_sprites_in_temp(sprites)
    # main()
