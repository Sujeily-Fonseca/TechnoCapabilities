% Project: Hands-Free Intraoral Electrolarynx
% Module: Signal and Tone Generator 
% Description: The signalGenerator function is intended to produce an 
% impulse train signal according to a given pitch value. As for example: 
% 120Hz for men, 200Hz for women, and 300Hz for children).
% Author: Sujeily P. Fonseca-Gonzalez

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                   FORMAT FOR INPUT/OUTPUT VARIABLES                     %
% pitch: Although the Hands-Free Intraoral Electrolarynx  project is      %
% focused on only three values for the pith, this function does not       %
% require a validation of the inputs because the signals are generated by %
% the person in charge of the module.                                     %
%                                                                         %
% impulse_train: Signal generated according to the given picth value. At  %
% the end, the output signal is also stored in a .wav file.               %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function impulse_train = signalGenerator(pitch)

    %---------------------------------------------------------------------%
    %                         DEFINING VARIABLES                          %
    %---------------------------------------------------------------------%
    Fs = 48000;         % Common sampling rate in audio
    Ts = 1/Fs;          % Sample period 
    f = round(pitch);   % Number of cycles per second (120Hz for male, 200Hz for 
                        % women, and 300Hz for children)
    t = 0:Ts:10;        % 10 seconds long signal)

    %---------------------------------------------------------------------%
    %                           IMPULSE TRAIN                             %
    %---------------------------------------------------------------------%
    impulse_train = zeros(size(t));     % Impulse train signal 
    
    %Calculate how many samples per cycle
    duration = (Fs/f);                  % Duration of the signal
    impulse_train(1:duration:end) = 1;  % Plugging ones in the zero array
    sound(impulse_train, Fs);           % Generating the sound
    file_name = join(['ImpulseTrain_',int2str(pitch),'Hz']); % Name of the 
                                                             % audio file
    audiowrite(join([file_name,'.wav']), impulse_train, Fs); % Saving signal 
                                                             % in a .wav format
                                                                                                              
    %---------------------------------------------------------------------%
    %                            SIGNAL PLOT                              %
    %---------------------------------------------------------------------%
    figure('Name', file_name, 'units','normalized','outerposition',[0 0 1 1]); % Open figure in full screen
    stem(t,impulse_train);              % Signal plot
    xlabel('Time (seconds)');           % Naming the x-axis
    ylabel('Amplitude');                % Naming the y-axis 
    title ((join(['Impulse Train Signal - ',int2str(pitch),'Hz']))); % Plot title
    xlim ([0 1])                        % Limiting x-axis to 1 second
end