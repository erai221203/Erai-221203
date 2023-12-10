from pygame import *
from random import *

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 600
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Car Game")

# Load images
car_image = pygame.image.load("car.png")
background_image = pygame.image.load("background.png")

# Set up the car
car_x = window_width // 2 - car_image.get_width() // 2
car_y = window_height - car_image.get_height() - 50
car_speed = 5

# Set up obstacles
obstacle_image = pygame.image.load("obstacle.png")
obstacle_list = []
obstacle_speed = 3
obstacle_interval = 60
obstacle_timer = 0

# Set up score
score = 0
font = pygame.font.SysFont("Arial", 36)

# Set up sound effects
collision_sound = pygame.mixer.Sound("collision.wav")

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_x -= car_speed
            elif event.key == pygame.K_RIGHT:
                car_x += car_speed

    # Move obstacles
    for obstacle in obstacle_list:
        obstacle.y += obstacle_speed

    # Add new obstacles
    obstacle_timer += 1
    if obstacle_timer == obstacle_interval:
        obstacle_timer = 0
        obstacle_x = random.randint(0, window_width - obstacle_image.get_width())
        obstacle_y = -obstacle_image.get_height()
        obstacle_list.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_image.get_width(), obstacle_image.get_height()))

    # Check for collisions
    car_rect = pygame.Rect(car_x, car_y, car_image.get_width(), car_image.get_height())
    for obstacle in obstacle_list:
        if car_rect.colliderect(obstacle):
            collision_sound.play()
            running = False

    # Draw the background
    window.blit(background_image, (0, 0))

    # Draw the car
    window.blit(car_image, (car_x, car_y))

    # Draw the obstacles
    for obstacle in obstacle_list:
        window.blit(obstacle_image, obstacle)

    # Update the score
    score += 1
    score_text = font.render("Score: {}".format(score))
