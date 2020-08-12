#Ui Widgets for pygame
#this is supposed to make it as easy as possible to make and use buttons and other widgets
#Documentation at 'https://github.com/TheBigKahuna353/PygameUI'
#All made by Jordan Withell

import pygame

#make screen quick
def Window(w = 500, h = 500):
    pygame.init()
    return pygame.display.set_mode((w,h))

#instead of updating every widget individually, this func updates all created for you
def update_all():
    for widget in _all_widgets:
        widget.update()

#this is a list that holds every widget created, used by the func update_all
_all_widgets = []

#this creates a curved rect, given a w,h and the curve amount, bewtween 0 and 1
def curve_square(width,height,curve, color = (0,0,0)):
    if not 0 <= curve <= 1:
        raise ValueError("curve value out of range, must be between 0 and 1")
    curve *= min(width,height)
    curve = int(curve)
    surf = pygame.Surface((width,height),pygame.SRCALPHA)
    pygame.draw.rect(surf,color,(0,curve,width,height-2*curve))
    pygame.draw.rect(surf,color,(curve,0,width - 2 * curve,height))
    pygame.draw.circle(surf,color, (curve,curve),curve)
    pygame.draw.circle(surf,color, (width - curve,curve),curve)
    pygame.draw.circle(surf,color, (curve,height - curve),curve)
    pygame.draw.circle(surf,color, (width - curve,height - curve),curve)
    return surf



#button class
class Button:
    def __init__(self, x, y, w = 0, h = 0, param_options = {}):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.x_offset = 0
        self.y_offset = 0
        _all_widgets.append(self)
        options = {
            'surface': None,
            'hover_background_color': None,
            'font': 'Calibri',
            'font_size': 30,
            'outline': False,
            'outline_thickness':2,
            'outline_color':(0,0,0),
            'outline_half':False,
            'on_click': None,
            'on_hover_enter':None,
            'on_hover_exit':None,
            'on_hover':None,
            'image': None,
            'hover_image': None,
            'enlarge': False,
            'enlarge_amount': 1.1,
            'calculate_size': False,
            'dont_generate': False,
            'font_colour': (0, 0, 0),
            'background_color': (255, 255, 255),
            'curve': 0,
            'padding_x':0,
            'padding_y':0,
            'text':"",
            'center': False
        }
        
        for key, value in param_options.items():
            if key not in options:
                raise KeyError(key + " is not an option, is it spelt correctly")
        
        options.update(param_options)
    
        self.padding_x = options['padding_x']
        self.padding_y = options['padding_y']
        self.surface = options['surface']
        self.text_colour = options['font_colour']
        self.background = options['background_color']
        self.hover_bg_colour = options['hover_background_color']
        if self.hover_bg_colour is None:
            self.hover_bg_colour = self.background
        self.curve = options['curve']
        font = options['font']
        font_size = options['font_size']
        self.outline = options['outline']
        self.outline_col = options['outline_color']
        self.outline_half = options['outline_half']
        self.outline_amount = options['outline_thickness']
        self.on_click = options['on_click']
        self.on_hover_enter = options['on_hover_enter']
        self.on_hover_exit = options['on_hover_exit']
        self.on_hover = options['on_hover']
        image = options['image']
        dont_generate = options['dont_generate']
        self.caclulateSize = options['calculate_size']
        self.hover_image = options['hover_image']
        self.enlarge = options['enlarge']
        self.enlarge_amount = options['enlarge_amount']   
        self.text = options['text']
        self.center = options['center']
    
        # if no surface is supplied, try getting main screen
        if self.surface is None:
            self.surface = pygame.display.get_surface()
            if self.surface is None:
                raise ValueError("No surface to blit to")

        self.font = pygame.font.Font(pygame.font.match_font(font),font_size)

        self.image = image.copy() if image else None
        self.clicked_on = False
        self.draw = False
        self.clicked = False
        
        if self.enlarge:
            if self.text != "":
                self.enlarge_font = pygame.font.Font(
                    pygame.font.match_font(font), int(font_size * self.enlarge_amount))
        self.hover = False
        
        self.prev_clicked_state = False
        # create the surfaces for the button to blit every frame
        if not dont_generate:
            if self.w == 0 or self.h == 0 or self.caclulateSize:
                if image is not None:
                    self.w = self.image.get_width()
                    self.h = self.image.get_height()
                else:
                    if self.text != "":
                        self._caclulate_size()
                    else:
                        raise ValueError("cannot calculate width and height without text")
            self._Generate_images()
     
    def _Generate_images(self):     
        #generate images
        #if no image, create the button by drawing
        if self.image == None:
            self.image = pygame.Surface((self.w,self.h), pygame.SRCALPHA)
            self.hover_image = pygame.Surface((self.w,self.h), pygame.SRCALPHA)
            self.image.blit(curve_square(self.w, self.h, self.curve, self.background), (0,0))
            self.hover_image.blit(curve_square(self.w, self.h, self.curve, self.hover_bg_colour), (0,0))
            #self.hover_image.fill(self.hover_background)
            if self.outline:
                self.hover_image.blit(curve_square(self.w, self.h, self.curve, 
                                       self.outline_col), (0, 0))
                self.hover_image.blit(curve_square(self.w - self.outline_amount * 2, 
                                       self.h - self.outline_amount * 2, 
                                       self.curve, self.hover_bg_colour), 
                          (self.outline_amount, self.outline_amount))
            elif self.outline_half:
                self.hover_image.blit(curve_square(self.w, self.h, self.curve, 
                                       self.outline_col), (0, 0))
                self.hover_image.blit(curve_square(self.w - self.outline_amount,
                                                   self.h - self.outline_amount, 
                                                   self.curve,
                                                   self.hover_bg_colour), (0,0))
            self.image.convert()
        #if the user gives an image, create the image when the mouse hovers over
        elif self.hover_image == None:
            self.hover_image = self.image.copy()
            if not self.outline is None:
                pygame.draw.rect(self.hover_image,(0, 0, 0, 255), (0, 0, self.w, self.outline_amount))
                pygame.draw.rect(self.hover_image,(0, 0, 0, 255), (0 ,0 ,self.outline_amount, self.h))
                pygame.draw.rect(self.hover_image,(0, 0, 0, 255), (self.w, self.h, -self.w, -self.outline_amount))
                pygame.draw.rect(self.hover_image,(0, 0, 0, 255), (self.w, self.h, -self.outline_amount, -self.h))
            self.hover_image.convert_alpha()
            self.image.convert_alpha()
        #enlarge the image, no matter if user gives an image or not
        if self.enlarge:
            size = (int(self.w * self.enlarge_amount), int(self.h * self.enlarge_amount))
            self.dx, self.dy = size[0] - self.w, size[1] - self.h
            self.hover_image = pygame.transform.scale(self.image,size) 
        #put the text over images, if enlarge, create a bigger font so resolution stays high
        if self.text != "":
            txt = self.font.render(self.text,True,self.text_colour)
            self.image.blit(txt,((self.w - txt.get_width())//2, (self.h - txt.get_height())//2))
            if self.enlarge:
                txt = self.enlarge_font.render(self.text,True,self.text_colour)
            self.hover_image.blit(txt,((self.hover_image.get_width() - txt.get_width())//2, (self.hover_image.get_height() - txt.get_height())//2))  
        #if the user gives both images, check to see if different sizes so know if enlarged or not
        if self.hover_image.get_width() != self.w or self.hover_image.get_height() != self.h:
            self.enlarge = True
            self.dx, self.dy = self.hover_image.get_width() - self.w, self.hover_image.get_height() - self.h
        #convert the images so it is faster to put on screen
        self.image.convert()
        self.hover_image.convert()
        
            
    #if no width or height is given, calculate it with length of text
    def _caclulate_size(self):
        txt = self.font.render(self.text,False,(0,0,0))
        self.w = txt.get_width() + self.w
        self.h = txt.get_height() + self.h
    
    #return a pygame.Rect of the button
    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.w,self.h)
    
    def __bool__(self):
        return self.clicked
    
    #this is what will be shown when print(button)
    def __str__(self):
        if self.text:
            return "Button: <Text: '" + self.text + "'> " + str(self.get_rect())
        else:
            return "Button: " + str(self.get_rect()) 
    
    #update the text of the button, remake the surfaces for the button
    def Update_text(self,text):
        self.text = text
        if self.caclulateSize:
            self._caclulate_size()
        self._Generate_images()
    
    def Scroll(self, x=0, y=0):
        if x != 0:
            self.x_offset = x
        if y != 0:
            self.y_offset = y
    
    #update the button, this should get called every frame
    def update(self):
        click = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()
        self.hover = False
        returnee = False
        #check if mouse over button
        if mouse_pos[0] > self.x + self.x_offset and mouse_pos[0] < self.x + self.w + self.x_offset:
            if mouse_pos[1] > self.y + self.y_offset and mouse_pos[1] < self.y + self.y_offset + self.h:
                if self.hover == False:
                    if self.on_hover_enter:
                        self.on_hover_enter(self)
                self.hover = True
                        
                # check for click, if held down, action only gets called once
                if click and not self.prev_clicked_state:
                    self.clicked_on = True
                if self.prev_clicked_state and self.clicked_on and click == False:
                    if self.on_click:
                        '''
                        if self.on_click_arg:
                            self.on_click(self.on_click_arg)
                        else:
                            self.on_click()
                        '''
                        self.on_click(self)
                    returnee = True
                if not click:
                    self.clicked_on = False
            else:
                if self.hover:
                    if self.on_hover_exit:
                        self.on_hover_exit(self)
                self.hover = False
        else:
            if self.hover:
                if self.on_hover_exit:
                    self.on_hover_exit(self)
            self.hover = False     
        if self.hover:
            if self.on_hover:
                self.on_hover(self)
        self.prev_clicked_state = click
        #draw
        self._draw()
        #return if the button was clicked on
        self.clicked = returnee
        return returnee
    
    #draw the button
    def _draw(self):
        x = self.x + self.x_offset
        y = self.y + self.y_offset
        if self.center:
            x -= self.w//2
            y -= self.h//2
        if self.hover:
            if self.enlarge:
                self.surface.blit(self.hover_image,(x - self.dx//2,y - self.dy//2))
            else:
                self.surface.blit(self.hover_image,(x,y))
        else:
            self.surface.blit(self.image,(x,y))



#class textbox
class TextBox:
    
    def __init__(self,x, y, w, h = 0,param_options = {}):
        options = {
            'lines' : 1, 
            'text' : "", 
            'background' : None, 
            'font_size' : 30, 
            'font' : "Calibri", 
            'text_colour' : (0,0,0), 
            'surface' : None, 
            'margin' : 2, 
            'cursor' : True,
            'on_enter' : None, 
            'calculateSize' : False,
            'selectable' : False,
            'selected': True,
            'variable_size': False
        }
        for key, value in param_options.items():
            if key not in options:
                raise KeyError(key + " is not an option, is it spelt correctly")        
        options.update(param_options)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        _all_widgets.append(self)
        self.cursor = options['cursor']
        self.current_line = 0
        self.current_col = len(options['text'])
        self.lines = options['lines']
        self.font = pygame.font.Font(pygame.font.match_font(options['font']),
                                     options['font_size'])
        self.text_colour = options['text_colour']
        self.text = list(options['text'].split('\n'))
        self.wrapper()
        self.background = options['background']
        self.surface= options['surface'] if options['surface'] else pygame.display.get_surface()
        self.margin = options['margin']
        self.Enter_action = options['on_enter']   
        self.var_size = options['variable_size'] 
        #if no surface is supplied, get window
        if self.surface == None:
            raise ValueError("No surface to blit to") 
        if options['calculateSize'] or self.h == 0:
            self.h = self._get_font_height() + h
        self.selectable = options['selectable']
        self.selected = options['selected'] if self.selectable else True
        self.prev_clicked = False
    
    #get the width of the text using the font
    def _get_text_width(self,text):
        text = "".join(text)
        if len(text) == 0:
            return 0
        obj = self.font.render(text,True,(0,0,0))
        return obj.get_width()

    #returns the height of the font
    def _get_font_height(self):
        obj = self.font.render(" ",True,(0,0,0))
        return obj.get_height()
    
    #call this when the user presses a key down, supply the event from `pygame.event.get()`
    def key_down(self,e):
        if not self.selected:
            return
        #when backspace is pressed, delete last char
        if e.unicode == "":
            #if nothing in line, delete line
            if len(self.text[self.current_line]) == 0:
                if self.current_line > 0:
                    del self.text[self.current_line]
                    self.current_line -= 1
                    self.current_col = len(self.text[self.current_line])
            else:
                self.text[self.current_line] = self.text[self.current_line][:self.current_col-1] + self.text[self.current_line][self.current_col+1:]
                self.current_col -= 1
        #if key is enter, create line
        elif e.key == 13:
            if self.Enter_action:
                self.Enter_action()
            elif self.current_line < self.lines - 1:
                self.current_line += 1
                self.text.append("")
                self.current_col = 0
        #if key is a charachter, put on screen
        elif e.unicode != "":
            if len(self.text[self.current_line]) > 0:
                if self.text[self.current_line][-1] == "":
                    del self.text[self.current_line][-1]
            self.text[self.current_line] = self.text[self.current_line][:self.current_col] + e.unicode + self.text[self.current_line][self.current_col:]
            self.current_col += 1
            #wrapper
            if self._get_text_width(self.text[self.current_line]) > self.w:
                self.wrapper(True)
        #if the down arrow is pressed
        elif e.key == 274:
            self.current_line += 1 if self.current_line < len(self.text)-1 else 0
            self.current_col = min(self.current_col, len(self.text[self.current_line]))
        #if the up arrow is pressed
        elif e.key == 273:
            self.current_line -= 1 if self.current_line > 0 else 0
            self.current_col = min(self.current_col, len(self.text[self.current_line]))
        #if the right arrow is pressed
        elif e.key == 275:
            self.current_col += 1 if len(self.text[self.current_line]) > self.current_col else 0
        #if the left arrow is pressed
        elif e.key == 276:
            self.current_col -= 1 if 0 < self.current_col else 0
    
    # if text goes out of textbox, wrap it to next line
    def wrapper(self, change_cur = False):
        for cur_line, line in enumerate(self.text):
            for i in range(len(''.join(line))):
                length = self._get_text_width(''.join(line[:i]))
                if length > self.w:
                    indexs = [i for i, e in enumerate(self.text[cur_line][:i]) if e == " "]
                    if cur_line < self.lines - 1:
                        if len(indexs) == 0:
                            indexs.append(i-1)
                        if change_cur:
                            self.current_line += 1
                            self.current_col = len(self.text[cur_line]) - indexs[-1] - 1
                        if cur_line < len(self.text):
                            self.text.append(self.text[cur_line][indexs[-1]+1:])
                        else:
                            self.text[cur_line + 1] = self.text[cur_line][indexs[-1]+1:] + self.text[cur_line]
                        self.text[cur_line] = self.text[cur_line][:indexs[-1]]
                        break
    
    #draw the textbox
    def _draw(self):
        #draw background
        if self.background:
            pygame.draw.rect(self.surface, self.background, (self.x,self.y,self.w,self.h*self.lines))
        #draw all text
        for line,text in enumerate(self.text):
            if len(text) != 0:
                txt = text
                obj = self.font.render(txt,True,self.text_colour)
                self.surface.blit(obj,(self.x + self.margin,self.y +(self.h*line)))
        #draw cursor
        if self.selected:
            if self.cursor:
                total = 0
                total = self._get_text_width(self.text[self.current_line][:self.current_col])
                pygame.draw.line(self.surface,(0,0,0),(self.x + total,self.y +(self.h*self.current_line)),
                                        (self.x + total,self.y + (self.h*(self.current_line+1))),2)
                #print(self.current_col)
    
    #update should be called every frame, it draws the textbox
    def update(self):
        if self.selectable:
            mx, my = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()[0]
            clicked_on = False
            if mx > self.x and mx < self.x + self.w and my > self.y and my < self.y + self.h:
                if click:
                    if not self.prev_clicked:
                        self.selected = not self.selected
                        clicked_on = True
                        print("now selected" if self.selected else "not selected", self.text)
            if not clicked_on:
                if click:
                    if not self.prev_clicked:
                        self.selected = False
            self.prev_clicked = click
        self._draw()
    
    #get the text of a specific line or lines
    def get_lines(self, lines= -1,return_as_string = False):
        pas = False
        #if user gives an int, check if it is -1 for all lines, else get specific line
        if isinstance(lines,int):
            if lines == -1:
                lines = (0,self.lines)
                pas = True
            if not pas:
                if 0 > lines or self.lines < lines:
                    raise IndexError("line index not in range")
                if len(self.text) < lines:
                    return ""
                return "".join(self.text[lines])
        #if user wants a range of lines, get lines
        if isinstance(lines,tuple):
            if lines[0] < 0 or lines[0] > self.lines or lines[1] < 0 or lines[1] > self.lines or lines[0] > lines[1]:
                raise IndexError("line index is out of range: " + str(lines) + " (0, " + str(str(self.lines)))
            string = []
            for x in range(lines[0],lines[1]):
                if len(self.text) > x:
                    string.append("".join(self.text[x]))
                else:
                    string.append("")
            if return_as_string:
                return "\n".join(string)
            return string


#CheckBox class
class CheckBox:
    def __init__(self,x,y,w,param_options = {}):
        self.x = x
        self.y = y
        self.w = w
        
        options = {
            'checked' : False,
            'background_color' : (255,255,255),
            'outline' : False,
            'outline_amount': 2,
            'outline_color': (0,0,0),
            'outline_half': False,
            'surface' : None,
            'check_width' : 2
        }
        
        for key, value in param_options.items():
            if key not in options:
                raise KeyError(key + " is not an option, is it spelt correctly")        
        options.update(param_options)
        
        _all_widgets.append(self)
        self.checked = options['checked']
        self.backgound = options['background_color']
        self.outline = options['outline']
        self.out_amount = options['outline_amount']
        self.out_col = options['outline_color']
        self.out_half = options['outline_half']
        self._prev_click = False
        self.surface = options['surface'] if options['surface'] else pygame.display.get_surface()
        self.check_width = options['check_width']
        if self.surface == None:
            raise ValueError("No surface to blit to") 
    
    #return if checkbox is checked when converting to a bool
    def __bool__(self):
        return self.checked
    
    #return if checkbox is checked when for comparing e.g. 'if checkbox:'
    def __repr__(self):
        return self.checked
    
    #when represented as a string e.g. 'print(checkbox)'
    def __str__(self):
        return "Checkbox at (" + str(self.x) + ", " + str(self.y) + "): " + str(self.checked)
    
    #update the checkbox
    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]
        
        #check if mouse over checkbox and clicking
        if mouse[0] > self.x and mouse[0] < self.x + self.w:
            if mouse[1] > self.y and mouse[1] < self.y + self.w:
                if click:
                    if not self._prev_click:
                        self.checked = not self.checked
                        self._prev_click = True
                else:
                    self._prev_click = False
        self._draw()
    
    #draw the checkbox
    def _draw(self):
        #if outline
        if self.outline:
            pygame.draw.rect(self.surface,self.out_col,(self.x,self.y,self.w,self.w))
            pygame.draw.rect(self.surface,self.backgound,
                             (self.x + self.out_amount, self.y + self.out_amount,
                              self.w - self.out_amount*2, self.w - self.out_amount*2))
        else:
            pygame.draw.rect(self.surface,self.backgound,(self.x,self.y,self.w,self.w))
        #if checked
        if self.checked:
            pygame.draw.line(self.surface,(0, 0, 0),
                             (self.x, self.y), (self.x + self.w, self.y + self.w),self.check_width)
            pygame.draw.line(self.surface,(0, 0, 0),
                             (self.x, self.y + self.w), (self.x + self.w, self.y),self.check_width)

#scroll widget
class Scroll:
    def __init__(self, param_options = {}):
        options = {'starting_x': 0,
                   'starting_y': 0,
                   'range_x': 0,
                   'range_y': 0,
                   'bar_color': (200, 200, 200),
                   'slider_color': (150, 150, 150)}
        for key, value in param_options.items():
            if key not in options:
                raise KeyError(key + " is not an option, is it spelt correctly")        
        options.update(param_options)

        screen_size = pygame.display.get_surface().get_size()
        self.w, self.h = screen_size
        #create sliders for x and y axis
        if options['range_x'] != 0:
            self.x_slider = Slider(0, self.h - 20, self.w - 20, 20,
                                   {'starting_value': options['starting_x'],
                                    'value_range': [0, options['range_x']],
                                    'slider_color': options['slider_color'],
                                    'background_color': options['bar_color'],
                                    })
        else:
            self.x_slider = None
        if options['range_y']:
            self.y_slider = Slider(self.w - 20, 0, 20, self.h - 20,
                              {'starting_value': options['starting_y'],
                               'value_range': [0, options['range_y']],
                               'slider_color': options['slider_color'],
                               'background_color': options['bar_color'],
                               'direction': 'vertical'
                               })
        else:
            self.y_slider = None

    #this is updates the sliders, this should be called every frame
    def update(self):
        if self.x_slider is not None:
            self.x_slider.update()
        if self.y_slider is not None:
            self.y_slider.update()
    
    #returns the scroll amount given an index e.g. 'scrollx = scroll[0]'
    def __getitem__(self, index):
        if index == 0:
            if self.x_slider is not None:
                return -self.x_slider.value()
            return 0
        elif index == 1:
            if self.y_slider is not None:
                return -self.y_slider.value()
            return 0
        return (-self.x_slider.value() if self.x_slider is not None else 0,
                -self.y_slider.value() if self.y_slider is not None else 0)

#a slider widget
class Slider:
    def __init__(self, x, y, w, h, params):
        options = {
            "background_color": (100, 100, 100),
            "slider_width": None,
            "slider_color": (200, 200, 200),
            "starting_value": None,
            "value_range": [0, 1],
            "slider_height": None,
            "step": 0,
            "image": None,
            'direction': 'horizontal',
            'resize_slider': False,
            'curve': 0
        }
        for key, val in params.items():
            if key not in options:
                raise TypeError(key + " is not an option, have you spelt it correctly")

        options.update(params)

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.direction = options['direction']
        if self.direction not in ['horizontal', 'vertical']:
            raise ValueError('option \'direction\' is not a direction, (%d)' % (self.direction))
        self.bg = options["background_color"]
        #if the user gives an image for slider background, use that instead of drawing one
        if options["image"] is not None:
            self.image = pygame.Surface((self.w, self.h))
            self.image.blit(options["image"], (0, 0))
        else:
            self.image = None
        self.val_range = options["value_range"]
        self.curve = options['curve']
        self.resize = options['resize_slider']
        val_dif = self.val_range[1] - self.val_range[0]
        self.slider_bg = options["slider_color"]
        self.slider_h = options["slider_height"]
        if self.slider_h is None:
            if self.direction == 'horizontal':
                self.slider_h = h
            else:
                self.slider_h = w
        self.step = options["step"]
        if self.direction == 'horizontal':
            self.slider_w = (
                options["slider_width"] if options["slider_width"] is not None else h
            )
        else:
            self.slider_w = (
                options["slider_width"] if options["slider_width"] is not None else w
            )            
        if options["starting_value"] is not None:
            self.val = constrain(
                options["starting_value"], self.val_range[0], self.val_range[1], 0, 1
            )
        else:
            self.val = 0.5
        if self.resize:
            range_ = self.val_range[1] - self.val_range[0]
            if self.direction == 'horizontal':
                if range_ < self.w:
                    self.slider_w = self.w - range_
            else:
                if range_ < self.h:
                    self.slider_h = self.h - range_                    
        self.screen = pygame.display.get_surface()
        if self.direction == 'horizontal':
            self.slider_rect = pygame.Rect(
                self.x + self.val * (self.w - self.slider_w),
                self.y + (self.h - self.slider_h) // 2,
                self.slider_w,
                self.slider_h,
            )
        else:
            self.slider_rect = pygame.Rect(
                self.x + (self.w - self.slider_w) // 2,
                self.y + self.val * (self.h - self.slider_h),
                self.slider_w,
                self.slider_h,
            )
        self.clicked_on = False
        self.prev_click = False

    #draw the slider
    def _draw(self):
        if self.image is not None:
            self.screen.blit(self.image, (self.x, self.y))
        elif self.curve == 0:
            pygame.draw.rect(
                self.screen, self.bg, (self.x, self.y, self.w, self.h)
            )
        else:
            self.screen.blit(curve_square(self.w, self.h, self.curve, self.bg),
                             (self.x, self.y))
        if self.curve == 0:
            pygame.draw.rect(self.screen, self.slider_bg, self.slider_rect)
        else:
            self.screen.blit(curve_square(self.slider_w, self.slider_h,
                                          self.curve, self.slider_bg), self.slider_rect)

    #updates the slider, this should be called every frame
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]
        if self.slider_rect.collidepoint(mouse_pos):
            # check for click, if held down, action only gets called once
            if click and not self.prev_click:
                self.clicked_on = True
        if self.clicked_on:
            if self.direction == 'horizontal':
                self.val = (mouse_pos[0] - self.x) / self.w
                self.val = max(min(self.val, 1), 0)
                self.val = self._get_val(self.val)
                self.slider_rect.x = self.x + self.val * (self.w - self.slider_w)
            else:
                self.val = (mouse_pos[1] - self.y) / self.h
                self.val = max(min(self.val, 1), 0)
                self.val = self._get_val(self.val)
                self.slider_rect.y = self.y + self.val * (self.h - self.slider_h)
        if not click:
            self.clicked_on = False   
        self.prev_click = click
        self._draw()

    def Move(self, x = 0, y = 0, dx = 0, dy = 0):
        self.x = x if x != 0 else self.x
        self.y = y if y != 0 else self.y
        self.x += dx
        self.y += dy
        if self.direction == 'horizontal':
            self.slider_rect = pygame.Rect(
                self.x + self.val * (self.w - self.slider_w),
                self.y + (self.h - self.slider_h) // 2,
                self.slider_w,
                self.slider_h,
            )
        else:
            self.slider_rect = pygame.Rect(
                self.x + (self.w - self.slider_w) // 2,
                self.y + self.val * (self.h - self.slider_h),
                self.slider_w,
                self.slider_h,
            )

    #returns the value the slider is at
    def value(self):
        val = constrain(self.val, 0, 1, self.val_range[0], self.val_range[1])
        if isinstance(self.step, int) and self.step != 0:
            val = int(val)
        return val

    #sets the value of the slider, moveing the slider object to that position
    def set_value(self, val):
        self.val = constrain(val, self.val_range[0], self.val_range[1], 0, 1)
        self.slider_rect.x = self.x + self.val * (self.w - self.slider_w)

    #if the slider has a step and is not contineous, round to nearest step size
    def _get_val(self, val):
        if self.step == 0:
            return val
        else:
            a = constrain(val, 0, 1, self.val_range[0], self.val_range[1])
            b = round_to(a, self.step)
            c = constrain(b, self.val_range[0], self.val_range[1], 0, 1)
            # print(val, a, b, c)
            return c

#transform a value from one range to another
def constrain(val, start, end, realstart, realend):
    # mouseX 0 width 0 255
    # v = (mouseX / (end-start)) * (realend-realstart)
    # return realstart + v
    # if val < start, val = start
    # if val > end, val = end

    if val < start:
        return start
    if val > end:
        return end
    v = ((val - start) / (end - start)) * (realend - realstart)
    return realstart + v

#this returns the number rounded to a base number
def round_to_num(x, base=1):
    return base * round(x / base)
