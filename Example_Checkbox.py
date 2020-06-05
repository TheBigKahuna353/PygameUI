import pygame
import UI


#setup pygame
pygame.init()
screen = UI.Window(500,400) #creates a window 500x400


checkBox = UI.CheckBox(
    250,
    250,
    30, 
    {
        'outline' : UI.Outline(),
        'background' : (200,200,200)
    }
)

print(checkBox.backgound)


running = True
# Game Loop
while running:
    pygame.display.update()
    screen.fill((255,255,255))
    
    
    checkBox.update()
    
    
    if checkBox:
        print("checkBox = true")
    
    for e in pygame.event.get():             # checks all events that happen
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
