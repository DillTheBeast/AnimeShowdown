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
color_light = (170,170,170)
color_dark = (100,100,100)
imageP = pg.image.load("narutoback.png")
imageP1 = pg.image.load("hiddenleaftransparent.png")
imageE = pg.image.load("luffyforward.png")
imageE1 = pg.image.load("luffyshiplogo.png")
scaledImageP = pg.transform.scale(imageP, (150, 240))
scaledImageP1 = pg.transform.scale(imageP1, (150, 110))
scaledImageE = pg.transform.scale(imageE, (230, 300))
scaledImageE1 = pg.transform.scale(imageE1, (200, 120))

buttonFont = pg.font.SysFont("Times New Roman", 50)
button1 = buttonFont.render('Attack1' , True , WHITE)
button2 = buttonFont.render('Attack2' , True , WHITE)
button3 = buttonFont.render('Attack3' , True , WHITE)

buttonClick = False
done1 = False
done = False

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

        #If clicked setting buttonClick to true
        if event.type == pg.MOUSEBUTTONDOWN:         
            #if the mouse is clicked then game starts
            if WIDTH/2-70 <= mouse[0] <= WIDTH/2+140 and HEIGHT - 60 <= mouse[1] <= HEIGHT+80:
                buttonClick = True

    screen.fill(BACKGROUND)
    mouse = pg.mouse.get_pos()
    bar_width = 150
    bar_height = 20
    bar_filled_width = int((health / 100) * bar_width)
    
    if WIDTH/2-70 <= mouse[0] <= WIDTH/2+200 and HEIGHT - 60 <= mouse[1] <= HEIGHT+100:
        pg.draw.rect(screen,color_light,[WIDTH/2 - 70,HEIGHT - 60, 200, 100])        
    else:
        pg.draw.rect(screen,color_dark,[WIDTH/2 - 70,HEIGHT - 60, 200, 100])


    screen.blit(button1 , (WIDTH/2 - 70 + 35/2,HEIGHT - 60))
    #Naruto
    pg.draw.rect(screen, BORDER_COLOR, (10, 228, bar_width, bar_height))
    pg.draw.rect(screen, BACKGROUND_COLOR, (12, 230, bar_width - 4, bar_height - 4))
    #Luffy
    pg.draw.rect(screen, BORDER_COLOR, (WIDTH - 172, 138, bar_width, bar_height))
    pg.draw.rect(screen, BACKGROUND_COLOR, (WIDTH - 170, 140, bar_width - 4, bar_height - 4))

    # Draw the filled part of the health bar based on the health percentage
    #Naruto
    pg.draw.rect(screen, HEALTH_COLOR, (12, 230, bar_filled_width - 4, bar_height - 4))
    #Luffy
    pg.draw.rect(screen, HEALTH_COLOR, (WIDTH - 170, 140, bar_filled_width - 4, bar_height - 4))
    screen.blit(scaledImageP, (0,250))
    screen.blit(scaledImageE, (WIDTH - 220, 125))
    screen.blit(scaledImageP1, (0, 100))
    screen.blit(scaledImageE1, (WIDTH - 200, 10))




    pg.display.flip()