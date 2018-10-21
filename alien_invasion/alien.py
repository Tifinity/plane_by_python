import pygame
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
	"""docstring for Alien"""
	def __init__(self, ai_settings, screen):
		"""初始化并设定位置"""
		super(Alien, self).__init__()
		
		self.screen = screen
		self.ai_settings = ai_settings
		#加载外星人图像
		self.image = pygame.image.load('images/monster.png')
        #获取矩形
		self.rect = self.image.get_rect()
		#设置初始位置
		self.rect.centerx = randint(0,1200)
		self.rect.centery = -10
		self.center_y = float(self.rect.centery)
		#生命值
		#self.life = 3

	def update(self):
		"""移动"""
		self.center_y += self.ai_settings.alien_speed_factor
		self.rect.centery = self.center_y

	def blitme(self):
		"""指定位置画"""
		self.screen.blit(self.image, self.rect)