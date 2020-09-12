# This first part makes it easy to get the right format the Arduino to read it right
# The code list is the list for which lights to light up, and times are the miliseconds that that light will light up
# The new_song will be the right format for the Arduino code and the last part will sent it to the Arduino

import serial
import time

a = 'a'
b = 'b'
c = 'c'
d = 'd'

code = [a,a,b,c,d,c,d,b,d,d,a,b,c]

times = [200,200,500,200,200,500,500,200,200,200,200,200,500]

song = []

for c,t in zip(code,times):
    song.append([c,t])
   
new_song = []

for s in song:
    ss = s[0]+' '+str(s[1])
    new_song.append([ss])
    
for i in range(len(new_song)):
    new_song[i].append(song[i][1])
    
ser = serial.Serial('COM5', 9600)
if not ser.isOpen():
    ser.open()
                                                     
time.sleep(2)

for ss in new_song:

    byaa = []
        
    bu = ss[0]
    
    for i in bu:
        byaa.append(i.encode('utf-8')) 
    byaa.append(b'\n')
    
    
    for b in byaa:
        ser.write(b)
    
    time.sleep(ss[1]/1000+0.05)
    
ser.close()
