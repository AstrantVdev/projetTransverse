import pygame

class World():
	def __init__(self, level):
		self.taille = pygame.display.set_mode((700, 700))
		self.list = []
		dirt_img = pygame.image.load('img/dirt.png')
		grass_img = pygame.image.load('img/grass.png')
		ligne_count = 0
		for ligne in level:
			colonne_count = 0
			for nb in ligne:
				if nb == 1:
					terre = pygame.transform.scale(dirt_img, (50, 50))
					img_rect = terre.get_rect()
					img_rect.x = colonne_count * 50
					img_rect.y = ligne_count * 50
					self.list.append((terre, img_rect))
				if nb == 2:
					sol = pygame.transform.scale(grass_img, (50, 50))
					img_rect = sol.get_rect()
					img_rect.x = colonne_count * 50
					img_rect.y = ligne_count * 50
					self.list.append((sol, img_rect))
				colonne_count += 1
			ligne_count += 1
	def draw(self):
		for tile in self.list:
			self.taille.blit(tile[0], tile[1])