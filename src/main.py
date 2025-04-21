from ursina import *
from pet import VirtualPet

app = Ursina()

# 創建寵物
pet = VirtualPet()

EditorCamera()
app.run()
