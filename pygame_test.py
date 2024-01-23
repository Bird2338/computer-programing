# File Imports
import pygame

# pygame window
background_colour = (0, 0, 0) 
screen = pygame.display.set_mode((300, 300)) 
pygame.display.set_caption("Oliver's magnificent RPG") 
running = True
while running:  
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False