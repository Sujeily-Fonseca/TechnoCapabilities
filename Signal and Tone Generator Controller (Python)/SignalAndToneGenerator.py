# Project: Hands-Free Intraoral Electrolarynx
# Module: Signal and Tone Generator
# Description: The signalAndToneGenerator script is intended to serve as a controller for the module. It is in charge of
# activate/deactivate the sound production. Furthermore, it is responsible of reproducing the appropriate impulse train
# signal according to a given pitch value.
# Author: Sujeily P. Fonseca-Gonzalez

import os

# SIGNAL AND TONE GENERATOR
# This function is intended to verify the status of the signal and activate/deactivate the sound production. Moreover,
# it is responsible of calling the soundProduction function.
# pitch: 120Hz for men, 200Hz for women, and 300Hz for children.
# signal_status: If true, the Signal and Tone Generator must reproduce the adequate signal. Otherwise, the sound
# production must be stopped.
def signalAndToneGenerator(pitch, signal_status):
    if signal_status == True:
        #Activate tone generator
        reproduce = True
        soundProduction(pitch, reproduce)
    else:
        #Deactivate tone generator
        reproduce = False
        soundProduction(pitch, reproduce)

# SOUND PRODUCTION
# This function is responsible of reproducing the audio file corresponding to the given pitch value.
# reproduce: If true, sound production is attained. Otherwise, sound is not produced.
# filepath: Path of the desired audio file
def soundProduction(pitch, reproduce):
    if reproduce == True:
        getfilepath(pitch)
     
# GET FILE PATH
# This function is responsible of selecting the path corresponding to the given pitch value.
# Returns the path for the desired .wav file.
def getfilepath(pitch):
    if pitch == 200: 
        os.system('aplay /home/pi/Desktop/AudioFiles/ImpulseTrain_200Hz.wav')
    elif pitch == 300:
        os.system('aplay /home/pi/Desktop/AudioFiles/ImpulseTrain_300Hz.wav')
    else:
        os.system('aplay /home/pi/Desktop/AudioFiles/ImpulseTrain_120Hz.wav')