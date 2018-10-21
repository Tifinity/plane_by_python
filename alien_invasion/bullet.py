import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""docstring for Bullet"""
	def __init__(self, ai_settings, screen, ship):
		super(Bullet, self).__init__()

		self.screen = screen
		self.ai_settings = ai_settings
		#加载图片
		self.image = pygame.image.load('images/player_bullet.png')
		#获取矩形
		self.rect = self.image.get_rect()
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		self.y = float(self.rect.y)
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		"""移动子弹"""
		self.y -= self.speed_factor
		self.rect.centery = self.y

	def blitme(self):
		"""画子弹"""
		self.screen.blit(self.image, self.rect)