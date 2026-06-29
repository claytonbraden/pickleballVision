# pickleballVision
-Video of Ben Johns/Gabe Tardio found in videofile/ folder. Not uploaded to Github to file size constraints.

1. Court mapping done in courtDetection/ folder.
-Here we mapped the pixels of a single frame given the rear camera view.
-After we traing ball detection, it will allow us to track where the ball is
-This will allow us to track coordinates and make decision if given the rear view.

2. Player mapping and detection found in playerDetector folder.

3. Ball detection 
-This part is hard. YOLO has a class that allows for tracking of a sports ball, but it does not get picked up very well as a pickleball is small, yellow, and fast. 
-1000 Frames will be labeled of the pickleball. 

