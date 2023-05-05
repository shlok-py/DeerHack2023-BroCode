from keras.models import load_model
import numpy as np
from tensorflow.keras.utils import img_to_array,load_img
from utils import input, send_sms
import os

image_dic = {0:"deer",1:"elephant",2:"lion",3:"tiger"}

# image_model = load_model('image_model.h5')
# audio_model = load_model('audio_model.h5')


input.main()
input_image= "E:\Shit stuffs\deerhack_\images_captured\image.jpg" 
"""# input_audio = "E:\Shit stuffs\Deerhack\audio_captured\audio.wav"

img = load_img(input_image, target_size=(150, 150))

img_array = img_to_array(img)

input_tensor = np.expand_dims(img_array, axis=0)

predictions = image_model.predict(input_tensor)

predictions = np.argmax(predictions, axis=1)"""

predictions = 1

print(predictions)
msg = "Warning! {} detected!".format(image_dic[predictions])
if predictions != 0:
    send_sms.main(msg)


#delete the image and audio files
os.remove(input_image)
# os.remove(input_audio)
