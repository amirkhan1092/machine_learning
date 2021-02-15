import cv2
# init camera
cam = cv2.VideoCapture(0)

while cam.isOpened():
    ret, image1 = cam.read()
    ret, image2 = cam.read()

    diff = cv2.absdiff(image1, image2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Khan Camera', gray)
    if cv2.waitKey(10) == ord('q'):  # wait for 10ms for wait-key
        break

cv2.destroyAllWindows()



