import cv2
image = cv2.imread('lunar_c.png', cv2.IMREAD_GRAYSCALE)


edges = cv2.Canny(image, 50, 150)
cv2.imwrite('edges.jpg', edges)

