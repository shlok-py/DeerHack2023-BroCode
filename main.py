from keras.models import load_model
import numpy as np
from tensorflow.keras.utils import img_to_array,load_img
from utils import input
import os
import time
from utils.image_dic import image_dic

def main():
    print("Starting main")
    # image_model = load_model('image_model.h5')
    # audio_model = load_model('audio_model.h5')

    start_time = time.time()
    while (time.time() - start_time) <= 30:
        input.main()
        # input_image = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images_captured', 'image.jpg')
        # input_audio = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audio_captured', 'audio.wav')

        # img = load_img(input_image, target_size=(150, 150))
        # img_array = img_to_array(img)
        # input_tensor = np.expand_dims(img_array, axis=0)

        # predictions = image_model.predict(input_tensor)
        # predictions = np.argmax(predictions, axis=1)
        # predictions = 1
        # print(predictions)
        # msg = "Warning! {} detected!".format(image_dic[predictions])
        # print(msg)
        # if predictions != 0:
        #     send_sms.main(msg)

        #delete the image and audio files
        # os.remove(input_image)
        # os.remove(input_audio)

if __name__ == '__main__':
    main()
