# PygameUI
UI widgets for pygame

Currently have button and textbox

- Button

Create a button with `UI.Button()`

All paramters are optional except x and y location but you need to rather call 'UI.createWindow()' or send the window surface as the surface argument


Arguments for `Button(x,y,w= 0,h=0,text="",background = (255,255,255),font = "Calibri", font_size = 30, text_colour = (0,0,0), outline = False, outline_amount = 2, half_outline = False, offset = [0,0],action = None, action_arg = None, surface = None, image = None, enlarge = False, enlarge_amount = 1.1)`


- x - x location of the button
- y - y location of the button
- w = 0 - width of the button, if 0, width will be calculated off length of text(text argument must be supplied)
- h=0 - height of the button, if 0, height will be calculated off height of text(text argument must be supplied)
- text="" - the text of the button, if button is image, no text will be put on screen
- background = (255,255,255) - background color of the button, does not affect image
- font = "Calibri" - the font of the text
- font_size = 30  - the font size of the text
- text_colour = (0,0,0) - the color of the text
- outline = False - when set to True, if the mouse is over the button, it will outline the button
- outline_amount = 2 - the amount to outline of the button when outline = True or half_outline = True, this does not make the button bigger, but smaller
- half_outline = False - when set to True, it will outline 2 sides of the button instead of all 4 in outline
- offset = [0,0] - how much room in between the border of the button and the text, mainly used is width or height not supplied
- action = None - function that gets called when button clicked
- action_arg = None - argument for action function
- surface = None - surface the button gets blit to
- image = None - surface will be the button, using this means there can be no text, or outline
- enlarge = False - When enlarge is set to True, it will enlarge the image when the mouse is over the button, only when image is supplied
- enlarge_amount = 1.1 - the amount to enlarge by 

To update the button, you can use `button.update(mouse_position,click)`

this method draws the button and calculates if the mouse has clicked the button

- TextBox

***Work in Progress***
  
Create a Inputbox with `UI.TextBox()`


arguments for `TextBox(x = 0, y = 0, w = 0, h = 0, text = "", background = False, font_size = 30, font = "Calibri", text_colour = (0,0,0))`

- x = 0 - x position of the textBox
- y = 0 - y position of the textBox
- w = 0 - width of the textbox
- h = 0 - height of the textbox
- text = "" - starting text for textbox
- background = False - background color
- font_size = 30 - font size of the text
- font = "Calibri" - font of the text
text_colour = (0,0,0) - text color

methods for textbox

- Add_char(key)
key is ascii number of key
can be `pygame.keys.get()`
adds the key to the text, if the key is backspace, the last char is deleted

- Get_obj()
draws the background if there is one, and returns surface of the text

- Get_pos()
return position as (x,y)
