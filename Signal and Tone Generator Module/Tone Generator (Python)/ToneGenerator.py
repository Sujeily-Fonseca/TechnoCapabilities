# Project: Hands-Free Intraoral Electrolarynx
# Module: Signal and Tone Generator
# Description: The ToneGenerator script is intended to serve as a controller for the module. It is in charge of
# activating/deactivating the sound production. Furthermore, it is responsible of reproducing the appropriate impulse train
# signal according to a given pitch value.
# Author: Sujeily P. Fonseca-Gonzalez
# Username: Sujeily-Fonseca

from pygame import mixer # Pygame module intended to loading and playing sounds

# TONE GENERATOR
# This function is intended to verify the status of the signal and activate/deactivate the sound production. Moreover,
# it is responsible of reproducing the audio file corresponding to the given pitch value. It is assumed that pitch and
# signal_status values were validated in the Control Module.
# pitch: 120Hz for men, 200Hz for women, and 300Hz for children.
# signal_status: If true, the Tone Generator must reproduce the adequate signal. Otherwise, the sound
# production must be stopped.
def toneGenerator(pitch, signal_status):
    mixer.init()               # Initialize the mixer module
    impulseTrain = loadSoundBuffer(pitch)
    if signal_status == True:
        # Activate the tone generator
        impulseTrain.play(-1)  # Start the sound playback and loop indefinitely until stopped  
    else:
        # Deactivate the tone generator
        impulseTrain.stop()    # Stop the sound playback if ii is currently playing
        mixer.quit()           # Quit from the mixer module

# LOAD SOUND BUFFER
# This function is responsible of loading new sound buffer from the path corresponding to the given pitch value.
# pitch: 120Hz for men, 200Hz for women, and 300Hz for children.
def loadSoundBuffer(pitch):
    if pitch == 200: 
        return mixer.Sound('/home/pi/Desktop/AudioFiles/ImpulseTrain_200Hz.wav') # Load a new sound buffer from the impulse train file 
    elif pitch == 300:
        return mixer.Sound('/home/pi/Desktop/AudioFiles/ImpulseTrain_300Hz.wav') # Load a new sound buffer from the impulse train file 
    else:
        return mixer.Sound('/home/pi/Desktop/AudioFiles/ImpulseTrain_120Hz.wav') # Load a new sound buffer from the impulse train file  