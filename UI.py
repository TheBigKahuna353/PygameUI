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
            'text':""
        }
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
    
    
    #update the button, this should get called every frame
    def update(self):
        click = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()
        self.hover = False
        returnee = False
        #check if mouse over button
        if mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.w:
            if mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.h:
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
        if self.hover:
            if self.enlarge:
                self.surface.blit(self.hover_image,(self.x - self.dx//2,self.y - self.dy//2))
            else:
                self.surface.blit(self.hover_image,(self.x,self.y))
        else:
            self.surface.blit(self.image,(self.x,self.y))



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
            'Enter_action' : None, 
            'calculateSize' : False
        }
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
        self.text = [list(options['text'].split('\n'))]
        self.wrapper()
        self.char_length = [self._get_text_width(x) for x in self.text]
        self.background = options['background']
        self.surface= options['surface'] if options['surface'] else pygame.display.get_surface()
        self.margin = options['margin']
        self.Enter_action = options['Enter_action']        
        if self.surface == None:
            raise ValueError("No surface to blit to")        
        #if no surface is supplied, get window
        if self.surface == None:
            self.surface = pygame.display.get_surface()
            if self.surface == None:
                raise ValueError("No surface to blit to")
        if options['calculateSize'] or self.h == 0:
            self.h = self._get_font_height() + h
    
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
        #when backspace is pressed, delete last char
        if e.unicode == "":
            #if nothing in line, delete line
            if len(self.text[self.current_line]) == 0:
                if self.current_line > 0:
                    del self.text[self.current_line]
                    self.current_line -= 1
                    self.current_col = len(self.text[self.current_line])
            else:
                del self.text[self.current_line][-1]
                self.current_col -= 1
        #if key is enter, create line
        elif e.key == 13:
            if self.Enter_action:
                self.Enter_action()
            elif self.current_line < self.lines - 1:
                self.current_line += 1
                self.text.append([""])
                self.current_col = 0
        #if key is a charachter, put on screen
        elif e.unicode != "":
            if len(self.text[self.current_line]) > 0:
                if self.text[self.current_line][-1] == "":
                    del self.text[self.current_line][-1]
            self.text[self.current_line] = self.text[self.current_line][:self.current_col] + [e.unicode] + self.text[self.current_line][self.current_col:]
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
    
    def wrapper(self, change_cur = False):
        for cur_line, line in enumerate(self.text):
            for i in range(len(line)):
                length = self._get_text_width(line[:i])
                if length > self.w:
                    indexs = [i for i, e in enumerate(self.text[cur_line]) if e == " "]
                    if cur_line < self.lines - 1:
                        if change_cur:
                            self.current_line += 1
                            self.current_col = len(self.text[cur_line]) - indexs[-1]
                        if cur_line < len(self.text):
                            self.text.append(self.text[cur_line][indexs[-1]+1:])
                        else:
                            self.text[cur_line + 1] = self.text[cur_line][indexs[-1]+1:] + self.text[cur_line]
                        self.text[cur_line] = self.text[cur_line][:indexs[-1]]
    
    #draw the textbox
    def _draw(self):
        #draw background
        if self.background:
            pygame.draw.rect(self.surface, self.background, (self.x,self.y,self.w,self.h*self.lines))
        #draw all text
        for line,text in enumerate(self.text):
            if len(text) != 0:
                txt = "".join(text)
                obj = self.font.render(txt,True,self.text_colour)
                self.surface.blit(obj,(self.x + self.margin,self.y +(self.h*line)))
        #draw cursor
        if self.cursor:
            total = 0
            total = self._get_text_width(self.text[self.current_line][:self.current_col])
            pygame.draw.line(self.surface,(0,0,0),(self.x + total,self.y +(self.h*self.current_line)),
                                     (self.x + total,self.y + (self.h*(self.current_line+1))),2)
            #print(self.current_col)
    
    #update should be called every frame, it draws the textbox
    def update(self):
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
            'background' : (255,255,255),
            'outline' : None,
            'surface' : None,
            'check_width' : 2
        }
        
        options.update(param_options)
        
        _all_widgets.append(self)
        self.checked = options['checked']
        self.backgound = options['background']
        self.out = options['outline']
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
        if self.out:
            pygame.draw.rect(self.surface,(0,0,0),(self.x,self.y,self.w,self.w))
            pygame.draw.rect(self.surface,self.backgound,(self.x + self.out.s,self.y + self.out.s,self.w - self.out.s*2,self.w - self.out.s*2))
        else:
            pygame.draw.rect(self.surface,self.backgound,(self.x,self.y,self.w,self.w))
        #if checked
        if self.checked:
            pygame.draw.line(self.surface,(0,0,0),(self.x,self.y), (self.x + self.w,self.y + self.w),self.check_width)
            pygame.draw.line(self.surface,(0,0,0),(self.x,self.y + self.w), (self.x + self.w,self.y),self.check_width)
        

class Scroll:
    def __init__(self,surface = None):
        pass