#This code is used to map the coordinates of a tennis court from an image to real-world coordinates. 
# It reads the court coordinates from a JSON file, computes the perspective transform matrix, and then
# applies the perspective transform to a given pixel coordinate (in this case, the position of the ball) to get its real-world coordinates on the court.


import cv2
import json
import numpy as np


with open("court_coordinates.json") as f:
    court = json.load(f)

#get the image points from the JSON file and convert them to a numpy array
image_points = np.float32([
    court["top_left"],
    court["top_right"],
    court["bottom_right"],
    court["bottom_left"]
])

#create the corresponding court points in real-world coordinates (in feet)
court_points = np.float32([
    [0,0],
    [20,0],
    [20,44],
    [0,44]
])

#compute the perspective transform matrix
#this matrix will be used to transform pixel coordinates to real-world coordinates on the court
matrix = cv2.getPerspectiveTransform(
    image_points,
    court_points
)

#example pixel coordinate of the ball in the image (this would be obtained from ball detection in a real application)
ball_pixel = np.float32([
    [[900,450]]
])


ball_court = cv2.perspectiveTransform(
    ball_pixel,
    matrix
)


print(ball_court)