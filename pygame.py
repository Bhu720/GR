import pygame

pygame.init()
fps = 60
clock = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paint')

WHITE = (255, 255, 255)
BLACK = (5, 8, 9)
current_color = BLACK

drawing = False
radius = 5

run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
        if event.type == pygame.MOUSEBUTTONUP:

            if event.button == 1:

                drawing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                screen.fill(WHITE)
            if event.key == pygame.K_r:
                current_color = (255, 0, 0)
            if event.key == pygame:

                current_color = BLACK
            if event.key == pygame:

                pygame.image.save(screen, "painting.jpg")


            if drawing:
                 pos = pygame.mouse.get_pos()
                 pygame.draw.circle(screen, current_color, pos, radius)
                 pygame.display.update()
                 pygame.quit()
