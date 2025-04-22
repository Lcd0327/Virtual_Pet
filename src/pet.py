from ursina import *
import os

class VirtualPet(Entity):
    def __init__(self):
        print(f"load model from: {os.path}")
        super().__init__(
            model='cube',
            texture=(f'{application.asset_folder}/IMG_5426.png'), 
            position=(0.5, -0.5),
        )
