# PygameUI
UI widgets for pygame

Currently have button and textbox

# - Button

## Create a button with `UI.Button(x,y,[optional parameters])`

## All paramters are optional except x and y location


### Arguments for `Button(x,y,w= 0,h=0,text="", calculateSize = False,background = (255,255,255),font = "Calibri", font_size = 30, text_colour = (0,0,0), outline = False, outline_amount = 2, half_outline = False,action = None, action_arg = None, surface = None, image = None, enlarge = False, enlarge_amount = 1.1)`


- x - x location of the button
- y - y location of the button
- w = 0 - width of the button, if 0, width will be calculated off length of text(text argument must be supplied)
- h=0 - height of the button, if 0, height will be calculated off height of text(text argument must be supplied)
- text="" - the text of the button, if button is image, no text will be put on screen
- calculateSize = False - when set to True, it will calculate the width and height, the width and height supplied as parameters will be added to calculated.
- background = (255,255,255) - background color of the button, does not affect image
- hover_background_color = None - this is the colour of the background when the mouse is over the button, by default it is the background supplied
- font = "Calibri" - the font of the text
- font_size = 30  - the font size of the text
- font_colour = (0,0,0) - the color of the text
- outline = False - when set to True, if the mouse is over the button, it will outline the button
- outline_amount = 2 - the amount to outline of the button when outline = True or half_outline = True, this does not make the button bigger, but smaller
- half_outline = False - when set to True, it will outline 2 sides of the button instead of all 4 in outline
- action = None - function that gets called when button clicked
- action_arg = None - argument for action function
- surface = None - surface the button gets blit to, if left as None, it will use the window surface
- image = None - surface will be the button, using this means there can be no text, or outline
- enlarge = False - When enlarge is set to True, it will enlarge the image when the mouse is over the button, only when image is supplied
- enlarge_amount = 1.1 - the amount to enlarge by 
- dont_generate = False - when set to True, it will not create the images, this is handy when you cant supply the text and want to calculate the width and height. 

## Methods for Button

### To update the button, you can use `button.update()` => bool
This method draws the button and calculates if the mouse has clicked the button

return True if the user clicked on the button, If the mouse is held down on the button, only return True first frame

### To change the text of the button, use `button.Update_text(text)`
This method changes the text of the button and creates the surfaces for the button, if `calculateSize = True`, it will recalculate the width and height

### You can get the rect of the Button with `button.get_rect()` => pygame.Rect
This method returns a `pygame.Rect` object with the x, y, width and height of the button 

# - TextBox
  
## Create a Inputbox with `UI.TextBox(x, y, w, [optional parameters])`


### arguments for `TextBox(self,x, y, w, h = 0,lines = 1, text = "", background = None, font_size = 30, font = "Calibri", text_colour = (0,0,0), surface = None, margin = 2, cursor = True,Enter_action = None)`

all optional except x,y, width and height, it syas height it optional but if you want background, you need to supply height

- x = 0 - x position of the textBox
- y = 0 - y position of the textBox
- w = 0 - width of the textbox
- h = 0 - height of the textbox
- lines = 1 - amount of lines the textbox has/can type in
- text = "" - starting text for textbox
- background = False - background color
- font_size = 30 - font size of the text
- font = "Calibri" - font of the text
- text_colour = (0,0,0) - text color
- surface = None - the surface to blit to, if None is supplied, it will blit to window
- margin = 2 - the distance from when the letters start from the side of the textbox
- cursor = True - show a cursor
- Enter_action = None - a function that gets called when enter is pressed, no matter if there is more lines to write on

## methods for textbox

### - `textbox.key_down(event)`
event is a pygame.event()
best way to do this is 
`for event in pygame.event.get()`
`    if e.type == pygame.KEYDOWN:`
`        textbox.key_down(event)`

### - `textbox.draw()`
draws the textbox

### - `textbox.get_rect()` => pygame.Rect
This method returns a `pygame.Rect` object with the x, y, width and height of the textbox

### - `textbox.get_lines(lines = -1, return_as_string = False)` => string or list
This method returns the text on a specific line or lines, by defualt, it returns all lines
The parameter `lines`, it the line or lines you want, this can be an integer of the line or a tuple of 2 integers that are the start and end lines 
e.g. 
    `get_lines()`, gets all lines  
    `get_lines(lines = 2)` gets 2nd line
    `get_lines(lines = (0,2))` gets the 1st and 2nd line

The parameter `return_as_string` will return multiple lines as one string with `"\n"` representing a new line instead of a list

# - CheckBox

## Create a CheckBox with `CheckBox(x, y, w, [optional parameters])`

### arguments for `CheckBox(x,y,w,checked=False,background=(255,255,255),outline=True,outline_amount=2,surface=None,check_width = 2)`
- x - the x position of the checkbox
- y - the y position of the checkbox
- w - the width and height of the checkbox
- checked = False - this is if the checkbox is checked or not, False by default
- background = (0,0,0) - this is the background colour of the checkbox, white by default
- outline = True - when True, creates a black border around the edge of the box
- outline_amount = 2 - this is the thickness of the border, by default it is 2
- surface = None - this is the surface to draw the checkbox on, if left as None, uses Window surface
- check_width = 2 - the thickness of the x when the checkbox is checked
