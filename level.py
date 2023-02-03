import pygame
class World():
	def __init__(self, level):
		self.tile_list = []
		dirt_img = pygame.image.load('img/dirt.png')
		grass_img = pygame.image.load('img/grass.png')
		ligne = 0
		for ligne in level:
			colonne = 0
			for tile in ligne:
                if tile == 1:
					img = pygame.transform.scale(dirt_img, (50, 50))
					img_rect = img.get_rect()
					img_rect.x = colonne * 50
					img_rect.y = ligne * 50
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					img = pygame.transform.scale(grass_img, (50, 50))
					img_rect = img.get_rect()
					img_rect.x = colonne * 50
					img_rect.y = ligne * 50
					tile = (img, img_rect)
					self.tile_list.append(tile)
				colonne += 1
		 ligne += 1

	def draw(self):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])