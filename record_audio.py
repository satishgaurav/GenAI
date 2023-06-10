


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
while not stop_recording:
    pass

# Stop the audio stream
stream.stop()
stream.close()

# Concatenate the recorded audio frames into a single array
audio_data = np.concatenate(audio_frames, axis=0)

# Save the recorded audio to a WAV file
sf.write(OUTPUT_FILE, audio_data, SAMPLE_RATE)
print("Audio saved to:", OUTPUT_FILE)

























# import pyaudio
# import wave

# # Set the audio settings
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 44100
# CHUNK = 1024
# RECORD_SECONDS = 5
# OUTPUT_FILE = "recorded_audio.wav"

# # Initialize PyAudio
# audio = pyaudio.PyAudio()

# # Open the audio stream
# stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

# print("Recording started...")

# # Create an empty list to store the audio frames
# frames = []

# # Record audio for the specified duration
# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)

# print("Recording finished.")

# # Stop the audio stream
# stream.stop_stream()
# stream.close()
# audio.terminate()

# # Save the recorded audio to a WAV file
# wave_file = wave.open(OUTPUT_FILE, "wb")
# wave_file.setnchannels(CHANNELS)
# wave_file.setsampwidth(audio.get_sample_size(FORMAT))
# wave_file.setframerate(RATE)
# wave_file.writeframes(b"".join(frames))
# wave_file.close()

# print("Audio saved to:", OUTPUT_FILE)
