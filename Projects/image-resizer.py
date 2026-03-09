import cv2

#Read image
img = cv2.imread("./Images/cat.jpg")

#Resize image
resized = cv2.resize(img, (420, 300))

#Show resized image
cv2.imshow("Resized Image", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Save resized image
saved = cv2.imwrite("D:\Ayush\Python\Images\resized-cat.jpg", resized)