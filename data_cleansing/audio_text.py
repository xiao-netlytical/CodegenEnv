import sounddevice as sd
import numpy as np
import wave
import threading

class AudioRecorder:
    def __init__(self, filename):
        self.filename = filename
        self.sample_rate = 44100
        self.channels = 1
        self.is_recording = False
        self.audio_data = []

    def record_audio(self):
        """Start recording audio."""
        self.is_recording = True
        print("Recording...")
        
        # Create a stream to record audio
        with sd.InputStream(samplerate=self.sample_rate, channels=self.channels, dtype='int16') as stream:
            while self.is_recording:
                # Read audio data from the stream
                data = stream.read(1024)[0]
                self.audio_data.append(data)

    def stop_recording(self):
        """Stop recording audio."""
        self.is_recording = False
        print("Recording finished.")

        # Save the recorded audio data to a WAV file
        self.save_audio()

    def save_audio(self):
        """Save the recorded audio to a WAV file."""
        with wave.open(self.filename, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(2)  # Sample width in bytes
            wf.setframerate(self.sample_rate)
            wf.writeframes(b''.join(self.audio_data))

import speech_recognition as sr
def transcribe_audio(filename):
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)  # Read the entire audio file
        try:
            # Transcribe the audio to text
            text = recognizer.recognize_google(audio_data, language='zh-CN')  # Change language if needed
            return text
        except sr.UnknownValueError:
            return "Audio not understood"
        except sr.RequestError as e:
            return f"Could not request results; {e}"


def audio_to_text(filename):
    recorder = AudioRecorder(filename)

    # Start recording in a separate thread
    recording_thread = threading.Thread(target=recorder.record_audio)

    # Control loop for starting and stopping the recording
    try:
        while True:
            command = input("Type 'start' to record, 'stop' to finish: ").strip().lower()
            if command == 'start' and not recorder.is_recording:
                recording_thread.start()
            elif command == 'stop' and recorder.is_recording:
                recorder.stop_recording()
                recording_thread.join()  # Wait for the recording thread to finish
                break
            else:
                print("Invalid command or already recording.")
    except KeyboardInterrupt:
        recorder.stop_recording()
        recording_thread.join()

    transcription = transcribe_audio(filename)
    print("Transcription:", transcription)
    return transcription

    
