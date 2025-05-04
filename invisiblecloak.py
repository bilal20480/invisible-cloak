import cv2
import numpy as np
import time

# Start the webcam
cap = cv2.VideoCapture(0)
time.sleep(2)

# Capture the background
print("Capturing background. Please move out of the frame...")
for i in range(30):
    ret, background = cap.read()
background = np.flip(background, axis=1)

print("Background captured! Now wear your black cloth.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)

    # Convert the frame from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define mask for black color (tweak values if needed)
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 50])
    mask = cv2.inRange(hsv, lower_black, upper_black)

    # Refine the mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask = cv2.dilate(mask, np.ones((3,3), np.uint8), iterations=1)

    # Invert the mask
    inverse_mask = cv2.bitwise_not(mask)

    # Segment out the non-black parts from the current frame
    res1 = cv2.bitwise_and(frame, frame, mask=inverse_mask)

    # Segment out the black cloth parts from the background
    res2 = cv2.bitwise_and(background, background, mask=mask)

    # Combine both to get final output
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Invisible Cloak - Black Cloth", final_output)

    if cv2.waitKey(1) == 27:  # ESC key to exit
        break

cap.release()
cv2.destroyAllWindows()
