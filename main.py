import numpy as np
import pygame
from pygame.locals import *
import sys

class game():
	def __init__(self):
		self.w = 1000
		self.h = 800
		pygame.init()
		screen = pygame.display.set_mode((self.w,self.h))
		pygame.display.set_caption('Fish')

    	# Fill background
		background = pygame.Surface(screen.get_size())
		background = background.convert()
		background.fill((0, 0, 55))

    	# Display some text
		font = pygame.font.Font(None, 36)
		text = font.render("Hello There", 1, (10, 10, 10))
		textpos = text.get_rect()
		textpos.centerx = background.get_rect().centerx
		background.blit(text, textpos)

		# Blit everything to the screen
		screen.blit(background, (0, 0))
		pygame.display.flip()

		# Event loop
		while 1:
			for event in pygame.event.get():
				if event.type == QUIT:
					return

			screen.blit(background, (0, 0))
			pygame.display.flip()




if __name__=="__main__":
	g = game()
