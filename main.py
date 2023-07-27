import pygame as pg

pg.init()
pg.font.init()
WIDTH, HEIGHT = 800, 700
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND = (211, 211, 211)
HEALTH_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (255, 255, 255)
BORDER_COLOR = (0, 0, 0)
imageP = pg.image.load("narutoback.png")
imageP1 = pg.image.load("hiddenleaftransparent.png")
imageE = pg.image.load("luffyforward.png")
imageE1 = pg.image.load("luffyshiplogo.png")
scaledImageP = pg.transform.scale(imageP, (150, 240))
scaledImageP1 = pg.transform.scale(imageP1, (150, 110))
scaledImageE = pg.transform.scale(imageE, (230, 300))
scaledImageE1 = pg.transform.scale(imageE1, (200, 120))

# Define the health bar parameters
health_width = 20
health_height = 5
max_health = 100
current_health = 100

# Create a rect for the health bar
health_bar = pg.Rect(10, 10, health_width, health_height)

running = True
health = 100

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Anime Showdown")
clock = pg.time.Clock()

while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False


    screen.fill(BACKGROUND)
    bar_width = 150
    bar_height = 20
    bar_filled_width = int((health / 100) * bar_width)

    # Draw the background and border of the health bar
    #Naruto
    pg.draw.rect(screen, BORDER_COLOR, (10, 228, bar_width, bar_height))
    pg.draw.rect(screen, BACKGROUND_COLOR, (12, 230, bar_width - 4, bar_height - 4))
    #Luffy
    pg.draw.rect(screen, BORDER_COLOR, (WIDTH - 172, 198, bar_width, bar_height))
    pg.draw.rect(screen, BACKGROUND_COLOR, (WIDTH - 170, 200, bar_width - 4, bar_height - 4))

    # Draw the filled part of the health bar based on the health percentage
    #Naruto
    pg.draw.rect(screen, HEALTH_COLOR, (12, 230, bar_filled_width - 4, bar_height - 4))
    #Luffy
    pg.draw.rect(screen, HEALTH_COLOR, (WIDTH - 170, 200, bar_filled_width - 4, bar_height - 4))
    screen.blit(scaledImageP, (0,250))
    screen.blit(scaledImageE, (WIDTH - 220, 175))
    screen.blit(scaledImageP1, (0, 100))
    screen.blit(scaledImageE1, (WIDTH - 200, 10))




    pg.display.flip()