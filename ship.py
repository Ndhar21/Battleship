from random import randint

class Ship:

	def setup_location(self):
		x = randint(0, self.config.row-1) # row = 5 , 0,1,2,3,4
		y = randint(0, self.config.column-1)
		self.location = (x,y)

	def __init__(self, Game):
		self.config = Game.config