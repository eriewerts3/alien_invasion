import sys

import pygame #This is saying we want to use the pip module pygame package 

from settings import Settings #Imported Settings class from settings.py
from ship import Ship #Imported the class Ship from ship.py

class AlienInvasion:
	"""Overall class to mannage game assets and behavior."""


	def __init__(self):
		"""Initialize the game, and create game resources."""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height)) #self.screen is the back surface
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)

		#Set the backround color
		self.bg_color = (0,180,204) #Color Azure Blue for sea backround

	def run_game(self): # Controle center for game
		"""Start the main loop for the game."""
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			# Redraw the screen druring each pass through the loop.
			self.screen.fill(self.settings.bg_color)
			self.ship.blitme()

			# Make the most recently drawn screen visible.
			pygame.display.flip()
			
if __name__ == '__main__':
	#Make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()