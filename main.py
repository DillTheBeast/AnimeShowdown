import pygame as pg

pg.init()
pg.font.init()
WIDTH, HEIGHT = 800, 700
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND = (211, 211, 211)
imageP = pg.image.load("narutoback.png")
imageH = pg.image.load("fullhealthreal.png")
scaledImageP = pg.transform.scale(imageP, (150, 240))
scaledImageH = pg.transform.scale(imageH, (250, 47.3977))
# Define the health bar parameters
health_width = 200
health_height = 20
max_health = 100
current_health = 100

# Create a rect for the health bar
health_bar = pg.Rect(10, 10, health_width, health_height)

running = True

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Anime Showdown")
clock = pg.time.Clock()

while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False


    screen.fill(BACKGROUND)
    screen.blit(scaledImageP, (0,250))
    screen.blit(scaledImageH, (0, 200))




    pg.display.flip()