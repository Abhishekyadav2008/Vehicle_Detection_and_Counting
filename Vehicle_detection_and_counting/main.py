import cv2
import numpy as np

# Open webcam feed (0 = default camera)
video_path = "C:/Users/Abhishek/Desktop/Vehicle_detection_and_counting/video.mp4"
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

min_width_react = 80
min_height_react = 80
count_line_position = 550

algo = cv2.createBackgroundSubtractorMOG2()

def center_handle(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

detect = []
offset = 6
counter = 0

while True:
    ret, frame1 = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    frame1 = cv2.resize(frame1, (1020, 720))

    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)

    img_sub = algo.apply(blur)
    dilated = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilated = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
    dilated = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame1, (25, count_line_position), (1200, count_line_position), (255, 127, 0), 3)

    for (i, c) in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(c)
        is_valid = (w >= min_width_react) and (h >= min_height_react)
        if not is_valid:
            continue

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

        center = center_handle(x, y, w, h)
        detect.append(center)
        cv2.circle(frame1, center, 4, (0, 0, 255), -1)

        for (cx, cy) in detect:
            if (count_line_position - offset) < cy < (count_line_position + offset):
                counter += 1
                cv2.line(frame1, (25, count_line_position), (1200, count_line_position), (0, 127, 255), 3)
                detect.remove((cx, cy))
                print("Vehicle Counter:", counter)

    cv2.rectangle(frame1, (90, 60), (700, 120), (255, 255, 255), -1)
    text = f"VEHICLE COUNTER: {counter}"
    cv2.putText(frame1, text, (100, 110), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)

    cv2.imshow("Vehicle Detection from Webcam", frame1)

    if cv2.waitKey(30) == 13:  # Press ENTER to stop
        break

cap.release()
cv2.destroyAllWindows()
