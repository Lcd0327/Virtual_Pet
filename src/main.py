import pygame
import os
from pathlib import Path
from pet import VirtualPet

# 初始化 Pygame
pygame.init()

# 設定視窗大小與標題
WINDOW_WIDTH, WINDOW_HEIGHT = 1152, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Virtual Pet")

# 設定資產資料夾
ASSET_FOLDER = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), '../assets')))
print(f"Asset folder: {ASSET_FOLDER}")

# 初始化虛擬寵物
pet = VirtualPet(ASSET_FOLDER, WINDOW_WIDTH, WINDOW_HEIGHT)

# 初始化主迴圈控制與時鐘
running = True
clock = pygame.time.Clock()

# 主迴圈
while running:
    # 處理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 取得按鍵輸入
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pet.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        pet.move(5, 0)
    if keys[pygame.K_UP]:
        pet.move(0, -5)
    if keys[pygame.K_DOWN]:
        pet.move(0, 5)

    # 繪製畫面
    screen.fill((135, 206, 250))  # 背景顏色 (淺藍色)
    pet.draw(screen)

    # 更新畫面
    pygame.display.flip()

    # 控制幀率
    clock.tick(60)

# 結束 Pygame
pygame.quit()
