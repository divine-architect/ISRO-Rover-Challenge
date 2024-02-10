import cv2
import numpy as np


image = cv2.imread('crater_final_2.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


blurred = cv2.GaussianBlur(gray, (5, 5), 0)


circles = cv2.HoughCircles(
    blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=100, param2=30, minRadius=10, maxRadius=1000000
)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:

        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)


        cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)

        diameter_pixels = i[2] * 2
        print(f"Diameter: {diameter_pixels} pixels")

cv2.imwrite('output_image_with_circles.jpg', image)


cv2.imshow('Crater Measurement', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
