# PygameUI
UI widgets for pygame

Currently have button and textbox

- Button

Create a button with 'UI.Button()'

All paramters are optional except x and y location but you need to rather call 'UI.createWindow()' or send the window surface as the surface argument

Arguments for Button(x,y,w= 0,h=0,text="",background = (255,255,255),font = "Calibri", font_size = 30, text_colour = (0,0,0), outline = False, outline_amount = 2, half_outline = False, offset = [0,0],action = None, action_arg = None, surface = None, image = None, enlarge = False, enlarge_amount = 1.1)

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

