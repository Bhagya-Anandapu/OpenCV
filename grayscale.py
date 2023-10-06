import cv2
img=cv2.imread("dehya.jpg_large")
#imread = read an image
cv2.imshow("original",img)
#imshow = to show image with a name
cv2.waitKey(0)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Cvt.COLORBGR2GRAY = convert color from bgr to gray
cv2.imshow("gray",gray)
cv2.imwrite("mygf.jpg",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
