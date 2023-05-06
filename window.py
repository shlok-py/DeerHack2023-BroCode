import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
from utils.cap import cap
import time

def main():
    # create a window
    window = tk.Tk()
    window.title("Live Feed")

    # create a label to display the live feed
    feed_label = tk.Label(window)
    feed_label.pack()

    # create a label for audio recording
    audio_label = tk.Label(window, text="Audio Recording", font=("Arial", 16))
    audio_label.pack(pady=10)

    # start a timer to exit the program after 30 seconds

    def update_feed():
        # read a frame from the video stream
        ret, frame = cap.read()

        if ret:
            # convert the frame to an image and display it in the label
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = PIL.Image.fromarray(img)
            img = PIL.ImageTk.PhotoImage(img)
            feed_label.imgtk = img
            feed_label.configure(image=img)

        # update the feed every 10 milliseconds
        window.after(10, update_feed)

    # start updating the feed
    update_feed()

    # start the main event loop
    window.mainloop()

    print("Done")
