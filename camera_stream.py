import cv2

# Open a connection to the camera
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)


# Set resolution (match it to the sensor’s capability)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_FPS, 30)  # Set frame rate

# Stream the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture video")
        break

    # Display the frame on the screen
    cv2.imshow("Camera Stream", frame)

    # Press 'q' to quit the stream
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
