import tkinter as tk
import cv2
from PIL import Image, ImageTk

# Set up the window
root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')

# Set up the video capture
cap = cv2.VideoCapture(0)

# Define the function for updating the video feed
def update_video_feed():
    # Capture a frame from the video feed
    _, frame = cap.read()

    # Convert the frame to RGB format
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Resize the frame to fit in the window
    height, width, _ = frame.shape
    aspect_ratio = width / height
    new_width = int(root.winfo_height() * aspect_ratio)
    new_height = root.winfo_height()
    frame = cv2.resize(frame, (new_width, new_height))

    # Convert the frame to an ImageTk object and display it in the window
    img = ImageTk.PhotoImage(image=Image.fromarray(frame))
    video_label.configure(image=img)
    video_label.image = img

    # Schedule the next update of the video feed
    root.after(10, update_video_feed)

# Set up the video label
video_label = tk.Label(root, background='black')
video_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Set up the label beneath the video
label_text = tk.StringVar()
label_text.set("Live Video Feed")
label = tk.Label(root, textvariable=label_text, background='black', foreground='white', font=('Arial', 24))
label.pack(side=tk.BOTTOM, pady=20)

# Set up the three squares on the right side
square1 = tk.Canvas(root, width=50, height=50, background='red')
square1.pack(side=tk.RIGHT, padx=10)
square2 = tk.Canvas(root, width=50, height=50, background='green')
square2.pack(side=tk.RIGHT, padx=10)
square3 = tk.Canvas(root, width=50, height=50, background='blue')
square3.pack(side=tk.RIGHT, padx=10)

# Start the video feed
update_video_feed()

# Run the GUI
root.mainloop()
