from ursina import *
import os
from pathlib import Path
from pet import VirtualPet
from control import  movement

application.asset_folder = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), '../assets')))
print(application.asset_folder)

app = Ursina()
#image_entity = Entity(model='quad',texture=('IMG_5426.png'),  position=(0.5, -0.5))
pet = VirtualPet()

print(os.path)

def update():
    movement(pet, held_keys)
#     pass   
app.run()
