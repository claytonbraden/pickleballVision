import cv2
from ultralytics import YOLO


# Load YOLO model
model = YOLO("yolov8n.pt")


# Open video
# Create stream of frames from video
video = cv2.VideoCapture("../videofile/video.mp4")
video.set(cv2.CAP_PROP_POS_MSEC, 3000)  # Set to 3 seconds

#Go through all frames.
while True:

    ret, frame = video.read()

    if not ret:
        break


    # Run detection
    results = model.track(
    frame,
    persist=True,
    tracker="bytetrack.yaml", #use bytre
    imgsz=1280, #reduces image size we search for ball
    conf=0.1
)


    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])

            print(model.names[cls], conf)

            
            x1, y1, x2, y2 = box.xyxy[0].tolist()

            # PERSON
            if cls == 0:
                label = "person"

            # BALL
            elif cls == 32:
                label = "ball"

            else:
                continue

            # draw box
            cv2.rectangle(
                frame,
                (int(x1), int(y1)),
                (int(x2), int(y2)),
                (0,255,0),
                2
            )

            cv2.putText(
                frame,
                f"{label} {conf:.2f}",
                (int(x1), int(y1)-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,255,0),
                2
            )


    cv2.imshow(
        "Players",
        frame
    )


    if cv2.waitKey(1) == ord('q'):
        break


video.release()
cv2.destroyAllWindows()