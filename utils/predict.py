from keras.models import load_model
import numpy as np
from tensorflow.keras.utils import img_to_array, load_img
from utils import input, send_sms, image_dic, audio_dic
import os
import time
from threading import Thread
import sys
import librosa 
from audio_functions import envelope, Config
from python_speech_features import mfcc, logfbank
from audio_dic import audio_dic

consolidate = []
def predict_image():

    global consolidate
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
    predictions_max = np.argmax(predictions, axis=1)
    # predictions = 1
    # print("image ko index", predictions_max[0])
    # os.remove(image_path)

    animal = image_dic.image_dic[predictions_max[0]]


    consolidate.append([animal, predictions[0][predictions_max[0]]])
    # print("consolidate after image prediction",consolidate)


def predict_audio():
    print('Predicting audio...')

    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'animalAudio(3).h5')
    model = load_model(model_path)

    # audio_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audio_captured', 'audio.wav')

    # audio_path = "E://Shit stuffs//deerhack_//audio_captured//audio.wav"
    audio_path = "E://Shit stuffs//deerhack_//audio_samples//tiger//52.wav"
    signal,rate = librosa.load(audio_path, sr=12000)
    mask = envelope(signal, rate, 0.0005)

    conf = Config()

    signal = signal[mask]
    # print("signal_shape",signal.shape)
    rand_index = np.random.randint(0, signal.shape[0]-conf.step)
    signal = signal[rand_index:rand_index+conf.step]
    
    X_sample = mfcc(signal, rate, numcep = conf.nfeat, nfilt = conf.nfilt, nfft = 512).T
    _min = np.amin(X_sample)
    _max = np.amax(X_sample)

    sample = (X_sample - _min)/(_max - _min)

    sample = sample.reshape(1, sample.shape[0], sample.shape[1], 1)
    y_hat = model.predict(sample)
    y_pred = np.argmax(y_hat, axis=1)

    # print("index of max prob audio", y_pred)

    animal = audio_dic[y_pred[0]]

    #append consolidate with the list [animal, confidence level]
    consolidate.append([animal, (y_hat[0][y_pred][0])])
    # print("consolidate after audio processing", consolidate)

def consolidate_func():
    #find value at index 1 of the two lists inside the list and return the value of index 0 of the list with the higher value
    conf1 = consolidate[0][1]
    conf2 = consolidate[1][1]
    if conf1 > conf2:
        animal = consolidate[0][0]
    else:
        animal = consolidate[1][0]
    print(animal)

    # print("consolidate after consolidation", consolidate)
    #send sms
    send_sms.main(animal)


def start_threads():
    # Start the threads
    image_thread = Thread(target=predict_image)
    audio_thread = Thread(target=predict_audio)
    image_thread.start()
    audio_thread.start()

    # Wait for the threads to finish
    image_thread.join()
    audio_thread.join()

    consolidate_func()


def main():
    print("Starting predict threads")
    start_threads()
    consolidate.clear()
    count = 0
    while count < 2:
        input.main()
        count += 1


if __name__ == '__main__':
    main()
