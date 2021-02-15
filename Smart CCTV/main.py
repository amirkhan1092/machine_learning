import cv2
# init camera
cam = cv2.VideoCapture(0)

while cam.isOpened():
    ret, image = cam.read()
    cv2.imshow('Khan Camera', image)

    if cv2.waitKey(10) == ord('q'):  # wait for 10ms for wait-key
        break

cv2.destroyAllWindows()



