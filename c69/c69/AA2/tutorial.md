Add Filters
============




In this activity, you will learn to add oil paint, grayscale filter on the raised hand.






<img src= "https://media.slid.es/uploads/1525749/images/10511361/AA2.gif" width = "480" height = "320">




Follow the given steps to complete this activity:
1. Read the info on the hands




* Open file main.py.




* Check if `handType1` is `Left` using an if condition.


    `if handType1 == "Left":`


* Convert the color image to grayscale image.


    `cameraFeedImg = cv2.cvtColor(
        cameraFeedImg, cv2.COLOR_BGR2GRAY)`


* Check if `handType1` is `Right`.


    `if handType1 == "Right":`


* Convert to oil paint image.


    `cameraFeedImg = cv2.xphoto.oilPainting(
        cameraFeedImg, size=7, dynRatio=1)`


* Check if `handType2` is `Left`.


    `if handType2 == "Left":`


* Convert the color image to grayscale image.


    `cameraFeedImg = cv2.cvtColor(
            cameraFeedImg, cv2.COLOR_BGR2GRAY)`


* Check if `handType2` is `Right`.


    `if handType2 == "Right":`


* Convert to oil paint image.


    `cameraFeedImg = cv2.xphoto.oilPainting(
            cameraFeedImg, size=7, dynRatio=1)`
           
* Save and run the code to check the output.
