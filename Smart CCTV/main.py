import cv2
# init camera
cam = cv2.VideoCapture(0)

while cam.isOpened():
    ret, image1 = cam.read()
    ret, image2 = cam.read()

    diff = cv2.absdiff(image1, image2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contour, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image1, contour, -1, (0, 255, 0), 2)
    cv2.imshow('Khan Camera', image1)
    if cv2.waitKey(10) == ord('q'):  # wait for 10ms for wait-key
        break

cv2.destroyAllWindows()



