
class World():
	def __init__(self, level):
		self.tile_list = []
		dirt_img = pygame.image.load('img/dirt.png')
		grass_img = pygame.image.load('img/grass.png')
		ligne = 0
		for ligne in data:
			colonne = 0
			for tile in ligne:
                if tile == 1:
					img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = colonne * tile_size
					img_rect.y = ligne * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					img = pygame.transform.scale(grass_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = colonne * tile_size
					img_rect.y = ligne * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 3:
					blob = Enemy(colonne * tile_size, ligne * tile_size + 15)
					blob_group.add(blob)
				if tile == 4:
					platform = Platform(colonne * tile_size, ligne * tile_size, 1, 0)
					platform_group.add(platform)
				if tile == 5:
					platform = Platform(colonne * tile_size, ligne * tile_size, 0, 1)
					platform_group.add(platform)
				if tile == 6:
					lava = Lava(colonne * tile_size, ligne * tile_size + (tile_size // 2))
					lava_group.add(lava)
				if tile == 7:
					coin = Coin(colonne * tile_size + (tile_size // 2), ligne * tile_size + (tile_size // 2))
					coin_group.add(coin)
				if tile == 8:
					exit = Exit(colonne * tile_size, ligne * tile_size - (tile_size // 2))
					exit_group.add(exit)
				colonne += 1
		 ligne += 1

	def draw(self):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])