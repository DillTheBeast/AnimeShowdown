import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 400, 50
HEALTH_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (255, 255, 255)
BORDER_COLOR = (0, 0, 0)

# Initialize the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Health Bar")

def draw_health_bar(health):
    bar_width = WIDTH - 10
    bar_height = HEIGHT - 10
    bar_filled_width = int((health / 100) * bar_width)

    # Draw the background and border of the health bar
    pygame.draw.rect(screen, BORDER_COLOR, (5, 5, bar_width, bar_height))
    pygame.draw.rect(screen, BACKGROUND_COLOR, (7, 7, bar_width - 4, bar_height - 4))

    # Draw the filled part of the health bar based on the health percentage
    pygame.draw.rect(screen, HEALTH_COLOR, (7, 7, bar_filled_width - 4, bar_height - 4))

# Main loop
health = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the health value here (e.g., based on the player's actions)
    # For the example, we'll just decrement the health value each frame
    health -= 0.1

    # Clamp health value between 0 and 100
    health = max(health, 0)
    health = min(health, 100)

    screen.fill((255, 255, 255))
    draw_health_bar(health)

    pygame.display.update()