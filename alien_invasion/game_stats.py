class Gamestats(object):
	"""docstring for Gamestats"""
	def __init__(self, ai_settings):
		"""初始化"""
		self.ai_settings = ai_settings
		#self.reset_stats()
		self.game_active = True

	#def reset_stats():
	#	"""初始化"""
	#	self.ships_left = self.ai_settings.ship_limit
		