# This is being updated on hooman
this has been included in the [https://github.com/Abdur-rahmaanJ/hooman](hooman) library and is currently being maintained


# PygameUI
UI widgets for pygame

Currently have [button](#--button), [textbox](#--textbox) and [checkbox](#--checkbox) and [other](#--other) functions

# Other Functions

## - Window(w,h) => pygame.Surface
this is a shorter way of typing `screen = pygame.display.set_mode((w,h))`

you can input a width and height, or in a tuple. If no width and height is supplied, it creates 500x500

e.g. 
``` screen = Window(500,500) 
  screen = Window((500,500))
  screen = Window()
  ```

## - update_all()
updates all widgets, easier than calling `widget.update()` on every widget 

## - curved_square(width, height, curve, color) => pygame.Surface
this creates a rectangle with curved corners.

width and height is the width and height of the rectangle

curve is the curve amount, 0 is 0 curve and 1 is full curve, giving a value above 1 or below 0 will result in a ValueError

color is the colour to draw it

returns the shape on a pygame.Surface.

# - Button

## Create a button with `UI.Button(x,y,w,h,optional_parameters])`

- x - x location of button
- y - y location of button
- w = 0 - width of the button, if 0, width will be calculated off length of text(text argument must be supplied)
- h = 0 - height of the button, if 0, height will be calculated off height of text(text argument must be supplied)
- optional_paramters - a dictionary of extra options for the button

### optional paramters

- text - the text of the button, if button is image, no text will be put on screen
- calculate_size - when set to True, it will calculate the width and height, the width and height supplied as parameters will be added to calculated.
- background - background color of the button, does not affect image
- hover_background_color - this is the colour of the background when the mouse is over the button, by default it is the background supplied
- font - the font of the text
- font_size  - the font size of the text
- font_colour - the color of the text
- outline - when set to True, an outline will be created when the mouse is over the button
- outline_half - this is the same as outline, but creates an outline for bottom and right side
- outline_thickness - the thickness of the outline
- outline_color - the color of the outline
- on_click - this is a function that will gets called when the button is clicked
- on_hover_enter - this is a function that gets called the first frame the mouse hovers over the button
- on_hover_enter - this is a function that gets called once when the mouse leaves the button
- on_hover - this is a function that gets called every frame the mouse is over the button
- surface - surface the button gets blit to, if left as None, it will use the window surface
- image - surface will be the button, using this means there can be no text, or outline
- enlarge - When enlarge is set to True, it will enlarge the image when the mouse is over the button, only when image is supplied
- enlarge_amount - the amount to enlarge by 
- dont_generate - when set to True, it will not create the images, this is handy when you cant supply the text and want to calculate the width and height. 

```
def on_click(button):
    print(button.text + " was clicked")

button = UI.Button(100, 100, 100, 100,
                   {'on_click': on_click}
                   )
```

## Methods for Button

### To update the button, you can use `button.update()` => bool
This method draws the button and calculates if the mouse has clicked the button

return True if the user clicked on the button, If the mouse is held down on the button, only return True first frame

### To change the text of the button, use `button.Update_text(text)`
This method changes the text of the button and creates the surfaces for the button, if `calculateSize = True`, it will recalculate the width and height

### You can get the rect of the Button with `button.get_rect()` => pygame.Rect
This method returns a `pygame.Rect` object with the x, y, width and height of the button 

# - TextBox
  
## Create a Inputbox with `UI.TextBox(x, y, w, h [optional parameters])`



- x - x position of the textBox
- y - y position of the textBox
- w - width of the textbox
- h - height of the textbox, when set to 0, it will use the font height, when calculateSize is True, this will be added to font height
- optional parameters - a dictionary of extra options for the textbox

### optional parameters

- line - amount of lines the textbox has/can type in
- text - starting text for textbox
- background - background color
- font_size - font size of the text
- font - font of the text
- text_colour - text color
- surface - the surface to blit to, if None is supplied, it will blit to window
- margin - the distance from when the letters start from the side of the textbox
- cursor - show a cursor
- Enter_action - a function that gets called when enter is pressed, no matter if there is more lines to write on
- calculateSize - when calculateSize is True, the height will be calculated and the height supplied will be added on top

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
    
     get_lines(lines = 2) gets 2nd line
    
     get_lines(lines = (0,2)) gets the 1st and 2nd line

The parameter `return_as_string` will return multiple lines as one string with `"\n"` representing a new line instead of a list

# - CheckBox

## Create a CheckBox with `CheckBox(x, y, w, [optional parameters])`


- x - the x position of the checkbox
- y - the y position of the checkbox
- w - the width and height of the checkbox
- optional parameters - a dictionary of extra options for the checkbox

### optional paramters

- checked - this is if the checkbox is checked or not, False by default
- background - this is the background colour of the checkbox, white by default
- outline - this outlines the object, needs to be a `UI.Outline()` object
- surface - this is the surface to draw the checkbox on, if left as None, uses Window surface
- check_width - the thickness of the x when the checkbox is checked

## methods for CheckBox

### CheckBox.update()
this updates the checkbox and draws it on the screen

## To check whether the Checkbox is checked or not

you can check if the CheckBox is checked or not by using `Checkbox.checked` or by checking if it is True

e.g. `print(Checkbox.checked)

     if CheckBox:
     
         print("The checkbox is checked"
`

# - Scroller

## Create a Scroller with `Scroll([optional parameters])`

### optional paramters

- starting_x - the start position of the horizontal slider
- starting_y - the start position of the vertical slider
- range_x - the amount of pixels to scroll by, the amount of extra pixels you want
- range_y - the amount of pixels to scroll by, the amount of extra pixels you want
- bar_color - the background color of the slider/ bar
- slider_color - the color of the slider

## to use the scroller

you can get the value of the scroll by using `scroll[0]` for horizontal and `scroll[1]` for vertical value

e.g.
```
pygame.draw.rect(screen, color, (x + scroll[0], y + scroll[1], 100, 100))
#this draws a rectangle and moves with the slider
```

# Slider

## create a slider with `Slider(x, y, w, h, [optional parameters])`

- x - the x position of the slider
- y - the y position of the slider
- w - the width of the slider
- h - the height of the slider
- optional paramters - a dictionary of extra options

### Optional paramters

- background_color - the background color of the slider/ bar
- slider_width - the width of the slider, no matter which direction, this is the horizontal size
- slider_height - the height of the slider, not matter which direction, this is the vertical size
- slider_color - the color of the slider
- starting_value - the starting value of the slider
- step - the amount the slider increments by, if left as 0, the slider will increment by the smallest amount to appear smooth
- value_range - the range of the slider, given as a list of the min and max, the slider will return its value between this range
- image - this will replace the background, the slider will go on top of the image
- direction - this can be 'horizontal' or 'vertical'
- resize_slider - When set to True, it will adjust the size of slider in porpotiion to the range
- curve - this is the amount of curve the shape of the slider
