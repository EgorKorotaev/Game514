#!/usr/bin/env python

from distutils.core import setup

setup(
    name="Auvers Game",
    version="0.0.0",
    description="Auvers-sur-Oise",
    author="",
    packages=["auvers_game"],
    package_dir={"": "src"},
    entry_points={"console_scripts": ["auvers_game=auvers_game.main:main"]},
)
