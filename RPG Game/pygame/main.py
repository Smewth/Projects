import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
screen_width = 800
screen_height = 600

# Create the display window
screen = pygame.display.set_mode((screen_width, screen_height))

# Main game loop
running = True
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a solid color
    screen.fill((0, 0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()