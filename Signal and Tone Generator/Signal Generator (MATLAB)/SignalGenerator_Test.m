% Project: Hands-Free Intraoral Electrolarynx
% Module: Signal and Tone Generator 
% Description: This script is intended to test the SignalGenerator function 
% with three frequency values (120Hz for low frequency, 200Hz for medium 
% frequency, and 300Hz for high frequency). These frecuency values correspond 
% to the pitch options available in the Hands-Free Intraoral Electrolarynx.
% Author: Sujeily P. Fonseca-Gonzalez
% Username: Sujeily-Fonseca

clear all % Clear variables and functions 
close all % Close all the open figure windows
clc       % Clear command window

% Test No 1: 120Hz Impulse Train Signal
SignalGenerator(120, "impulse");  % Impulse train signal using 120Hz 
pause(10);                        % Wait 10 seconds 

% Test No 2: 200Hz Impulse Train Signal
SignalGenerator(200, "impulse");  % Impulse train signal using 200Hz 
pause(10);                        % Wait 10 seconds 

% Test No 3: 300Hz Impulse Train Signal
SignalGenerator(120, "impulse");  % Impulse train signal using 300Hz 
pause(10);                        % Wait 10 seconds 

% Test No 4: 120Hz Sawtooth Signal
SignalGenerator(120, "sawtooth"); % Sawtooth signal using 120Hz
pause(10);                        % Wait 10 seconds 

% Test No 5: 200Hz Sawtooth Signal
SignalGenerator(200, "sawtooth"); % Sawtooth signal using 200Hz 
pause(10);                        % Wait 10 seconds 

% Test No 6: 300Hz Sawtooth Signal
SignalGenerator(300, "sawtooth"); % Sawtooth signal using 300Hz 
pause(10);                        % Wait 10 seconds 

% Test No 7: Invalid Parameter
SignalGenerator(120, "test");

% Test No 8: Not Enough Imput Arguments
SignalGenerator(120);