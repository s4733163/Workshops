from sense_emu import SenseHat
import time

s = SenseHat()

w = (255, 255, 255)
b = (0, 0, 0)

tick_logo = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, w,
  b, b, b, b, b, b, w, b,
  b, b, b, b, b, w, b, b,
  w, b, b, b, w, b, b, b,
  b, w, b, w, b, b, b, b,
  b, b, w, b, b, b, b, b,
  ]

cross_logo = [
  w, b, b, b, b, b, b, w,
  b, w, b, b, b, b, w, b,
  b, b, w, b, b, w, b, b,
  b, b, b, w, w, b, b, b,
  b, b, b, w, w, b, b, b,
  b, b, w, b, b, w, b, b,
  b, w, b, b, b, b, w, b,
  w, b, b, b, b, b, b, w,
  ]

g = (0, 255, 0)
r = (255, 0, 0)
b = (0, 0, 0)
green_tick = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, g,
  b, b, b, b, b, b, g, b,
  b, b, b, b, b, g, b, b,
  g, b, b, b, g, b, b, b,
  b, g, b, g, b, b, b, b,
  b, b, g, b, b, b, b, b,
  ]

red_cross = [
  r, b, b, b, b, b, b, r,
  b, r, b, b, b, b, r, b,
  b, b, r, b, b, r, b, b,
  b, b, b, r, r, b, b, b,
  b, b, b, r, r, b, b, b,
  b, b, r, b, b, r, b, b,
  b, r, b, b, b, b, r, b,
  r, b, b, b, b, b, b, r,
    ]
# the first 2 are the coorddinates
# the last 3 is the color option
# first is the x coordinate, second is the y coordinate

"""

# ACTIVITY 1

while  True:
    s.set_pixel(0, 0, 255, 0, 0)
    time.sleep(.1)
    s.set_pixel(0, 0, 0, 255, 0)
    time.sleep(.1)
    s.set_pixel(0, 0, 0, 0, 255)
    time.sleep(.5)
    s.set_pixel(0, 0, 0, 0, 0)
    time.sleep(1)
    s.set_pixel(7, 0, 255, 255, 0)
    time.sleep(1)
    s.set_pixel(7, 0, 0, 0, 0)
"""

"""
# ACTIVITY 2
# polls all the sensors
# also prints hot or cold based on temperature

while True:
    
    temperature = s.get_temperature()
    humidity = s.get_humidity()
    pressure = s.get_pressure()
    
    if temperature > 20:
        print("hot")
    else:
        print("cold")
    print("Humidity: ", humidity)
    print("Temperature:", temperature)
    print("Pressure:", pressure)
    time.sleep(5)
    
"""
"""

# print the temperature
# also changes the scroll speed and color
# also print the tick logo
while True:
    temp = s.get_temperature()
    
    s.show_message(str(temp))
    time.sleep(2)
    s.show_message(str(temp), .2, [255, 0, 255])
    
s.set_pixels(tick_logo) 
"""

while True:
    temperature = s.get_temperature()
    
    if (temperature > 20):
        s.set_pixels(green_tick)
    else:
        s.set_pixels(red_cross)
    time.sleep(1)
        
    
   