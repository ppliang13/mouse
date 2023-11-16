class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置。"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 3
        self.ship_limit = 3
        self.ship_blood = 10

        # bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 2
        self.bullet_height = 15
        self.bullet_hurt = 1
        self.bullet_color = (60, 60, 60)

        # alien settings
        self.alien_speed = 0.7
        self.alien_max_hurt = 10
        self.alien_max_blood = 10
        self.alien_max_refresh_num = 10
        # 10s
        self.alien_refresh_time = 15
