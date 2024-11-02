import cv2

# Set the camera ID (usually 1 for an external camera)
camera_id = 0

# Open the camera
cap = cv2.VideoCapture(camera_id)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

# Read frames in a loop
while True:
    ret, frame = cap.read()
    print(frame)
    if not ret:
        print("Failed to grab frame")   
        break

    # Display the resulting frame
    cv2.imshow("External Camera Feed", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()
