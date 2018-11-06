"""
Course:      ICOM5047 - Capstone
Semester:    August-December 2018
Group:       Hands-Free Instraoral Electrolarynx
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
import subprocess
import time

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
    global up_flag, signal_status
    if signal_status:
        up_flag = 1
        
# The up_flag is set only if the signal is active
def downHandler(pin):
    global down_flag, signal_status
    if signal_status:
        down_flag = 1

def signalHandler(pin):
    global signal_flag
    signal_flag = 1

# The pitch_flag is set only if the signal is deactived
def pitchHandler(pin):
    global pitch_flag, signal_status
    if signal_status == 0: 
        pitch_flag = 1

""" Subroutines for volume, pitch, and signal control """

# Function changePitch() toggles between the available frequencies in pitch list
def changePitch():
    global pitch_tracker
    if pitch_tracker >= (len(pitch)-1):
        pitch_tracker = 0

    else:
        pitch_tracker += 1
        
    print("The selected pitch is: %d." % (pitch[pitch_tracker]))

# Function decrementVolume() decrements the PCM volume on card 0 using amixer commands 
def decrementVolume():
    subprocess.Popen(['amixer','set','PCM','10db-'], shell=False)

# Function decrementVolume() increments the PCM volume on card 0 using amixer commands
def incrementVolume():
    subprocess.Popen(['amixer','set','PCM','10db+'], shell= False)


""" Ports configuration and callback assignments """
GPIO.setmode(GPIO.BCM)                                   # Referring to the pins by the Broadcom SoC channel number
GPIO.setwarnings(False)                                  # Disable Warnings

GPIO.setup(4, GPIO.IN)                                   # Increase Volume Button assigned to GPIO 4
GPIO.setup(10, GPIO.IN)                                  # Decrease Volume Button assigned to GPIO 10
GPIO.setup(17, GPIO.IN)                                  # Signal Activation/Deactivation Button and PSS assigned to GPIO 17
GPIO.setup(22, GPIO.IN)                                  # Pitch Button assigned to GPIO 22

# Callback assignments for GPIO 10, 4, 17, and 22.
GPIO.add_event_detect(10, GPIO.FALLING, callback = downHandler, bouncetime = 2)
GPIO.add_event_detect(4, GPIO.FALLING, callback = upHandler, bouncetime = 2)
GPIO.add_event_detect(17, GPIO.FALLING, callback = signalHandler, bouncetime = 2)
GPIO.add_event_detect(22, GPIO.FALLING, callback = pitchHandler, bouncetime = 2)

    
""" Wait for an interrupt """

while (True):

    if signal_flag:
        signal_flag = 0                                         # Reset signal_flag
        if signal_status:
            signal_status = 0                                   # Reset signal_status
            #Signal Deactivation Code
            print("Disable Signal!")
        else:
            #Signal Activation Code
            signal_status = 1                                   # Set signal_status
            print("Enable Signal!")
    elif up_flag:
        up_flag = 0                                             # Reset up_flag
        incrementVolume()                                       # Increment the RPi volume

    elif down_flag:
        down_flag = 0                                           # Reset down_flag
        decrementVolume()                                       # Decrement the RPi volume

    elif pitch_flag:
        pitch_flag = 0                                          # Reset pitch_flag
        changePitch()                                           # Change pitch 

    
