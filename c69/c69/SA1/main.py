# import required libraries
import cv2


# Capture the camera feed and set the resolution
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
# Loop to display video
while True:
    try:
        # Get a single capture from the camera
        check,cameraFeeding=cap.read()

        cameraFeeding=cv2.flip(cameraFeeding,1)
    # Show the camera feed image
    except Exception as e :
        print(e)


    cv2.imshow("Image", cameraFeeding)
    cv2.waitKey(1)