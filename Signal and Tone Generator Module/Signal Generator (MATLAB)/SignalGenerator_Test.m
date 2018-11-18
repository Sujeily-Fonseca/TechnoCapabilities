% Project: Hands-Free Intraoral Electrolarynx
% Module: Signal and Tone Generator 
% Description: This script is intended to test the SignalGenerator
% function with three frequency values (120Hz for men, 200Hz for 
% women, and 300Hz for children). These frecuency values correspond to the
% pitch options available in the Hands-Free Intraoral Electrolarynx.
% Author: Sujeily P. Fonseca-Gonzalez

clear all % Clear variables and functions 
close all % Close all the open figure windows
clc       % Clear command window

% Test No 1: 120 Hz
ImpulseTrain_120Hz = SignalGenerator(120); % Impulse train using 120Hz (men)
pause(10);                                 % Wait 10 seconds 

% Test No 2: 200 Hz
ImpulseTrain_200Hz = SignalGenerator(200); % Impulse train using 200Hz (women)
pause(10);                                 % Wait 10 seconds 

% Test No 3: 300 Hz
ImpulseTrain_300Hz = SignalGenerator(300); % Impulse train using 300Hz (children)
pause(10);                                 % Wait 10 seconds 

