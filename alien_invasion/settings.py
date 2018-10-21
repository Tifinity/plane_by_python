class Settings():
	"""储存所有设置"""
	def __init__(self):
		"""初始化游戏的设置"""
		#屏幕
		self.screen_width = 1200
		self.screen_height = 800
		self.background_color = (200,200,200)
		#子弹
		self.bullet_speed_factor = 0.7
		#敌机
		self.alien_speed_factor = 0.5
		#飞船
		self.ship_limit = 3
		self.ship_speed_factor = 1