import threading
import window
from utils import input

# Create a thread for running the main function from window.py
window_thread = threading.Thread(target=window.main)

# Create a thread for running the main function from main.py
main_thread = threading.Thread(target=input.main)

# Start both threads
window_thread.start()
main_thread.start()

# Wait for both threads to finish
window_thread.join()
main_thread.join()
