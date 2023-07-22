import cv2

#read image
plane = r'C:\Users\Farhan\Pictures\pexels-pixabay-46148.jpg'
img = cv2.imread(plane)

if img is None:
    print('Could not open or find the image:', plane)
    exit(0)
print('type',type(img))
print('shape',img.shape)

img_200 = cv2.resize(img,(200, 150))

img_25pct = cv2.resize(img, (0,0), fx=0.25, fy=0.25)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_edge = cv2.Canny(img, 100, 200)

cv2.imshow('image gray', img_gray)
cv2.imshow('image rgb', img_rgb)
cv2.imshow('image',img)
cv2.imshow('image edge', img_edge)

cv2.waitKey(0)
