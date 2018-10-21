import pygame

class Ship():
	"""docstring for Ship"""
	def __init__(self, screen, ai_settings):
		self.screen = screen
		self.ai_settings = ai_settings

		self.image = pygame.image.load('images/player.png')#加载图片

		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()#获取矩形
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.center_x = float(self.rect.centerx)
		self.center_y = float(self.rect.centery)

		self.moving = [False, False, False, False]#移动标志

	def update_ship(self):

		if self.moving[0] == True and self.rect.top > 0:
			self.center_y -= self.ai_settings.ship_speed_factor
		if self.moving[1] == True and self.rect.left > 0:
			self.center_x -= self.ai_settings.ship_speed_factor
		if self.moving[2] == True and self.rect.bottom < self.screen_rect.bottom:
			self.center_y += self.ai_settings.ship_speed_factor
		if self.moving[3] == True and self.rect.right < self.screen_rect.right:
			self.center_x += self.ai_settings.ship_speed_factor
		
		self.rect.centerx = self.center_x
		self.rect.centery = self.center_y

	def blitme(self):
		"""指定位置画飞船"""
		self.screen.blit(self.image, self.rect)

