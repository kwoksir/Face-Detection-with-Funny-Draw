import cv2

CAM_WIDTH = 640
CAM_HEIGHT = 480

cap = cv2.VideoCapture()
cap.open(0, cv2.CAP_DSHOW)
cap.set(3, CAM_WIDTH)
cap.set(4, CAM_HEIGHT)

face_detector = cv2.CascadeClassifier('face.xml')

def fancyDraw(img, bbox, l=30, t=5, rt= 3):
    x, y, w, h = bbox
    x1, y1 = x+w, y+h
    cv2.rectangle(img, (x + 20, y + 20 , w - 40, h - 40), (0,255,0), 2)

    #Top Left x,y
    cv2.line(img, (x,y), (x+l, y), (255,0,255), t)
    cv2.line(img, (x,y), (x, y+l), (255,0,255), t)

    #Top Right x,y
    cv2.line(img, (x1,y), (x1-l, y), (255,0,255), t)
    cv2.line(img, (x1,y), (x1, y+l), (255,0,255), t)

    #Bottom Left x,y
    cv2.line(img, (x,y1), (x+l, y1), (255,0,255), t)
    cv2.line(img, (x,y1), (x, y1-l), (255,0,255), t)

    #Bottom Right x,y
    cv2.line(img, (x1,y1), (x1-l, y1), (255,0,255), t)
    cv2.line(img, (x1,y1), (x1, y1-l), (255,0,255), t)

    return img

while True:
    success, img = cap.read()
    if success:
        faces = face_detector.detectMultiScale(img, scaleFactor=1.2, minNeighbors=5, minSize=(60,60))
    for (x,y,w,h) in faces:
        bbox = (x,y,w,h)
        img = fancyDraw(img,bbox)
        cv2.putText(img,"face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,255), 1)

    cv2.imshow('Frame1',img)
    if cv2.waitKey(1) == ord('q') or cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
cap.release()
