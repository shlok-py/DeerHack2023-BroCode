import time
import pyaudio
import wave
import os 
import predict
from send_sms import main as send_sms


def main():
    audio_dir = 'audio_captured'
    if not os.path.exists(audio_dir):
        os.makedirs(audio_dir)

    audio_format = pyaudio.paInt16
    channels = 1
    sample_rate = 44100
    chunk_size = 1024
    record_duration = 5


    print('Capturing audio...')
    audio_data = []
    audio = pyaudio.PyAudio()
    stream = audio.open(format=audio_format, channels=channels, rate=sample_rate, input=True, frames_per_buffer=chunk_size)
    for i in range(0, int(sample_rate / chunk_size * record_duration)):
        audio_data.append(stream.read(chunk_size))
    stream.stop_stream()
    stream.close()
    audio.terminate()
    audio_frames = b''.join(audio_data)
    wav_file = wave.open(os.path.join(audio_dir, f"audio.wav"), 'wb')
    wav_file.setnchannels(channels)
    wav_file.setsampwidth(audio.get_sample_size(audio_format))
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(audio_frames)
    wav_file.close()


    