# This is the python code of the project, this part creates an interface with pygame to slide the colors
# Note that it requires a self made pygame support library (pygametexting)

import pygame
from pygametexting import pyg_text
import time
import serial

class slider():
    def __init__(self,x,y,width):
    
        self.width = width
        self.height = width
        self.x = x
        self.y = y
        self.mouse = 0
        self.color = (200,200,200)

    def draw(self,window):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))
        
def pyformat(a):

    a_final = ""
    
    for i in a:
        a_final+=str(i)
        a_final+=' '
        
    a_final = a_final[0:(len(a_final)-1)]
    
    return a_final
    
def send_bytes(serial_name,string):
        
    bu = string
    
    byaa = []
    
    for i in bu:
        byaa.append(i.encode('utf-8')) 
    byaa.append(b'\n')
    
    for b in byaa:
        serial_name.write(b)
        
ser = serial.Serial('COM5', 9600)
if not ser.isOpen():
    ser.open()

pygame.init()

win=pygame.display.set_mode((600,600))

pygame.display.set_caption("Color")

clock = pygame.time.Clock()

clock_time = 30

txt = pyg_text(20,(255,255,255),"comicsansms",Win=win)

black = (0,0,0)

grey = (125,125,125)

run = True

sliders = []

init_y = 455

side = 20

init_sx = 95

for i in range(3):
    sliders.append(slider(init_sx, init_y, side))
    init_sx += 200
    
fake_color = [0,0,0]
    
true_color = (0,0,0)

now = time.time()

interval = 0.1

while run:
    
    clock.tick(clock_time)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse_p = pygame.mouse.get_pressed()
    mouse_xy = pygame.mouse.get_pos()
    
    
    win.fill(true_color)
    
    init_x = 100
    
    for i in range(3):
        pygame.draw.rect(win,grey,(init_x,200,10,255))
        init_x += 200
        
    for i in sliders:
        i.draw(win)
        
    for i in sliders:
        if mouse_p[0]:
            if (i.x<=mouse_xy[0]<=i.x+side) and (i.y<=mouse_xy[1]<=i.y+side) and (i.mouse == 0):
                pygame.time.delay(15)
                i.mouse = 1
            else:
                pygame.time.delay(15)
                i.mouse = 0
                
    for i in sliders:
        if i.mouse == 1:
            i.y = mouse_xy[1]-10
            if i.y>455:
                i.y = 455
            elif i.y<200:
                i.y = 200
                
    init_x = 100
    
    for i in sliders:
        y_value = 455 - i.y
        txt.screen_text_centerpos(y_value,init_x,100)
        init_x += 200
        
    for i in range(3):
        fake_color[i] = 455 - sliders[i].y
        
    true_color = tuple(fake_color)
    
    if time.time() - now >= interval:
        send_bytes(ser,pyformat(fake_color))
        now = time.time()
        
    pygame.display.update()
    
pygame.quit()
ser.close()
