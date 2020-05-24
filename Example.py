import pygame
import UI


#setup pygame
pygame.init()
screen = UI.Window(500,400) #creates a window 500x400

#this function will run when button1 is clicked
def button_clicked():
    print("button clicked")

#create our textBoxes and Buttons
InputBox = UI.TextBox(
    x = 100,
    y = 100,
    w = 300,
    h = 30,
    background=(200,200,200), 
    lines = 2,
    cursor = True
)
button1 = UI.Button(
    x = 100,
    y = 300,
    w = 10,
    h = 5,
    calculateSize = True,
    outline = UI.Outline(),
    background = (200,200,200), 
    action = button_clicked,
    dont_generate = True
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
    text = "Button2",
    background = (200,200,200), 
    hover_background_color = (240,240,240),
    outline=UI.Outline("half",outline_color=(200,200,200))
)


#create an image for our button
img = UI.curve_square(120,35,0.4,(200,200,200))
hover_img = UI.curve_square(130,45,0.4,(200,200,200))

#create our button using our image
button_img = UI.Button(
    x = 350,
    y = 300,
    image = img,
    enlarge = True, 
    text = "Button3"
)
button_img2 = UI.Button(
    x = 350,
    y = 350,
    image = img,
    hover_image=hover_img,
    text = "Button4"
)


checkBox = UI.CheckBox(
    300,
    180,
    30, 
    background=(200,200,200)
)


running = True
# Game Loop
while running:
    pygame.display.update()
    screen.fill((255,255,255))
    
    #draw and update our buttons and textbox
    InputBox.update()
    button1.update()
    if button2.update(): #if button2 is clicked, it will return True
        print("button2 clicked")
        
    button_img.update()
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
        
