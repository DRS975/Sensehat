code:

from sense_hat import SenseHat import time 
s = SenseHat() 
s.low_light = True  
red = (255, 0, 0) 
white = (255,255,255) 
nothing = (0,0,0) 
def s_alpha():  
O = nothing 
#code for T
def t(): 
P = pink O = nothing logo = 
[ P, P, P, P, P, P, P, P, 
P, P, P, P, P, P, P, P, 
O, O, O, P, P, O, O, O, 
O, O, O, P, P, O, O, O, 
O, O, O, P, P, O, O, O, 
O, O, O, P, P, O, O, O, 
O, O, O, P, P, O, O, O, 
O, O, O, P, P, O, O, O, ] 
return logo 
def space(): 
P = pink O = nothing logo = 
[ O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O, 
O, O, O, O, O, O, O, O, 
O, O, O, O, O, O, O, O, 
O, O, O, O, O, O, O, O, 
O, O, O, O, O, O, O, O, 
O, O, O, O, O, O, O, O, 
O, O, O, O, O, O, O, O, 
] 
return logo 
images = [space,t] 
count = 0 
while True: 
s.set_pixels(images[count % len(images)]()) 
time.sleep(.75) 
count += 1 