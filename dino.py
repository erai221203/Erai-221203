import pygame
import random

# initialize Pygame
pygame.init()

# set up game window
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dinosaur Jumping Over Cactus Game")

# set up fonts
font = pygame.font.Font(None, 30)

# set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# set up game objects
dinosaur_img = pygame.image.load("dino.png").convert()
dinosaur_img.set_colorkey(white)
dinosaur_img = pygame.transform.scale(dino_img, (100, 80))
dinosaur_rect = dinosaur_img.get_rect()
dinosaur_rect.center = (screen_width // 4, screen_height // 2)

cactus_img = pygame.image.load("cactus.png").convert()
cactus_img.set_colorkey(white)
cactus_rect = cactus_img.get_rect()
cactus_rect.center = (screen_width, screen_height // 1)

# set up game loop
clock = pygame.time.Clock()
game_over = False

while not game_over:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not dinosaur_jump:
                dinosaur_jump = True

    # move game objects
    cactus_rect.x -= 5
    if cactus_rect.x < -cactus_rect.width:
        cactus_rect.center = (screen_width, screen_height // 2)
        dinosaur_score += 1

    if dinosaur_jump:
        if dinosaur_jump_count >= -10:
            neg = 1
            if dinosaur_jump_count < 0:
                neg = -1
            dinosaur_rect.y -= (dinosaur_jump_count ** 2) * 0.5 * neg
            dinosaur_jump_count -= 1
        else:
            dinosaur_jump = False
            dinosaur_jump_count = 10

    # check for collisions
    if dinosaur_rect.colliderect(cactus_rect):
        game_over = True

    # draw game objects
    screen.fill(white)
    screen.blit(dinosaur_img, dinosaur_rect)
    screen.blit(cactus_img, cactus_rect)
    score_text = font.render("Score: " + str(dinosaur_score), True, black)
    screen.blit(score_text, (10, 10))

    # update display
    pygame.display.update()

    # set up game clock
    clock.tick(60)

# quit Pygame
pygame.quit()
