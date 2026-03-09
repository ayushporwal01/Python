import cv2

#Read image
img = cv2.imread("cat.jpg")

#Resize image
resized = cv2.resize(img, (420, 300))
