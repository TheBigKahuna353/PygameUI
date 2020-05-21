import pygame
import UI

pygame.init()
size = width, height = 500, 400
screen = pygame.display.set_mode(size)

def button_clicked():
    print("button clicked")


InputBox = UI.TextBox(100,100,100,30,background=(200,200,200), lines=2,cursor=True)

button = UI.Button(100,300,w=10,h=5,text="Button",calculateSize=True,outline=True,background = (200,200,200), action = button_clicked)
button2 = UI.Button(200,300,w=10,h=5,text="Button2",calculateSize=True,half_outline=True,background = (200,200,200), hover_background_color=(255,0,0))

button_img = pygame.Surface((30,30),pygame.SRCALPHA)
pygame.draw.line(button_img,(0,0,0),(0,5),(30,5),3)
pygame.draw.line(button_img,(0,0,0),(0,15),(30,15),3)
pygame.draw.line(button_img,(0,0,0),(0,25),(30,25),3)

button_img = UI.Button(350,300,image=button_img,enlarge=True)

running = True
# Game Loop
while running:
    screen.fill((255,255,255))
    
    InputBox.draw()
    button.update()
    if button2.update():
        print("button2 clicked")
    button_img.update()
    
    pygame.display.update()
    
    for e in pygame.event.get():             # checks all events that happen
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            InputBox.key_down(e)
        
