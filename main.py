import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # === COLOR DETECTION ===
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    lower_green = np.array([36, 100, 100])
    upper_green = np.array([86, 255, 255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    lower_blue = np.array([94, 80, 2])
    upper_blue = np.array([126, 255, 255])
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    red_area = cv2.countNonZero(mask_red)
    green_area = cv2.countNonZero(mask_green)
    blue_area = cv2.countNonZero(mask_blue)

    # === OBSTACLE DETECTION ===
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    height, width = edges.shape
    roi = edges[int(height*0.6):height, int(width*0.3):int(width*0.7)]
    obstacle_edges = cv2.countNonZero(roi)

    # Visual Debug: Show ROI
    cv2.rectangle(frame, (int(width*0.3), int(height*0.6)), (int(width*0.7), height), (255, 255, 0), 2)

    # === DECISION LOGIC ===
    if red_area > 2000:
        action = "STOP"
    elif obstacle_edges > 500:
        action = "AVOID OBSTACLE"
    elif green_area > 2000:
        action = "MOVE FORWARD"
    elif blue_area > 2000:
        action = "TURN"
    else:
        action = "SEARCHING..."

    # Show action
    cv2.putText(frame, action, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (255, 255, 255), 2)

    cv2.imshow("AI Agent View", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
