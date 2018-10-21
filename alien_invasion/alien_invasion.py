import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import Gamestats
import game_functions as gf
from button import Button

def run_game():
	#初始化
	pygame.init()
	#设置类
	ai_settings = Settings()
	#统计信息类
	stats = Gamestats(ai_settings)
	#创建窗口
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	#创建飞船，子弹，敌人
	play_button = Button(ai_settings, screen, "Play")
	ship = Ship(screen, ai_settings)
	bullets = Group()
	aliens = Group()

	#开始主循环
	while True:
		gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
		if stats.game_active == True:
			ship.update_ship()
			gf.update_aliens(ai_settings, stats, screen, ship, aliens)
			gf.update_bullets(ai_settings, screen, aliens, bullets)
			gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()