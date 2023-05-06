import threading
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from capture_audio import main as capture_audio
from capture_image import capture_image
from utils import predict



def main():

    # Start the audio and image capture in parallel
    audio_thread = threading.Thread(target=capture_audio)
    audio_thread.start()

    image_thread = threading.Thread(target=capture_image)
    image_thread.start()

    # Wait for the audio and image capture to finish
    audio_thread.join()
    image_thread.join()

    predict.main()




