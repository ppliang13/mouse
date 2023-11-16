import sys
import pygame
from setting import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import Game_stats
from button import Button
import time
import random


class AlienInvasion:
    """管理游戏资源和行为类"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.stats = Game_stats(self)
        # 设置窗口大小
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height),
                                              pygame.RESIZABLE)

        # 全屏
        # self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_height=self.screen.get_rect().height
        # self.settings.screen_width=self.screen.get_rect().width

        # 说明
        pygame.display.set_caption("Alien Invasion")
        # 设置背景颜色
        self.bg_color = self.settings.bg_color
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.play_button = Button(self, "Play")

    def run_game(self):
        timestamp = int(time.time())
        print(timestamp)
        while True:
            # 检查事件修改参数
            self._check_events()
            # 飞船移动
            self.ship.update()
            # 子弹移动
            self.bullets.update()
            # 外星人移动
            self.aliens.update()
            # 外星人增加
            if timestamp == int(time.time()):
                self._create_fleet()
                timestamp += self.settings.alien_refresh_time
                # 重新绘制
            pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
            self._update_screen()

    # 创建外星人群
    def _create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        refresh_num = self.settings.alien_max_refresh_num
        number_aliens_x = random.randint(int(0.2 * refresh_num), refresh_num)
        for alien_number in range(number_aliens_x):
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)

    '''step1：检查事件'''

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self.ship.update_screen(self)
            elif event.type == pygame.KEYDOWN:
                self._event_key_down(event)
            elif event.type == pygame.KEYUP:
                self._event_key_up(event)

    def _event_key_down(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _event_key_up(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
        self._remove_bullets()

    def _remove_bullets(self):
        if len(self.bullets) > 50 and len(self.bullets) % 50 == 0:
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

    def _update_screen(self):

        # 每次循环重新绘制屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        if not self.stats.game_active:
            self.play_button.draw_button()
            # 让最近绘制屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
