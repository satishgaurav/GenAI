import sounddevice as sd
import soundfile as sf
import numpy as np
import os
import threading

# Set the audio settings
SAMPLE_RATE = 44100
OUTPUT_FILE = "recorded_audio.wav"
START_FLAG_FILE = "start_flag.txt"
STOP_FLAG_FILE = "stop_flag.txt"

# Initialize an empty list to store the recorded audio frames
audio_frames = []

# Define the callback function that will be called for each audio block
def audio_callback(indata, frames, time, status):
    audio_frames.append(indata.copy())

# Read the start flag value from the file
def read_start_flag():
    if os.path.exists(START_FLAG_FILE):
        with open(START_FLAG_FILE, 'r') as file:
            return file.read().strip()
    return '0'  # Default value if the file doesn't exist

# Read the stop flag value from the file
def read_stop_flag():
    if os.path.exists(STOP_FLAG_FILE):
        with open(STOP_FLAG_FILE, 'r') as file:
            return file.read().strip()
    return '0'  # Default value if the file doesn't exist

# Start the audio stream
def start_audio_stream():
    stream = sd.InputStream(callback=audio_callback, channels=1, samplerate=SAMPLE_RATE)
    stream.start()
    return stream

# Stop the audio stream
def stop_audio_stream(stream):
    stream.stop()
    stream.close()

# Concatenate the recorded audio frames into a single array
def concatenate_audio_frames():
    return np.concatenate(audio_frames, axis=0)

# Save the recorded audio to a WAV file
def save_audio_to_file(audio_data):
    sf.write(OUTPUT_FILE, audio_data, SAMPLE_RATE)
    print("Audio saved to:", OUTPUT_FILE)

# Clear the flag files
def clear_flag_files():
    if os.path.exists(START_FLAG_FILE):
        os.remove(START_FLAG_FILE)
    if os.path.exists(STOP_FLAG_FILE):
        os.remove(STOP_FLAG_FILE)

# Main recording function
def record_audio():
    clear_flag_files()

    try:
        while True:
            start_flag = read_start_flag()
            if start_flag == '1':
                print("Start recording...")
                stream = start_audio_stream()

                stop_flag = read_stop_flag()
                while stop_flag != '1':
                    stop_flag = read_stop_flag()

                print("Stop recording...")
                stop_audio_stream(stream)
                audio_data = concatenate_audio_frames()
                save_audio_to_file(audio_data)
                clear_flag_files()
                break

    except KeyboardInterrupt:
        print("Keyboard interrupt detected. Stopping recording...")
        stop_audio_stream(stream)
        audio_data = concatenate_audio_frames()
        save_audio_to_file(audio_data)
        clear_flag_files()

# Create a separate thread for recording audio
audio_thread = threading.Thread(target=record_audio)

try:
    # Start the audio recording thread
    audio_thread.start()

    # Wait for the user to press Ctrl + C
    while True:
        pass

except KeyboardInterrupt:
    print("Keyboard interrupt detected. Stopping the program...")

finally:
    # Join the audio thread to the main thread before exiting
    audio_thread.join()
