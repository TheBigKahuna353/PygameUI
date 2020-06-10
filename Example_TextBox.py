import pygame
import UI


#setup pygame
pygame.init()
screen = UI.Window(500,400) #creates a window 500x400


#create our textBoxes
InputBox = UI.TextBox(
    x = 100,
    y = 100,
    w = 300,
    h = 30,
    param_options = {
        'background' : (200,200,200), 
        'lines' : 2,
        'cursor' : True
    }
)

def On_enter_press(textbox):
    print(textbox.get_lines(return_as_string = True))

InputBox2 = UI.TextBox(
    x = 100,
    y = 200,
    w = 300,
    h = 30,
    param_options = {
        'background' : (200,200,200), 
        'lines' : 3,
        'cursor' : False,
        'text': 'this is a bunch of text to put on the textbox to see if it will wrap'
    }
)


running = True
# Game Loop
while running:
    pygame.display.update()
    screen.fill((255,255,255))
    
    
    #draw and update our buttons and textbox
    InputBox.update()
    InputBox2.update()
    
    
    
    for e in pygame.event.get():             # checks all events that happen
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif e.type == pygame.KEYDOWN:  #if a key is pressed, update the Textbox
            InputBox.key_down(e) #supply the event to the Textbox
            print(InputBox.get_lines()) #print what is on the Inputbox
            print(InputBox.current_col)
