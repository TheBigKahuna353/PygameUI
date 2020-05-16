from pygame import *
import UI

init()
size = width, height = 700, 700
screen = display.set_mode(size)


InputBox = UI.TextBox(100,100,100,30,background=(200,200,200), lines=2,cursor=True)

button = UI.Button(100,300,w=10,h=5,text="Button",calculateSize=True,outline=True,background = (200,200,200))
button2 = UI.Button(200,300,w=10,h=5,text="Button2",calculateSize=True,half_outline=True,background = (200,200,200))


running = True
# Game Loop
while running:
    screen.fill((255,255,255))
    
    InputBox.draw()
    button.update()
    button2.update()
    
    display.update()
    
    for e in event.get():             # checks all events that happen
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            InputBox.key_down(e)
        
