from ursina import *
import os

class VirtualPet(Entity):
    def __init__(self):
        super().__init__(
            model='cube',
            color=color.white,
            scale=(1, 1, 1),
            position=(0,0,0)
        )
