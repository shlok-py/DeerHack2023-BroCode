from keras.models import load_model
import numpy as np
from tensorflow.keras.utils import img_to_array, load_img
from utils import input, send_sms
import os
import time
from threading import Thread
import sys



def predict_image():
    print('Predicting image...')
    # image_dir = 'images_captured'
    # image_path = os.path.join(image_dir, f"image.jpg")
    image_path = "E:\Shit stuffs\deerhack_\images_captured\image.jpg"

    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image /= 255.0
    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model14c.h5')
    model = load_model(model_path)
    predictions = model.predict(image)
    predictions = np.argmax(predictions, axis=1)
    # predictions = 1
    print(predictions)
    # os.remove(image_path)


    # if predictions == 0:
    #     send_sms.main("Image anomaly detected")


def predict_audio():
    print('Predicting audio...')
    audio_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audio_captured', 'audio.wav')
    # code for loading and processing audio data
    # ...
    # predictions = model.predict(audio_data)
    # predictions = np.argmax(predictions, axis=1)
    predictions = 1
    # os.remove(audio_path)

    if predictions == 0:
        send_sms.main("Audio anomaly detected")
    print("Audio prediction done")


def start_threads():


    # Start the threads
    image_thread = Thread(target=predict_image)
    audio_thread = Thread(target=predict_audio)
    image_thread.start()
    audio_thread.start()

    # Wait for the threads to finish
    image_thread.join()
    audio_thread.join()


    

def main():
    print("Starting predict threads")
    start_threads()
    count = 0
    while count < 2:
        input.main()
        print(count)
        count += 1



if __name__ == '__main__':
    main()
