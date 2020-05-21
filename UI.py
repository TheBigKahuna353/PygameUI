#template for buttons and textboxes in pygame

import pygame

#make screen quick
screen = None
def Window(w = 500, h = 500):
    global screen
    pygame.init()
    screen = pygame.display.set_mode((w,h))
    return screen

#button class
class Button:
    def __init__(self,x,y,w= 0,h=0, calculateSize = False,text="",background = (255,255,255),font = "Calibri", font_size = 30, font_colour = (0,0,0), outline = False, outline_amount = 2, half_outline = False,action = None, action_arg = None, surface = None, image = None, enlarge = False, enlarge_amount = 1.1, hover_image = None, dont_generate = False, hover_background_color = None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.surface = surface
        #if no surface is supplied, try getting 
        if self.surface == None:
            self.surface = pygame.display.get_surface()
            if self.surface == None:
                raise ValueError("No surface to blit to")
        self.text = text
        self.text_colour = font_colour
        self.background = background
        self.hover_background = self.background if hover_background_color == None else hover_background_color
        self.font = pygame.font.Font(pygame.font.match_font(font),font_size)
        self.outline = outline
        self.outline_amount = outline_amount
        self.half_outline = half_outline
        self.action = action
        self.image = image
        self.hover_image = hover_image
        self.enlarge = enlarge
        self.enlarge_amount = enlarge_amount
        self.action_arg = action_arg
        self.hover = False
        self.caclulateSize = calculateSize
        self.prev_clicked_state = False
        if not dont_generate:
            if self.w == 0 or self.h == 0 or self.caclulateSize:
                if image != None:
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
        if self.image == None:
            self.image = pygame.Surface((self.w,self.h))
            self.hover_image = pygame.Surface((self.w,self.h))
            self.image.fill(self.background)
            #self.hover_image.fill(self.hover_background)
            if self.outline:
                ow = self.outline_amount * 2
                pygame.draw.rect(self.hover_image,self.hover_background,(self.outline_amount,self.outline_amount,self.w-ow,self.h - ow))
            elif self.half_outline:
                pygame.draw.rect(self.hover_image,self.hover_background,(0,0, self.w-self.outline_amount,self.h-self.outline_amount))
            txt = self.font.render(self.text,True,self.text_colour)
            self.image.blit(txt,((self.w - txt.get_width())//2, (self.h - txt.get_height())//2))
            self.hover_image.blit(txt,((self.w - txt.get_width())//2, (self.h - txt.get_height())//2))
        elif self.hover_image == None:
            self.hover_image = self.image.copy()
        if self.enlarge:
            size = (int(self.w * self.enlarge_amount), int(self.h * self.enlarge_amount))
            self.dx, self.dy = size[0] - self.w, size[1] - self.h
            self.hover_image = pygame.transform.scale(self.image,size)        
        
            
    #if no width or height is given, calculate it with length of text
    def _caclulate_size(self):
        txt = self.font.render(self.text,False,(0,0,0))
        self.w = txt.get_width() + self.w
        self.h = txt.get_height() + self.h
    
    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.w,self.h)
    
    #this is what will be shown when print(button)
    def __str__(self):
        if self.text:
            return "Button: '" + self.text + "'"
        else:
            return "Button: at (" + str(self.x)  + ", " + str(self.y) + ")"  
    
    #update the text of the button, remake the surfaces for the button
    def Update_text(self,text):
        self.text = text
        if self.caclulateSize:
            self._caclulate_size()
        self._Generate_images()
        print(self.image, text)
    
    
    #update the button, this should get called every frame
    def update(self):
        click = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()
        self.hover = False
        returnee = False
        #check if mouse over button
        if mouse_pos[0] > self.x and mouse_pos[0] < self.x+self.w:
            if mouse_pos[1] > self.y and mouse_pos[1] < self.y+self.h:
                self.hover = True
                #check for click, if held down, action only gets caleed once
                if click and not self.prev_clicked_state:
                    returnee = True
                    if self.action:
                        if self.action_arg:
                            self.action(self.action_arg)
                        else:
                            self.action()
        self.prev_clicked_state = click
        #draw
        self._draw()
        #return if the button was clicked on
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
    
    def __init__(self,x, y, w, h = 0,lines = 1, text = "", background = None, font_size = 30, font = "Calibri", text_colour = (0,0,0), surface = None, margin = 2, cursor = True,Enter_action = None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.cursor = cursor
        self.current_line = 0
        self.current_col = len(text)
        self.lines = lines
        self.font = pygame.font.Font(pygame.font.match_font(font),font_size)
        self.text_colour = text_colour
        self.text = [list(text)]
        self.char_length = [self._get_text_width(x) for x in self.text]
        self.background = background
        self.surface= surface
        self.margin = margin
        self.Enter_action = Enter_action
        #if no surface is supplied, get window
        if self.surface == None:
            self.surface = pygame.display.get_surface()
            if self.surface == None:
                raise ValueError("No surface to blit to")
    
    #get the width of the text using the font
    def _get_text_width(self,text):
        text = "".join(text)
        if len(text) == 0:
            return 0
        obj = self.font.render(text,True,(0,0,0))
        return obj.get_width()
    
    #call this when the user presses a key down, supply the event from `pygame.event.get()`
    def key_down(self,e):
        #when backspace is pressed, delete last char
        if e.unicode == "":
            #if nothing in line, delete line
            if len(self.text[self.current_line]) == 0:
                if self.current_line > 0:
                    del self.text[self.current_line]
                    self.current_line -= 1
                    self.current_col = self.char_length[self.current_line][-1]
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
                self.char_length.append([0])
                self.current_col = 0
        #if key is a charachter, put on screen
        elif e.unicode != "":
            self.text[self.current_line] = self.text[self.current_line][:self.current_col] + [e.unicode] + self.text[self.current_line][self.current_col:]
            self.current_col += 1
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
            self.current_col += 1 if len(self.text[self.current_line]) - 1 > self.current_col else 0
        #if the left arrow is pressed
        elif e.key == 276:
            self.current_col -= 1 if 0 < self.current_col else 0
    
    #draw the textbox
    def draw(self):
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
        
