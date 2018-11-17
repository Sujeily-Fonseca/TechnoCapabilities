# Project: Hands-Free Intraoral Electrolarynx
# Module: Signal and Tone Generator
# Description: This script was developed to test the ToneGenerator script.
# Author: Sujeily P. Fonseca-Gonzalez

import time
from ToneGenerator import toneGenerator

# Calling the ToneGenerator function with the different possible input. The ToneGenerator script shall be called
# from the Control Module of the Hands-Free Intraoral Electrolarynx.

# Test No 1: 120Hz
print('120Hz sound signal')
toneGenerator(120, True)  # Start sound production
time.sleep(4)             # Wait 4 seconds
toneGenerator(120, False) # Stop sound production
time.sleep(2)             # Wait 2 seconds

# Test No 2: 200Hz
print('200Hz sound signal')
toneGenerator(200, True)  # Start sound production
time.sleep(8)             # Wait 8 seconds
toneGenerator(200, False) # Stop sound production
time.sleep(2)             # Wait 2 seconds

# Test No 3: 300Hz
print('300Hz sound signal')
toneGenerator(300, True)  # Start sound production
time.sleep(4)             # Wait 4 seconds
toneGenerator(300, False) # Stop sound production
time.sleep(2)             # Wait 2 seconds