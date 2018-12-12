# Project: Hands-Free Intraoral Electrolarynx
# Module: Signal and Tone Generator
# Description: The ToneGenerator script is intended to serve as a controller for the module. It is in charge of
# activating/deactivating the sound production. Furthermore, it is responsible of reproducing the appropriate sawtooth
# signal according to a given pitch value.
# Author: Sujeily P. Fonseca-Gonzalez
# Username: Sujeily-Fonseca

from pygame import mixer # Pygame module intended to loading and playing sounds
sawtooth = None          # Sawtooth signal to be generated

# TONE GENERATOR
# This function is intended to verify the status of the signal and activate/deactivate the sound production. Moreover,
# it is responsible of reproducing the audio file corresponding to the given pitch value. It is assumed that pitch and
# signal_status values were validated in the Control Module.
# pitch: 120Hz for low frequency, 200Hz for medium frequency, and 300Hz for high frequency.
# signal_status: If true, the Tone Generator must reproduce the adequate signal. Otherwise, the sound
# production must be stopped.
def toneGenerator(pitch, signal_status):
    mixer.init(48000, -16, 2, 4096)    # Initialize the mixer module (frequency=48000, size=-16, channels=2, and buffer=4096)
    global sawtooth                    # Get access to the global variable
    sawtooth = loadSoundBuffer(pitch)  # Call the sound buffer function
    if signal_status == True:
        # Activate the tone generator
        sawtooth.play(-1)              # Start the sound playback and loop indefinitely until stopped  
    else:
        # Deactivate the tone generator
        sawtooth.stop()                # Stop the sound playback if it is currently playing
        mixer.quit()                   # Quit from the mixer module

# LOAD SOUND BUFFER
# This function is responsible of loading new sound buffer from the path corresponding to the given pitch value.
# pitch: 120Hz for low frequency, 200Hz for medium frequency, and 300Hz for high frequency.
def loadSoundBuffer(pitch):
    if pitch == 200: 
        return mixer.Sound('/home/pi/Desktop/AudioFiles/200Hz_Sawtooth.wav') # Load a new sound buffer from the sawtooth signal file 
    elif pitch == 300:
        return mixer.Sound('/home/pi/Desktop/AudioFiles/300Hz_Sawtooth.wav') # Load a new sound buffer from the sawtooth signal file 
    else:
        return mixer.Sound('/home/pi/Desktop/AudioFiles/120Hz_Sawtooth.wav') # Load a new sound buffer from the sawtooth signal file

# INCREASE VOLUME
# This function is intended to increase the playback volume of the generated sawtooth signal.
# Default volume value is 1.0 (100%).
def increaseVolume():
    global sawtooth                                                # Get access to the global variable
    if sawtooth.get_volume() < 1.0:                                # Get the current playback volume 
        sawtooth.set_volume(round(sawtooth.get_volume(), 1) + 0.2) # Increase 20% the playback volume
    else:
        sawtooth.set_volume(1.0)                                    # Set volume to 100%

# DECREASE VOLUME
# This function is destined to decrease the playback volume of the generated sawtooth signal.
# Default volume value is 1.0 (100%).
def decreaseVolume():
    global sawtooth                                                # Get access to the global variable
    if sawtooth.get_volume() > 0.0:                                # Get the current playback volume
        sawtooth.set_volume(round(sawtooth.get_volume(), 1) - 0.2) # Decrease 20% the playback volume
    else:
        sawtooth.set_volume(0.0)                                    # Set volume to 0%