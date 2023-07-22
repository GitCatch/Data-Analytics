import cv2

cascase_path = 'haarcascade_fullbodyy.xml'
classifier = cv2.CascadeClassifier(cascase_path)
path = r'C:\Users\Farhan\Pictures\pexels-koolshooters-7346135 (2160p).mp4'
video = cv2.VideoCapture(path)


while True:
    status, image = video.read()
    if not status:
        print('could not read frame')
        break

    image = cv2.resize(image,(0,0), fx=0.4, fy=0.4)
    detection = classifier.detectMultiScale(image,
                                            scaleFactor=1,
                                            minNeighbors=3,
                                            minSize=(20,30))
    if len(detection) > 0:
        print(f'Found {len(detection)} people')
        for(x, y, w, h) in detection:
            cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2 )
    cv2.imshow('video', image)
    if cv2.waitKey(1) == ord('q'): #if a key is pressed then break
        break
video.release() #release video capture object
cv2.destroyAllWindows()#close all windows