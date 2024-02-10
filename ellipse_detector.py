import cv2
import numpy as np

def detect_and_draw_ellipses(image_path):

    original_image = cv2.imread(image_path)


    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
#gblur

    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)


    edges = cv2.Canny(blurred_image, 50, 150)

    kernel = np.ones((5, 5), np.uint8)
    closed_edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)


    contours, _ = cv2.findContours(closed_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    ellipses_image = original_image.copy()

    for contour in contours:
        if len(contour) >= 5:

            ellipse = cv2.fitEllipse(contour)


            cv2.ellipse(ellipses_image, ellipse, (0, 255, 0), 2)

    cv2.imshow('Ellipses Image', ellipses_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Provide the path to your input image
    image_path = "crater_final_2.jpg"

    detect_and_draw_ellipses(image_path)
