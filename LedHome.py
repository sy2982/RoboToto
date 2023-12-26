import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.D21, 24, brightness=0.1)
wait = .25
time.sleep(1)
# Fading to red
for i in range(100):
    red_value = i
    green_value = 0
    blue_value = 0
    for j in range(13, 19):
        pixels[j] = (red_value, green_value, blue_value)
    time.sleep(0.001)

# Fading to green
for i in range(100):
    red_value = 100 - i
    green_value = i
    blue_value = 0
    for j in range(13, 19):
        pixels[j] = (red_value, green_value, blue_value)
    time.sleep(0.0005)
    
time.sleep(wait)
# Fading to red
for i in range(100):
    red_value = i
    green_value = 0
    blue_value = 0
    for j in range(7, 13):
        pixels[j] = (red_value, green_value, blue_value)
    time.sleep(0.001)

# Fading to green
for i in range(100):
    red_value = 100 - i
    green_value = i
    blue_value = 0
    for j in range(7, 13):
        pixels[j] = (red_value, green_value, blue_value)
    time.sleep(0.0005)

time.sleep(wait)
# Fading to red
for i in range(100):
    red_value = i
    green_value = 0
    blue_value = 0
    for j in range(1, 7):
        pixels[j] = (red_value, green_value, blue_value)
    time.sleep(0.001)

# Fading to green
for i in range(100):
    red_value = 100 - i
    green_value = i
    blue_value = 0
    for j in range(1, 7):
        pixels[j] = (red_value, green_value, blue_value)
    time.sleep(0.0005)

# Fading to red
for i in range(100):
    red_value = i
    green_value = 0
    blue_value = 0
    for j in range(19, 24):
        pixels[0] = (red_value, green_value, blue_value)
        pixels[j] = (red_value, green_value, blue_value)
    time.sleep(0.001)

# Fading to green
for i in range(100):
    red_value = 100 - i
    green_value = i
    blue_value = 0
    for j in range(19, 24):
        pixels[0] = (red_value, green_value, blue_value)
        pixels[j] = (red_value, green_value, blue_value)
    time.sleep(0.00005)
    
pixels.fill((0, 0, 0))
time.sleep(.1)
pixels.fill((0, 100, 0))
time.sleep(.1)
pixels.fill((0, 0, 0))
time.sleep(.1)
pixels.fill((0, 100, 0))
time.sleep(.1)
pixels.fill((0, 0, 0))
time.sleep(.1)
pixels.fill((0, 100, 0))
time.sleep(.5)
pixels.fill((0, 0, 0))