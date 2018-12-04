# Project: Hands-Free Intraoral Electrolarynx
# Module: Signal and Tone Generator
# Description: This script was developed to test the ToneGenerator script.
# Author: Sujeily P. Fonseca-Gonzalez
# Username: Sujeily-Fonseca

import time
from ToneGenerator import toneGenerator
from ToneGenerator import increaseVolume
from ToneGenerator import decreaseVolume

# Calling the ToneGenerator function with the different possible inputs. The ToneGenerator script shall be called
# from the Control Module of the Hands-Free Intraoral Electrolarynx.

# Test No 1: 120Hz sawtooth signal
print('120Hz sound signal')
toneGenerator(120, True)  # Start sound production
time.sleep(4)             # Wait 4 seconds
toneGenerator(120, False) # Stop sound production
time.sleep(2)             # Wait 2 seconds

# Test No 2: 200Hz sawtooth signal
print('200Hz sound signal')
toneGenerator(200, True)  # Start sound production
time.sleep(8)             # Wait 8 seconds
toneGenerator(200, False) # Stop sound production
time.sleep(2)             # Wait 2 seconds

# Test No 3: 300Hz sawtooth signal
print('300Hz sound signal')
toneGenerator(300, True)  # Start sound production
time.sleep(4)             # Wait 4 seconds
toneGenerator(300, False) # Stop sound production
time.sleep(2)             # Wait 2 seconds

# Test No 4: Decrease volume
print('Volume at 100%')  
toneGenerator(200, True)  # Default volume is 1.0 (100%)
time. sleep(3)            # Wait 3 seconds
print('Volume at 80%')
decreaseVolume()          # Decrease volume to 0.8 (80%)
time. sleep(3)            # Wait 3 seconds
print('Volume at 60%')
decreaseVolume()          # Decrease volume to 0.6 (60%)
time. sleep(3)            # Wait 3 seconds
print('Volume at 40%')
decreaseVolume()          # Decrease volume to 0.4 (40%)
time. sleep(3)            # Wait 3 seconds
print('Volume at 20%')
decreaseVolume()          # Decrease volume to 0.2 (20%)
time. sleep(3)            # Wait 3 seconds
print('Volume at 0%')
decreaseVolume()          # Minimum volume 0.0 (0%)
time. sleep(3)            # Wait 3 seconds
print('Test boundary')
decreaseVolume()          # Test boundary

# Test No 5: Increase volume
print('Volume at 20%')
increaseVolume()          # Increase volume to 0.2 (20%)
time. sleep(3)            # Wait 3 seconds
print('Volume at 40%')
increaseVolume()          # Increase volume to 0.4 (40%)
time. sleep(3)            # Wait 3 seconds
print('Volume at 60%')
increaseVolume()          # Increase volume to 0.6 (60%)
time. sleep(3)            # Wait 3 seconds
print('Volume at 80%')
increaseVolume()          # Increase volume to 0.8 (80%)
time. sleep(3)            # Wait 3 seconds
print('Volume at 100%')
increaseVolume()          # Maximum volume 1.0 (100%)
time. sleep(3)            # Wait 3 seconds
print('Test boundary')
increaseVolume()          # Test boundary