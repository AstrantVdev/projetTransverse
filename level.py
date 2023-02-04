import pygame

class World():
	def __init__(self, data):
		self.tile_list = []
		self.screen = pygame.display.set_mode((700, 700))
		#load images
		dirt_img = pygame.image.load('img/dirt.png')
		grass_img = pygame.image.load('img/grass.png')
		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(dirt_img, (50, 50))
					img_rect = img.get_rect()
					img_rect.x = col_count * 50
					img_rect.y = row_count * 50
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					img = pygame.transform.scale(grass_img, (50, 50))
					img_rect = img.get_rect()
					img_rect.x = col_count * 50
					img_rect.y = row_count * 50
					tile = (img, img_rect)
					self.tile_list.append(tile)
				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			self.screen.blit(tile[0], tile[1])