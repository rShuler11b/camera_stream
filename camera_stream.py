from picamera2 import Picamera2, Preview
import time

# Initialize the camera
picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"size": (1920, 1080)})  # Set resolution as needed
picam2.configure(config)

# Start the camera
picam2.start_preview(Preview.QTGL)
picam2.start()

print("Streaming... Press Ctrl+C to stop.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping the stream.")
finally:
    picam2.stop()
