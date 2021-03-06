# It should collect the arduino sent lines in lists, which include the numbers on that line as items on the list if not bigger than 255

def direction_test(numbers):
    
    joy_values = numbers
    
    d = ""
    
    if (joy_values[1]<90) and (abs(joy_values[1]-90)>=abs(joy_values[0]-90)):
        d = "0 #Up"
    if (joy_values[1]>=90) and (abs(joy_values[1]-90)>=abs(joy_values[0]-90)):
        d = "1 #Down"
    if (joy_values[0]<90) and (abs(joy_values[0]-90)>=abs(joy_values[1]-90)):
        d = "2 #Left"
    if (joy_values[0]>=90) and (abs(joy_values[0]-90)>=abs(joy_values[1]-90)):
        d = "3 #Right"
        
    return d

import serial

c=""
size = 2
t_ins = []

def collect():
    global c
    global a
    global t_ins
    try:
        c = int(c)
        if c<=255:
            t_ins.append(c)
            c = ""
    except:
        pass
    c=""

ser = serial.Serial('COM5', 9600)

if not ser.isOpen():
    ser.open()

while(True):
    a = ser.read()
    if a!=b'\n' and a!=b' ':
        c+=a.decode('utf-8')
    if a==b' ':
        collect()
    if a==b'\n':
        collect()
        if len(t_ins)==size:
            print("{0} - {1}".format(t_ins,direction_test(t_ins)),end = "\r")
        t_ins = []
    
ser.close()
