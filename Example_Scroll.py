import pygame
import UI


pygame.init()

screen = pygame.display.set_mode((500, 500))

scroll = UI.Scroll({'range_x': 200, 'range_y': 500})

slider = UI.Slider(200, 700, 200, 30,
                   {'curve': 0.4}
                   )

running = True
while running:
    
    screen.fill((255, 255, 255))
    
    dx = scroll[0]
    dy = scroll[1]
    
    pygame.draw.rect(screen, (255, 0, 0), (100 + dx, 800 + dy, 100, 100))
    pygame.draw.rect(screen, (255, 0, 0), (300 + dx, 300 + dy, 100, 100))
    pygame.draw.rect(screen, (255, 0, 0), (100 + dx, 400 + dy, 100, 100))
    pygame.draw.rect(screen, (255, 0, 0), (200 + dx, 600 + dy, 100, 100))
    slider.Move(x = 200 + dx, y=700+dy)
    
    scroll.update()
    slider.update()
    
    pygame.display.update()
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()