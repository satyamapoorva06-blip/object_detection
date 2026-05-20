import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8s.pt")

# Open webcam using DirectShow
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Check camera
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    success, frame = cap.read()

    if not success:
        print("Failed to grab frame")
        break

    # Object detection
    results = model(frame)

    # Draw results
    annotated_frame = results[0].plot()

    # Show output
    cv2.imshow("Object Detection and Tracking", annotated_frame)

    # Quit with Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()