#This script allows the user to click on the corners of the court in a video frame. 
# The points are saved to a JSON file.
# User is prompted to click in the following order: top left, top right, bottom right, bottom left. 
# The points are displayed on the image as they are clicked. 
# Once all four points are selected, the final list of points is saved to a JSON file.

import cv2 #Open CV library for image processing
import json

points = []

def save_coordinates():
    court_points = {
        "top_left": points[0],
        "top_right": points[1],
        "bottom_right": points[2],
        "bottom_left": points[3]
    }

    with open("court_coordinates.json", "w") as file:
        json.dump(court_points, file, indent=4)

    print("\nSaved coordinates:")
    print(json.dumps(court_points, indent=4))


def click_event(event, x, y, flags, param):
    global img

    if event == cv2.EVENT_LBUTTONDOWN:

        points.append((x, y))

        print(f"Point {len(points)}: ({x}, {y})")

        cv2.circle(img, (x, y), 8, (0, 0, 255), -1)

        cv2.putText(
            img,
            str(len(points)),
            (x+10, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        cv2.imshow("Court", img)

        if len(points) == 4:
            print("\nDone!")

            save_coordinates()


img = cv2.imread("frame.jpg")


cv2.namedWindow("Court", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Court", 1800, 1000)

cv2.imshow("Court", img)

cv2.setMouseCallback("Court", click_event)


print("Click:")
print("1. Top Left")
print("2. Top Right")
print("3. Bottom Right")
print("4. Bottom Left")


cv2.waitKey(0)
cv2.destroyAllWindows()


print("\nFinal Points:")
print(points)