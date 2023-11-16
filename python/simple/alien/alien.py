import pygame
import random
import math
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类。"""
    def __init__(self, ai_game):
        """初始化外星人并设置其起始位置。"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近。
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置。
        self.x = float(self.rect.x)

        self.move_speed = ai_game.settings.alien_speed
        # 随机运动参数
        self.angle = random.uniform(0, 2 * math.pi)

    def update(self):
        self.random_move()

    def draw_alien(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def random_move(self):
        # 随机改变角度
        angle_change = random.uniform(-0.2, 0.2)
        self.angle += angle_change

        # 根据新角度移动
        random_x = math.cos(self.angle)
        random_y = math.sin(self.angle)
        if random_x > 0:
            self.rect.x += self.move_speed
        else:
            self.rect.x -= self.move_speed
        if random_y > 0:
            self.rect.y += self.move_speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > self.screen_rect.width - self.rect.width:
            self.rect.x = self.screen_rect.width - self.rect.width
