"""
Course:      ICOM5047 - Capstone
Semester:    August-December 2018
Group:       Hands-Free Intraoral Electrolarynx
Date:        November 2, 2018
Username:    gilissaM
Name:        Gilissa M. Matos Hernandez
Description: Program that controls any interaction with the user.
             It includes the volume adjustment, the change of pitch
             between three frequencies, and the activation or
             deactivation of the signal. 
"""

""" Importing external modules """
import RPi.GPIO as GPIO
from ToneGenerator import toneGenerator
from ToneGenerator import increaseVolume
from ToneGenerator import decreaseVolume

""" Global Variables Declaration and Assignment """
signal_status = 0                                        # 0- Signal is deactivated     1- Signal is activated     
pitch_flag = 0                                           # 1- Pitch button pressed
down_flag = 0                                            # 1- Down volume button pressed
up_flag = 0                                              # 1- Up volume button pressed
signal_flag = 0                                          # 1- Signal activation/deactivation button pressed
pitch = [120,200,300]                                    # Available frequencies to generate the signal: 120Hz-Men, 200Hz-Women, and 300Hz-Child
pitch_tracker = 0                                        # Pointer to the pitch array: Default selected frequency is 120Hz


""" Handler Functions for: Volume, Pitch, and signal activation/deactivation """

# The up_flag is set only if the signal is active
def upHandler(pin):
    global up_flag, signal_status                        # Get access to the global variable
    if signal_status:
        up_flag = 1                                      # Set volume up flag to 1
        
# The up_flag is set only if the signal is active
def downHandler(pin):
    global down_flag, signal_status                      # Get access to the global variable
    if signal_status:
        down_flag = 1                                    # Set volume down flag to 1

def signalHandler(pin):
    global signal_flag                                   # Get access to the global variable
    signal_flag = 1                                      # Set signal flag to 1

# The pitch_flag is set only if the signal is deactived
def pitchHandler(pin):
    global pitch_flag, signal_status                     # Get access to the global variable
    if signal_status == 0:    
        pitch_flag = 1                                   # Set the pitch flag to 1

""" Subroutines for volume, pitch, and signal control """

# Function changePitch() toggles between the available frequencies in pitch list
def changePitch():
    global pitch_tracker
    if pitch_tracker == 0:
        GPIO.output(25, GPIO.LOW)                       # Turn off the blue led 
        GPIO.output(8,GPIO.HIGH)                        # Turn on the red led 
        pitch_tracker +=1                               # Change the pitch pointer

    elif pitch_tracker == 1:
        GPIO.output(8, GPIO.LOW)                        # Turn off the red led
        GPIO.output(7, GPIO.HIGH)                       # Turn on the yellow led
        pitch_tracker += 1                              # Change the pitch pointer
        
    else:
        GPIO.output(7, GPIO.LOW)                        # Turn off the yellow pointer
        GPIO.output(25, GPIO.HIGH)                      # Turn on the blue led
        pitch_tracker = 0                               # Change the pitch pointer

""" Ports configuration and callback assignments """
GPIO.setmode(GPIO.BCM)                                   # Referring to the pins by the Broadcom SoC channel number
GPIO.setwarnings(False)                                  # Disable Warnings

GPIO.setup(4, GPIO.IN)                                   # Increase Volume Button assigned to GPIO 4
GPIO.setup(10, GPIO.IN)                                  # Decrease Volume Button assigned to GPIO 10
GPIO.setup(15, GPIO.IN)                                  # Signal Activation/Deactivation Button and PSS assigned to GPIO 17
GPIO.setup(23, GPIO.IN)                                  # Pitch Button assigned to GPIO 22
GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)              # On/Off led indicator
GPIO.setup(25, GPIO.OUT, initial=GPIO.HIGH)              # 120Hz led indicator - Low pitch
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)                # 200Hz led indicator - Medium pitch
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)                # 300Hz led indicator - High pitch

# Callback assignments for GPIO 10, 4, 15, and 22.3
GPIO.add_event_detect(10, GPIO.FALLING, callback = downHandler, bouncetime = 250)   # Volume down button
GPIO.add_event_detect(4, GPIO.FALLING, callback = upHandler, bouncetime = 250)      # Volume up button
GPIO.add_event_detect(15, GPIO.FALLING, callback = signalHandler, bouncetime = 250) # Signal activation/deactivation button
GPIO.add_event_detect(23, GPIO.FALLING, callback = pitchHandler, bouncetime = 250)  # Pitch button

""" Wait for an interrupt """

try:    
    while (True):

        if signal_flag:
            signal_flag = 0                                         # Reset signal_flag
            if signal_status:                                       # Signal deactivation
                signal_status = 0                                   # Reset signal_status
            else:                                                   # Signal activation
                signal_status = 1                                   # Set signal_status
            toneGenerator(pitch[pitch_tracker], signal_status)      # Call toneGenerator function
        elif up_flag:
            up_flag = 0                                             # Reset up_flag
            increaseVolume()                                       # Increment the RPi volume

        elif down_flag:
            down_flag = 0                                           # Reset down_flag
            decreaseVolume()                                       # Decrement the RPi volume

        elif pitch_flag:
            pitch_flag = 0                                          # Reset pitch_flag
            changePitch()                                           # Change pitch 

except KeyboardInterrupt:
    GPIO.cleanup()                                                  # Clean all used ports 

finally:
    GPIO.cleanup()                                                  # Clean exit
        

