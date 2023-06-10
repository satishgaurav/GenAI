#include <iostream>
#include "portaudio.h"

#define SAMPLE_RATE 44100
#define FRAMES_PER_BUFFER 1024
#define NUM_CHANNELS 1
#define DURATION_SECONDS 5
#define OUTPUT_FILE "output.wav"

// Data structure to hold the recorded audio
struct RecordData {
    FILE* file;
    unsigned long frameIndex;
};

// Callback function to record audio
int recordCallback(const void* inputBuffer, void* outputBuffer,
                   unsigned long framesPerBuffer,
                   const PaStreamCallbackTimeInfo* timeInfo,
                   PaStreamCallbackFlags statusFlags,
                   void* userData) {
    RecordData* data = (RecordData*)userData;
    const float* buffer = (const float*)inputBuffer;
    
    // Write the audio data to the file
    unsigned long numSamples = framesPerBuffer * NUM_CHANNELS;
    data->frameIndex += numSamples;
    fwrite(buffer, sizeof(float), numSamples, data->file);

    return paContinue;
}

int main() {
    PaStream* stream;
    PaError err;
    RecordData data;

    // Open the output file for writing
    data.file = fopen(OUTPUT_FILE, "wb");
    if (!data.file) {
        std::cout << "Failed to open output file" << std::endl;
        return 1;
    }

    // Initialize PortAudio
    err = Pa_Initialize();
    if (err != paNoError) {
        std::cout << "PortAudio initialization failed" << std::endl;
        return 1;
    }

    // Set up the stream parameters
    PaStreamParameters inputParams;
    inputParams.device = Pa_GetDefaultInputDevice();
    inputParams.channelCount = NUM_CHANNELS;
    inputParams.sampleFormat = paFloat32;
    inputParams.suggestedLatency = Pa_GetDeviceInfo(inputParams.device)->defaultLowInputLatency;
    inputParams.hostApiSpecificStreamInfo = NULL;

    // Open the stream for recording
    err = Pa_OpenStream(&stream, &inputParams, NULL, SAMPLE_RATE, FRAMES_PER_BUFFER,
                        paClipOff, recordCallback, &data);
    if (err != paNoError) {
        std::cout << "Failed to open stream for recording" << std::endl;
        return 1;
    }

    // Start the stream
    err = Pa_StartStream(stream);
    if (err != paNoError) {
        std::cout << "Failed to start recording stream" << std::endl;
        return 1;
    }

    // Wait for the specified duration
    Pa_Sleep(DURATION_SECONDS * 1000);

    // Stop the stream
    err = Pa_StopStream(stream);
    if (err != paNoError) {
        std::cout << "Failed to stop recording stream" << std::endl;
        return 1;
    }

    // Close the stream
    err = Pa_CloseStream(stream);
    if (err != paNoError) {
        std::cout << "Failed to close recording stream" << std::endl;
        return 1;
    }

    // Terminate PortAudio
    err = Pa_Terminate();
    if (err != paNoError) {
        std::cout << "PortAudio termination failed" << std::endl;
        return 1;
    }

    // Close the output file
    fclose(data.file);

    std::cout << "Recording saved to " << OUTPUT_FILE << std::endl;

    return 0;
}
