import pygame

#管理飞船的类
class Ship:
  def __init__(self,ai_game):
    #初始化飞船 获取窗口信息
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()
    #加载飞船的图像并获取外接矩形
    self.image = pygame.image.load("simple/alien/images/ship.bmp")
    self.rect = self.image.get_rect()

    #对于每艘新飞船，都将其放在屏幕的中央
    self.rect.midbottom = self.screen_rect.midbottom

    self.moving_right=False
    self.moving_left=False
    self.moving_up=False
    self.moving_down=False
    self.settings=ai_game.settings

  #窗口变化修改图形的位置
  def update_screen(self,ai_game):
    #相对位置的变更
    self.rect.x=self.rect.x/self.screen_rect.width*ai_game.screen.get_rect().width
    self.rect.y=self.rect.y/self.screen_rect.height*ai_game.screen.get_rect().height
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()

    if(self.rect.x>self.screen_rect.width-self.rect.width):
      self.rect.x=self.screen_rect.width-self.rect.width
    if(self.rect.y>self.screen_rect.height-self.rect.height):
      self.rect.y=self.screen_rect.height-self.rect.height

  def update(self):
    self._update_move()

  def _update_move(self):
    # 保存原始位置
    original_x = self.rect.x
    original_y = self.rect.y
    if self.moving_right:
      self.rect.x+=self.settings.ship_speed
    if self.moving_left:
      self.rect.x-=self.settings.ship_speed
    if self.moving_down:
      self.rect.y+=self.settings.ship_speed
    if self.moving_up:
      self.rect.y-=self.settings.ship_speed   
    if not self.is_inside_screen():
      self.rect.x=original_x
      self.rect.y=original_y

  def is_inside_screen(self):
    # 检查新位置是否在屏幕范围内
    screen_width=self.screen_rect.width-self.rect.width
    screen_height=self.screen_rect.height-self.rect.height
    return 0 <= self.rect.x <= screen_width and 0 <= self.rect.y <= screen_height

  def blitme(self):
    self.screen.blit(self.image,self.rect)  