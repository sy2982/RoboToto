import time
import board
import neopixel
import random

pixels = neopixel.NeoPixel(board.D21, 24, brightness=0.1)

# Function to fade out the rainbow sparkle gradually
def fade_out(duration):
    steps = 100
    for step in range(steps):
        brightness = .1 - step / steps
        pixels.brightness = brightness
        time.sleep(duration / steps)

# Rainbow sparkle pattern
duration = 13
start_time = time.monotonic()

while (time.monotonic() - start_time) < duration:
    for i in range(24):
        pixels[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    time.sleep(0.1)  # Adjust the sleep time for smooth animation

# Fading out the rainbow sparkle
fade_out(2)

pixels.fill((0, 0, 0))  # Turn off the pixels at the end

    