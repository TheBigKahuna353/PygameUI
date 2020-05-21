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
    w = 100,
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
    outline = True,
    background = (200,200,200), 
    action = button_clicked,
    dont_generate = True
)

print(button1)

#becuase we want to calculate the size of button1 without text or an image, we can use 'dont_generate = True'
#then use Update_text(text) to calculate the size

button1.Update_text("Button")

button2 = UI.Button(
    x = 200,
    y = 300,
    w = 120,
    h = 35,
    text = "Button2",
    half_outline = True,
    background = (200,200,200), 
    hover_background_color = (255,0,0)
)


#create an image for our button
button_img = pygame.Surface((30,30),pygame.SRCALPHA) #the pygame.SRCHALPHA makes it transparent
pygame.draw.line(button_img,(0,0,0),(0,5),(30,5),3)
pygame.draw.line(button_img,(0,0,0),(0,15),(30,15),3)
pygame.draw.line(button_img,(0,0,0),(0,25),(30,25),3)

#create our button using our image
button_img = UI.Button(
    x = 350,
    y = 300,
    image = button_img,
    enlarge = True, 
)


running = True
# Game Loop
while running:
    screen.fill((255,255,255))
    
    #draw and update our buttons and textbox
    InputBox.draw()
    button1.update()
    if button2.update(): #if button2 is clicked, it will return True
        print("button2 clicked")
        
    button_img.update()
    
    
    pygame.display.update()
    for e in pygame.event.get():             # checks all events that happen
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif e.type == pygame.KEYDOWN:  #if a key is pressed, update the Textbox
            InputBox.key_down(e) #supply the event to the Textbox
            print(InputBox.get_lines()) #print what is on the Inputbox
        
