import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.D21, 24, brightness=0.2)

# Function to set the police light pattern with strobing effect
def police_lights(duration, speed):
    start_time = time.monotonic()
    while (time.monotonic() - start_time) < duration:
        for i in range(12):
            pixels[i] = (255, 0, 0)  # Red color for the first half
            
        time.sleep(speed)    
        pixels.fill((0, 0, 0))
        
        for i in range(12, 24):
            pixels[i] = (0, 0, 255)
            
        time.sleep(speed)
        pixels.fill((0, 0, 0))

police_lights(8, 0.5)
