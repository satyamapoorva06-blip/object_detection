import cv2

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if success:
        cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



#### to test the camara  

C:\Users\Lenovo\AppData\Local\Programs\Python\Python314\python.exe d:\ObjectDetectionProject\camera_test.py


# run this on the terminal