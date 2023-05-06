from keras.models import load_model
import numpy as np
from tensorflow.keras.utils import img_to_array, load_img
from image_dic import image_dic
import os
import time
from threading import Thread
import sys
import librosa 
from audio_functions import envelope, Config
from python_speech_features import mfcc, logfbank
from audio_dic import audio_dic




def predict_audio():
    print('Predicting audio...')
    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'animalAudio.h5')
    model = load_model(model_path)

    # audio_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audio_captured', 'audio.wav')

    audio_path = "E://Shit stuffs//deerhack_//audio_samples//wolf//58.wav"
    signal,rate = librosa.load(audio_path, sr=12000)
    mask = envelope(signal, rate, 0.005)

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

    print("index of max prob audio", y_pred)

    animal = audio_dic[y_pred[0]]
    print(f"animal: {animal}")
    #append consolidate with the list [animal, confidence level]

predict_audio()