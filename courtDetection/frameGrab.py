import cv2

video = cv2.VideoCapture("../videofile/video.mp4")

video.set(cv2.CAP_PROP_POS_MSEC, 3000) #set the position of the video to 3 seconds

success, frame = video.read()

cv2.imwrite("frame.jpg", frame)

video.release()