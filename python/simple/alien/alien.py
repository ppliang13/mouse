import pygame
import random
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类。"""

    def __init__(self, ai_game):
        """初始化外星人并设置其起始位置。"""
        super().__init__()
        self.screen = ai_game.screen

        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近。
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置。
        self.x = float(self.rect.x)
        self.move_speed = ai_game.settings.alien_speed

    def update(self):
        self.random_move()

    def draw_alien(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def random_move(self):
        result = random.randrange(3)
        if result == 0:
            self.rect.y += self.move_speed
        elif result == 1:
            self.rect.x -= self.move_speed
        elif result == 2:
            self.rect.x += self.move_speed
