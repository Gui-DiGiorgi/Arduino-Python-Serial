# This is the python code of the project, this part creates an interface with pygame to slide the colors
# Note that it requires a self made pygame support library (pygametexting)

import pygame
from pygametexting import pyg_text
import time
import serial

class slider():
    def __init__(self, x, y, width, height, size):
        
        slider.g_selected = False
        
#         Buttom config:
        self.size = size
    
#         Slider config
        self.width = width
        self.height = height
        self.s_x = x
        self.s_y = y
        self.color = (200,200,200)
#         Block config
        self.selected = False
        self.clicked = False
        self.block = width
        self.x = x
        self.y = y
        self.block_color = (100,100,100)
        
    def click(self,mouse_x,mouse_y,mouse_p):
        
        if mouse_p and not slider.g_selected:
            if self.s_x<=mouse_x<=self.s_x+self.width and self.s_y<=mouse_y<=self.s_y+self.height:
                self.selected = True
                slider.g_selected = True
                
        elif not mouse_p:
            self.selected = False
            slider.g_selected = False
            
        if pygtxt.screen_button_initpos("▲", self.s_x, self.s_y - self.size):
            
            self.clicked = True
            self.y -= 1
            
        elif pygtxt.screen_button_initpos("▼", self.s_x, self.s_y + self.height):
            
            self.clicked = True
            self.y += 1
            
        else:
            
            self.clicked = False
            
    def move(self, mouse_x, mouse_y):
        
        if self.selected:
        
            self.y = mouse_y - self.block//2
            
        if self.selected or self.clicked:

            if self.y < self.s_y:
                self.y = self.s_y

            if self.y > self.s_y + self.height - self.block:
                self.y = self.s_y + self.height - self.block

    def draw(self,window):
        pygame.draw.rect(window,self.color,(self.s_x,self.s_y,self.width,self.height))
        pygame.draw.rect(window,self.block_color,(self.x,self.y,self.block,self.block))
        
ser = serial.Serial('COM3', 9600)
if not ser.isOpen():
    ser.open()
        
pygame.init()

win=pygame.display.set_mode((600,600))

pygame.display.set_caption("Color")

clock = pygame.time.Clock()

clock_time = 30

pygtxt = pyg_text(20,(255,255,255),"msmincho",win)

black = (0,0,0)

grey = (125,125,125)

run = True

sliders = []

side = 20

init_y = 200

init_sx = 95

for i in range(3):
    sliders.append(slider(init_sx, init_y, 10, 255 + side/2, side))
    init_sx += 200
    
fake_color = [0,0,0]
    
true_color = (0,0,0)

now = time.time()

interval = 0.1

for i in sliders:
    
    i.y = 455

while run:
    
    clock.tick(clock_time)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse_p = pygame.mouse.get_pressed()
    mouse_xy = pygame.mouse.get_pos()
    
#     win.fill(true_color)
    win.fill(black)
        
    for i in sliders:
        
        i.click(mouse_xy[0], mouse_xy[1], mouse_p[0])
        i.move(mouse_xy[0], mouse_xy[1])
        i.draw(win)
        
    init_x = 100
        
    for n,i in enumerate(sliders):
        y_value = int(455 - i.y)
        pygtxt.screen_text_centerpos(y_value, init_x, 100)
        init_x += 200
        fake_color[n] = y_value
        
    true_color = tuple(fake_color)
    
    if time.time() - now >= interval:
        send_bytes(ser,pyformat(fake_color))
        now = time.time()
        
    pygame.display.update()
    
pygame.quit()
ser.close()
