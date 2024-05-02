# Pygame template - skeleton for a new pygame projects
import pygame
import random

WIDTH = 360  # width of our game window
HEIGHT = 480  # height of our game window
FPS = 30  # frame per second

# Define Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Game Loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)

    # Process input
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    
    # Render (draw)
    screen.fill(BLACK)
    
    # *after* drawing everything, flip display
    pygame.display.flip()