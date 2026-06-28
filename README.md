# VOX-macOS-python
A python script to do Voice Activated HotKey press in macOS.
Tested on macOS Sonoma. Will also support Monterey.

Made to create a Dictation machine utility with a Motorola 'biscuit' SpeakerMic using its switch and 'Handy'– an FOSS offline dictation software. Likely any mic with a PTT switch will create the loudest sound/signal to trigger and feed into this system.

These are the Terminal commands to resolve dependencies and install this software.
Brew and Python3 must be installed.

Runs as a Terminal window. (BASh)



python3.14 -m pip install --upgrade pip    
 
brew install python
 
brew install portaudio
 
pip3 install numpy
 
pip3 install pyaudio
 
pip3 install pyautogui

 
Place python script in home folder, or change command code.


Run with 'VOX.command.'

Grant necessary permissions through 'System Preferences' or 'System Settings.'

Threshold can be edited to match application.

Use case:
Tapping the computer or 'keying up' a custom microphone with a switch (Which produces an audible 'POP!')
triggers a Keystroke which is a HotKey for another software like Handy (handy.computer) in order to provide transcription services based on Microphone input following the HotKey press.

Currently configured to 'Command+NumPad *'
