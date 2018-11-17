# Project: Hands-Free Intraoral Electrolarynx
# Module: Signal and Tone Generator
# Description: The ToneGenerator script is intended to serve as a controller for the module. It is in charge of
# activate/deactivate the sound production. Furthermore, it is responsible of reproducing the appropriate impulse train
# signal according to a given pitch value.
# Author: Sujeily P. Fonseca-Gonzalez

import pygame # Sound module shall be used to control the playback of music in the sound mixer.

# TONE GENERATOR
# This function is intended to verify the status of the signal and activate/deactivate the sound production. Moreover,
# it is responsible of reproducing the audio file corresponding to the given pitch value.
# pitch: 120Hz for men, 200Hz for women, and 300Hz for children.
# signal_status: If true, the Tone Generator must reproduce the adequate signal. Otherwise, the sound
# production must be stopped.
def toneGenerator(pitch, signal_status):
    pygame.init()                    # Initialize pygame modules
    if signal_status == True:
        #Activate tone generator
        loadFile(pitch)              # Load the appropiate .wav file
        pygame.mixer.music.play(-1)  # Start the playback of the sound stream      
    else:
        #Deactivate tone generator
        pygame.mixer.music.stop()    # Stop the music playback if ii is currently playing

# LOAD FILE
# This function is responsible of loading the path corresponding to the given pitch value.
# pitch: 120Hz for men, 200Hz for women, and 300Hz for children.
def loadFile(pitch):
    if pitch == 200: 
        pygame.mixer.music.load('/home/pi/Desktop/AudioFiles/ImpulseTrain_200Hz.wav') # Load the sound file and prepare it for playback
    elif pitch == 300:
        pygame.mixer.music.load('/home/pi/Desktop/AudioFiles/ImpulseTrain_300Hz.wav') # Load the sound file and prepare it for playback
    else:
        pygame.mixer.music.load('/home/pi/Desktop/AudioFiles/ImpulseTrain_120Hz.wav') # Load the sound file and prepare it for playback