Identify Fingers on Both Hands
==============================


In this activity, you will learn to detect the fingers on both the hands shown in the video feed.


<img src= "https://media.slid.es/uploads/1525749/images/10511362/AA1.png" width = "480" height = "320">


Follow the given steps to complete this activity:
1. Read the info on the hands

* Open file main.py.

* Read the info for `hands[1]` such as `lmlist2`, `handType2`, `fingers2`.


    `hand2 = hands[1]`


    `lmList2 = hand2["lmList"]`


    `handType2 = hand2["type"]`


    `fingers2 = detector.fingersUp(hand2)`



* Set `currentFingersUp` to `""`.


    `currentFingerUp = ""`


* Check which finger is up in `fingers2` and set `currrentFingerUp` accordingly.


    `if fingers2[0] == 0:`


        `currentFingerUp = "Thumb"`


    `elif fingers2[1] == 1:`


        `currentFingerUp = "Index Finger"`


    `elif fingers2[2] == 1:`


        `currentFingerUp = "Middle Finger"`


    `elif fingers2[3] == 1:`


        `currentFingerUp = "Ring Finger"`


    `elif fingers2[4] == 1:`


       `currentFingerUp = "Little Finger"`


    `else:`


        `currentFingerUp = ""`




* Write to the output, the hand and the finger.


    `cv2.putText(cameraFeedImg, handType2 + " : " + currentFingerUp, (375, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)`



* Save and run the code to check the output.
