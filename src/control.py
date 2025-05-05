import pygame

def movement(pet, keys):
    """根據按鍵輸入移動寵物"""
    if keys[pygame.K_w]:
        pet.move(0, -5)  # 向上移動
    if keys[pygame.K_s]:
        pet.move(0, 5)   # 向下移動
    if keys[pygame.K_a]:
        pet.move(-5, 0)  # 向左移動
    if keys[pygame.K_d]:
        pet.move(5, 0)   # 向右移動