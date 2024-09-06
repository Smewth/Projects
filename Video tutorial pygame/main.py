import sys, pygame
pygame.init()

# Defining a clock to control the frame rate
clock = pygame.time.Clock()

# Defining the window size (Goes with the image size)
size = width, height = 640, 384
screen = pygame.display.set_mode(size)

# Defining the player
# Image
player_image = pygame.image.load(r"Video Tutorial pygame\player.png")
original_width, original_height = player_image.get_size()
new_height = 50  # Or whatever value you want
new_width = int(original_width * new_height / original_height)
player_image = pygame.transform.scale(player_image, (new_width, new_height))
# Player itself and position
player = player_image.get_rect()
player.center = (width//2, height - 50)
# Game variables related to the player
speed = 5
vertical_speed = -10
gravity = 1
jump_speed = 15

# Defining the background image
background = pygame.image.load(r"Video Tutorial pygame\background.jpg")
background = pygame.transform.scale(background, size)

# Main game loop
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player.bottom == height - 45:
                vertical_speed = -jump_speed
        
    # Process the even queue (To make sure following code works)
    pygame.event.pump()
       
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= speed
    if keys[pygame.K_RIGHT] and player.right < width:
        player.x += speed 
                
    # Apply gravity
    vertical_speed += gravity
    player.y += vertical_speed
    
    # Check if the player is on the ground
    if player.bottom > height - 45:
        player.bottom = height - 45
        vertical_speed = 0

    screen.blit(background, (0, 0))
    
    screen.blit(player_image, player)
    
    pygame.display.flip()