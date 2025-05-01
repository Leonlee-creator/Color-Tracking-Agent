import cv2
import numpy as np

# Start video capture (0 = default webcam)
cap = cv2.VideoCapture(0)

# Black color range (for obstacles)
lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 30])


# Define color range for detection (let's use red for now)
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Find contours in the red mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    direction = "Searching..."

    if contours:
        # Get the largest red object
        largest = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest)
        cx = x + w // 2

        # Draw rectangle and center point
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.circle(frame, (cx, y + h // 2), 5, (255, 255, 255), -1)

        # Decide direction based on object position
        if cx < 200:
            direction = "MOVE LEFT"
        elif cx > 440:
            direction = "MOVE RIGHT"
        else:
            direction = "MOVE FORWARD"

    # Show direction text
    cv2.putText(frame, direction, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow("Original", frame)
    cv2.imshow("Red Mask", mask)

    # Detect obstacles (black areas)
    black_mask = cv2.inRange(hsv, lower_black, upper_black)
    black_contours, _ = cv2.findContours(black_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # If obstacle detected, override direction
    if black_contours:
        largest_obstacle = max(black_contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_obstacle)
        if area > 500:
            direction = "STOP - Obstacle!"

    cv2.imshow("Obstacle Mask", black_mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
