import sys
import pygame
from bullet import Bullet
from alien import Alien
from random import randint
from time import sleep


def check_events(ai_settings, screen, stats, play_button, ship, bullets):
	"""响应鼠标和键盘"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		#飞船移动方向
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(stats, play_button, mouse_x, mouse_y)

def check_play_button(stats, play_button, mouse_x, mouse_y):
	"""单击时开始"""
	if play_button.rect.collidepoint(mouse_x, mouse_y):
		stats.game_active = True

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""响应按下"""
	if event.key == pygame.K_UP:
		ship.moving[0] = True
	if event.key == pygame.K_LEFT:
		ship.moving[1] = True
	if event.key == pygame.K_DOWN:
		ship.moving[2] = True
	if event.key == pygame.K_RIGHT:
		ship.moving[3] = True

	if event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
	new_bullet = Bullet(ai_settings, screen, ship)
	bullets.add(new_bullet)

def check_keyup_events(event, ship):
	"""响应松开"""
	if event.key == pygame.K_UP:
		ship.moving[0] = False
	if event.key == pygame.K_LEFT:
		ship.moving[1] = False
	if event.key == pygame.K_DOWN:
		ship.moving[2] = False
	if event.key == pygame.K_RIGHT:
		ship.moving[3] = False

def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
	"""更新屏幕"""
	#重绘
	screen.fill(ai_settings.background_color)
	for bullet in bullets.sprites():
		bullet.blitme()	
	ship.blitme()
	aliens.draw(screen)
	if not stats.game_active:
		play_button.draw_button()

	#可见
	pygame.display.flip()
	
def update_bullets(ai_settings, screen, aliens, bullets):
	"""更新子弹"""
	#更新位置
	bullets.update()
	#删除子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	#碰撞检测
	check_collisions(ai_settings, screen, aliens, bullets)

def check_collisions(ai_settings, screen, aliens, bullets):
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

def create_fleet(ai_settings, screen, aliens):
	"""创建外星人群"""
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))

	for alien_number in range(number_aliens_x):
		alien = Alien(ai_settings, screen)
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		aliens.add(alien)

def update_aliens(ai_settings, stats, screen, ship, aliens):
	#更新位置
	aliens.update()
	#删除屏幕外
	for alien in aliens.copy():
		if alien.rect.bottom > (ai_settings.screen_height + 50):
			aliens.remove(alien)
	#创建新群
	if len(aliens) == 0:
		create_fleet(ai_settings, screen, aliens)
	#飞船与敌人
	if pygame.sprite.spritecollideany(ship, aliens):
		stats.game_active = False



