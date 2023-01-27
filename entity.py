import pygame

class Entity(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.name = 'name'
		self.speed = [0,0,0]
		self.weight
		self.life = -1
		self.fly = False
		self.x = 0
		self.y = 0
		self.pitch = 0
		self.texture
		self.type = "PROJECTILE"

class Player(Entity):

	def __init__(self):
		self.name = 'owo'
		self.life = 5
		self.mod = 0
		self.x = 184
		self.y = 184
		self.pitch = 0
		self.texture = pygame.image.load("graphics/logo32x32.jpg")
		self.type = "PLAYER"