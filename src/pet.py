from ursina import *
from ursina.color import color

class VirtualPet(Entity):
    def __init__(self):
        super().__init__(
            model='sphere',
            color=color.orange,
            scale=(1,1,1),
            position=(0,0,0)
        )
