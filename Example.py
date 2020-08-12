import pygame
import UI


#setup pygame
pygame.init()
screen = UI.Window(500,500) #creates a window 500x500

#this function will run when button1 is clicked
def button_clicked(btn):
    print("button clicked")

#create our textBoxes and Buttons
InputBox = UI.TextBox(
    x = 100,
    y = 100,
    w = 300,
    h = 30,
    param_options={
        'background':(200,200,200), 
        'lines' : 2,
        'cursor' : True
    }
)
button1 = UI.Button(
    x = 100,
    y = 300,
    w = 10,
    h = 5,
    param_options={
        'calculate_size' : True,
        'outline' : True,
        'background_color' : (200,200,200), 
        'on_click' : button_clicked,
        'dont_generate' : True,
        'curve':0.5,
        'center': True
    }
)

#becuase we want to calculate the size of button1 without text or an image, we can use 'dont_generate = True'
#then use Update_text(text) to calculate the size

button1.Update_text("Button")

print(button1)

button2 = UI.Button(
    x = 200,
    y = 300,
    w = 120,
    h = 35,
    param_options={
        'curve': 0.3,
        'text' : "Button2",
        'background_color' : (200, 200, 200), 
        'hover_background_color' : (240, 240, 240),
        'outline_half': False
    }
)


#create an image for our button
#img = UI.curve_square(120,35,0.4,(200,200,200))
img = pygame.Surface((100, 50), pygame.SRCALPHA)
hover_img = UI.curve_square(110, 60, 0.4, (0 ,0 ,200))

#create our button using our image
button_img = UI.Button(
    x = 100,
    y = 100,
    param_options={
        'image' : img,
        'enlarge' : True, 
    }
)
button_img2 = UI.Button(
    x = 250,
    y = 350,
    param_options={
        'image' : img,
        'hover_image':hover_img,
        'text' : "Button4"
    }
)


checkBox = UI.CheckBox(
    300,
    180,
    30, 
    {
        'outline':True,
        'background_color': (200, 200, 200)
    }
)

running = True
# Game Loop
while running:
    pygame.display.update()
    screen.fill((255,255,255))
    
    #pygame.draw.rect(screen,(255,0,0),(100,100,100,100))
    
    #draw and update our buttons and textbox
    InputBox.update()
    button1.update()
    if button2.update(): #if button2 is clicked, it will return True
        print("button2 clicked")
        
    if button_img.update():
        print("clicked invisible button")
    button_img2.update()
    checkBox.update()
    
    
    
    if checkBox:
        print("checkBox = true")
    
    for e in pygame.event.get():             # checks all events that happen
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif e.type == pygame.KEYDOWN:  #if a key is pressed, update the Textbox
            InputBox.key_down(e) #supply the event to the Textbox
            print(InputBox.get_lines()) #print what is on the Inputbox
        
