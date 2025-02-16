import sys, pygame

pygame.init()

# Load the background image
file_location_background = "./assets/images/background.png"
image_background = pygame.image.load(file_location_background)
background_rect = image_background.get_rect()
size = width, height = background_rect.width, background_rect.height

# Load the unicorn image
file_location_running_unicorn = "./assets/images/running_unicorn.gif"
image_running_unicorn = pygame.image.load(file_location_running_unicorn)
running_unicorn_rect = image_running_unicorn.get_rect()
running_unicorn_rect.bottomleft = (100, 1050)

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.blit(image_background, background_rect)
    screen.blit(image_running_unicorn, running_unicorn_rect)
    pygame.display.flip()
