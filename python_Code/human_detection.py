

import cv2

# ESP32-CAM Stream URL
ESP32_CAM_URL = "http://192.168.4.1:81/stream"

# Load Haar Cascade Classifier
human_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml"
)

# Open Video Stream
cap = cv2.VideoCapture(ESP32_CAM_URL)

if not cap.isOpened():
    print("Error: Unable to connect to ESP32-CAM.")
    exit()

print("Connected to ESP32-CAM.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to receive frame.")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect humans
    humans = human_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(60, 60)
    )

    # Draw detections
    if len(humans) > 0:
        label = "HUMAN"
        color = (0, 255, 0)

        for (x, y, w, h) in humans:
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
    else:
        label = "NON-HUMAN"
        color = (0, 0, 255)

    # Display result
    cv2.putText(
        frame,
        label,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        2
    )

    cv2.imshow("AI Smart Glasses - Human Detection", frame)

    # Press Q to Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
