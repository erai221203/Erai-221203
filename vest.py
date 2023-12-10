import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Armor-like Shape Animation")

# Colors
black = (0, 0, 0)
gray = (150, 150, 150)

# Armor parameters
armor_points = [
    (400, 100),
    (300, 300),
    (500, 300)
]

armor_speed = 3
armor_rotation_speed = 0.05
armor_angle = 0

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update armor position and rotation
    armor_angle += armor_rotation_speed
    armor_x = width // 2
    armor_y = height // 2

    # Clear the screen
    screen.fill(black)

    # Draw the armor-like shape
    rotated_armor_points = [
        (
            armor_x + (point[0] - armor_x) * math.cos(armor_angle) - (point[1] - armor_y) * math.sin(armor_angle),
            armor_y + (point[0] - armor_x) * math.sin(armor_angle) + (point[1] - armor_y) * math.cos(armor_angle)
        )
        for point in armor_points
    ]
    pygame.draw.polygon(screen, gray, rotated_armor_points)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
