import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)

while True:

    try:
        check, cameraFeedImg = cap.read()
        
        cameraFeedImg = cv2.flip(cameraFeedImg, 1)

        handsDetector = detector.findHands(cameraFeedImg, flipType=False)
        hands = handsDetector[0]
        cameraFeedImg = handsDetector[1]

        if hands:
            hand1 = hands[0]
            lmList1 = hand1["lmList"]  
            handType1 = hand1["type"]  
            fingers1 = detector.fingersUp(hand1)

        
            # Check if handType1 is "Left"
            
                 # Convert the color image to grayscale image
                 
            # Check if handType1 is "Right"
            
                # Convert to oil paint image
                
            
           

            
            # Check if handType2 is "Left"
            
                 # Convert the color image to grayscale image
                 
            # Check if handType2 is "Right"
            
                # Convert to oil paint image
                

    except Exception as e:
        print(e)

    cv2.imshow("Image", cameraFeedImg)
    cv2.waitKey(1)