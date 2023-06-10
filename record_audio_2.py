import sounddevice as sd
import soundfile as sf
import numpy as np

# Set the audio settings
SAMPLE_RATE = 44100
OUTPUT_FILE = "recorded_audio.wav"

# Initialize an empty list to store the recorded audio frames
audio_frames = []

# Define the callback function that will be called for each audio block
def audio_callback(indata, frames, time, status):
    audio_frames.append(indata.copy())

# Start the audio stream
stream = sd.InputStream(callback=audio_callback, channels=1, samplerate=SAMPLE_RATE)
stream.start()

# Keep recording until the stop flag is set
stop_recording = False
input("Press Enter to start recording...")
print("Recording started. Press Enter to stop recording.")
input()
stop_recording = True

# Stop the audio stream
stream.stop()
stream.close()

# Concatenate the recorded audio frames into a single array
audio_data = np.concatenate(audio_frames, axis=0)

# Save the recorded audio to a WAV file
sf.write(OUTPUT_FILE, audio_data, SAMPLE_RATE)
print("Audio saved to:", OUTPUT_FILE)
