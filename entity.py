import pygame

class Entity:

	def __init__(self):
		self.name = 'name'
		self.speed = [0,0,0]
		self.life = -1
		self.fly = False
		self.mod = 0
		self.x = 0
		self.y = 0
		self.pitch = 0
		self.texture
		self.type = "LETTER"

class Player(Entity):

	def __init__(self):
		self.name = 'player'
		self.life = 5
		self.mod = 0
		self.x = 200
		self.y = 200
		self.pitch = 0
		self.texture = pygame.image.load("logo32x32.jpg")
		self.type = "PLAYER"