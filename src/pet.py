import pygame
import os
from pathlib import Path

class VirtualPet:
    def __init__(self, asset_folder, window_width=1152, window_height=720, texture_file='IMG_5426.png'):
        self.asset_folder = Path(asset_folder)
        self.texture_path = self.asset_folder / texture_file

        # 嘗試載入寵物圖片
        if self.texture_path.exists():
            self.image = pygame.image.load(str(self.texture_path))
            self.image = pygame.transform.scale(self.image, (200, 200))  # 調整圖片大小
            print(f"Loaded texture from: {self.texture_path}")
        else:
            self.image = None
            print(f"Warning: Texture file {self.texture_path} not found.")

        # 設定初始位置
        self.position = [window_width // 2 - 100, window_height // 2 - 100]

    def draw(self, screen):
        """繪製寵物圖片到螢幕上"""
        if self.image:
            screen.blit(self.image, self.position)

    def move(self, dx, dy):
        """移動寵物位置"""
        self.position[0] += dx
        self.position[1] += dy