import cv2
import numpy as nm

def create_pencil_stetch(image_file):
    img = cv2.imread(image_file)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_img= cv2.bitwise_not(gray_img)
    blurred_img = cv2.GaussianBlur(inverted_img, (21, 21), sigmaX=0, sigmaY=0)
    pencil_sketch = cv2.divide(gray_img, 255 - blurred_img, scale=256)
    cv2.imshow("Pencil Sketch", pencil_sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

create_pencil_stetch("photo_2024-06-13 10.47.46 PM.jpeg")