from ursina import *
from pet import VirtualPet

# Create an instance of VirtualPet

def movement(pet, held_keys):
    if held_keys['w']:
        pet.y += 0.05
    if held_keys['s']:
        pet.y -= 0.05
    if held_keys['a']:
        pet.x -= 0.05
    if held_keys['d']:
        pet.x += 0.05