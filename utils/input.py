import cv2
import pyaudio
import wave
import time
import threading
import os

# Initialize the camera
def main():
    cap = cv2.VideoCapture(0)

    # Define the time interval between captures (in seconds)
    capture_interval = 5

    # Define the audio and image directories
    audio_dir = 'audio_captured'
    image_dir = 'images_captured'

    # Create the directories if they don't exist
    if not os.path.exists(audio_dir):
        os.makedirs(audio_dir)
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # Define the audio settings
    audio_format = pyaudio.paInt16
    channels = 1
    sample_rate = 44100
    chunk_size = 1024
    record_duration = 5

    # Define a variable to keep track of when the next capture should occur
    next_capture_time = time.time()

    # Define a function to capture audio
    def capture_audio():
        audio_data = []
        audio = pyaudio.PyAudio()
        stream = audio.open(format=audio_format, channels=channels, rate=sample_rate, input=True, frames_per_buffer=chunk_size)
        for i in range(0, int(sample_rate / chunk_size * record_duration)):
            audio_data.append(stream.read(chunk_size))
        stream.stop_stream()
        stream.close()
        audio.terminate()
        audio_frames = b''.join(audio_data)
        wav_file = wave.open(os.path.join(audio_dir, 'audio.wav'), 'wb')
        wav_file.setnchannels(channels)
        wav_file.setsampwidth(audio.get_sample_size(audio_format))
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio_frames)
        wav_file.close()

    # Define a function to capture an image
    def capture_image():
        ret, frame = cap.read()
        filename = os.path.join(image_dir, f"image.jpg")
        cv2.imwrite(filename, frame)

    # Start the audio and image capture in parallel
    audio_thread = threading.Thread(target=capture_audio)
    audio_thread.start()

    image_thread = threading.Thread(target=capture_image)
    image_thread.start()

    # Wait for the audio and image capture to finish
    audio_thread.join()
    image_thread.join()
