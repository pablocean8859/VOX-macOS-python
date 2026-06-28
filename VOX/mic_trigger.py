import pyaudio  
import numpy as np  
import os  
import time 

### --- CONFIGURATION ---
THRESHOLD = 22000  # Sound spike sensitivity (Raise if too sensitive, lower if it misses)  
COOLDOWN = 1.0     # Seconds to wait before allowing another trigger 
### ---------------------

FORMAT = pyaudio.paInt16  
CHANNELS = 1  
RATE = 44100  
CHUNK = 1024 

p = pyaudio.PyAudio()  
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK) 

print("Listening for microphone switch noise... Press Ctrl+C to stop.")  
last_trigger = 0 

try:  
    while True:  
        data = stream.read(CHUNK, exception_on_overflow=False)  
        audio_data = np.frombuffer(data, dtype=np.int16) 

        # Calculate the peak volume of the current audio chunk  
        peak = np.max(np.abs(audio_data)) 

        if peak > THRESHOLD:  
            current_time = time.time()  
            if current_time - last_trigger > COOLDOWN:  
                print(f"💥 Noise detected (Level: {peak})! Triggering Cmd+kp*...") 

                # Executes AppleScript triggering Command + Keypad Asterisk
                os.system("osascript -e 'tell application \"System Events\" to key code 67 using command down'")

                last_trigger = current_time  
except KeyboardInterrupt:  
    print("\nStopping...")  
finally:  
    stream.stop_stream()  
    stream.close()  
    p.terminate()