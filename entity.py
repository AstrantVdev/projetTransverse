import pygame

class Entity(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.name = 'name'
		self.weight = 50
		self.life = -1
		self.fly = False
		self.x = 0
		self.y = 0
		self.pitch = 0
		self.texture
		self.type = "PROJECTILE"
		self.mod = 0

class Player(Entity):

	def __init__(self):
		self.name="Player"
		self.weight=150
		self.life=500556448879
		self.type="PLAYER"
		self.nickname=""
		self.inventory=[50]
		self.texture = pygame.image.load("graphics/logo32x32.jpg")
