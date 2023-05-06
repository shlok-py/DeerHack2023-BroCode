import os 
import cv2
from utils.cap import cap
import time 
import predict
from utils import send_sms
from image_dic import image_dic
import time


def capture_image():
    time.sleep(5)
    image_dir = 'images_captured'
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    print('Capturing image...')

    ret, frame = cap.read()
    filename = os.path.join(image_dir, f"image.jpg")
    cv2.imwrite(filename, frame)
    print("Image captured")



    

