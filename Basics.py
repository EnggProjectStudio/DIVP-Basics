import cv2
import numpy as np

image = cv2.imread("puppy.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resized_image = cv2.resize(image, (400, 600))

blurred_image = cv2.GaussianBlur(image, (7, 7), 0)

cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray_image)
cv2.imshow("Resized", resized_image)
cv2.imshow("Blurred", blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
