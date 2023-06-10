import sounddevice as sd
import soundfile as sf
import numpy as np
import time

# Set the audio settings
SAMPLE_RATE = 44100
OUTPUT_FILE = "recorded_audio.wav"

# Initialize an empty list to store the recorded audio frames
audio_frames = []

# Function to check the recording flag from the shared file
def check_recording_flag():
    try:
        with open("recording_flag.txt", "r") as flag_file:
            flag_value = flag_file.read().strip()
            return flag_value == "1"
    except FileNotFoundError:
        return False

# Define the callback function that will be called for each audio block
def audio_callback(indata, frames, time, status):
    if check_recording_flag():
        audio_frames.append(indata.copy())

# Start the audio stream
stream = sd.InputStream(callback=audio_callback, channels=1, samplerate=SAMPLE_RATE)
stream.start()

# Wait for a short duration to avoid buffered noise
time.sleep(1)

# Record audio while the recording flag is set
while check_recording_flag():
    time.sleep(0.1)

# Stop the audio stream
stream.stop()
stream.close()

# Check if any audio frames were recorded
if len(audio_frames) > 0:
    # Concatenate the recorded audio frames into a single array
    audio_data = np.vstack(audio_frames)

    # Save the recorded audio to a WAV file
    sf.write(OUTPUT_FILE, audio_data, SAMPLE_RATE)
    print("Audio saved to:", OUTPUT_FILE)
else:
    print("No audio recorded.")
