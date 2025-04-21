from ursina import *
from pet import VirtualPet
from control import  movement

app = Ursina()

pet = VirtualPet()

def update():
    movement(pet, held_keys)
    
app.run()
