import cv2
obj=cv2.CascadeClassifier('License_plate_recognition.xml')
count=1

def detect(frame,count):
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    objs=obj.detectMultiScale(gray,1.01,5)
    for x,y,w,h in objs:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
        cv2.imshow('video',frame)
        cv2.imwrite("cap/img"+str(count)+".jpg",frame[y:y+h,x:x+w])

"""image = cv2.imread("img.jpg")
cv2.imshow("orignal",image)
detect(image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""
video=cv2.VideoCapture(0)      
while True:
    check,frame=video.read()
    cv2.imshow("video",frame)
    detect(frame,count)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break;
    count=count+1;
video.release();
cv2.destroyAllWindows()

