import dlib
import cv2
import numpy as np


capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = capture.read()

    faceDetection = dlib.get_frontal_face_detector()
    detectors = faceDetection(frame, 1)
    for i, d in enumerate(detectors):
        cropFaceDetection = frame[d.top():d.bottom(), d.left():d.right()]
        cv2.rectangle(frame, (d.left(), d.top()), (d.right(), d.bottom()), (0, 255, 0), 1)
    cv2.imshow("VideoFrame", frame)

    if cv2.waitKey(1) > 0: break

capture.release()
cv2.destroyAllWindows()


