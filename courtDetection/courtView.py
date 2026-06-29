#This code is used to create a visual representation of a pickleball court using OpenCV. 
# It defines court dimensions, draws the court lines (including the border, center line, net, and kitchen lines), and labels the two teams. 
# Finally, it displays the simulated court in a window.

import cv2
import numpy as np

# Court dimensions (pixels for visualization)
WIDTH = 600
HEIGHT = 1200

# Create blank image
court = np.ones((HEIGHT, WIDTH, 3), dtype=np.uint8) * 255


# Court border
cv2.rectangle(
    court,
    (50, 50),
    (WIDTH-50, HEIGHT-50),
    (0, 0, 0),
    3
)


# Center line
cv2.line(
    court,
    (WIDTH//2, 50),
    (WIDTH//2, HEIGHT-50),
    (0,0,0),
    2
)


# Net
cv2.line(
    court,
    (50, HEIGHT//2),
    (WIDTH-50, HEIGHT//2),
    (0,0,255),
    5
)


# Kitchen lines (7 ft from net)
kitchen_offset = int(HEIGHT * (7/44)/2)

cv2.line(
    court,
    (50, HEIGHT//2 - kitchen_offset),
    (WIDTH-50, HEIGHT//2 - kitchen_offset),
    (0,0,0),
    2
)

cv2.line(
    court,
    (50, HEIGHT//2 + kitchen_offset),
    (WIDTH-50, HEIGHT//2 + kitchen_offset),
    (0,0,0),
    2
)


# Labels
cv2.putText(
    court,
    "Team A",
    (250,100),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0,0,0),
    2
)

cv2.putText(
    court,
    "Team B",
    (250,1150),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0,0,0),
    2
)


# Show window
cv2.namedWindow("Simulated Court", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Simulated Court", 500, 900)

cv2.imshow("Simulated Court", court)

cv2.waitKey(0)
cv2.destroyAllWindows()