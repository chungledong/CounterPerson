import cv2

drawing=False
point1=()
point2=()
def mouse_drawing(event,x,y,flags,params):
    global point1,point2,drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        if drawing is False:
            drawing = True
            point1 = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            point2 = (x,y)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

cap = cv2.VideoCapture('video.avi')
cv2.namedWindow('Count person')
cv2.setMouseCallback('Count person',mouse_drawing)
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(1080,720))
    person_cascade=cv2.CascadeClassifier('haarcascade_fullbody.xml')
    if point1 and point2:
        r = cv2.rectangle(frame,point1,point2, (100,50,200),5)
        frame_eys = frame[point1[1]:point2[1],point1[0]:point2[0]]
        if drawing is False:
            try:
                grayscale=cv2.cvtColor(frame_eys,cv2.COLOR_BGR2GRAY)
                person=person_cascade.detectMultiScale(grayscale)
                for (x,y,w,h) in person:
                    cv2.rectangle(frame_eys,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.putText(frame_eys,'Count person: '+str(person.shape[0]),(10, frame_eys.shape[0]-25), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0),1)
            except:
                print("Error!")
    cv2.imshow('Count person',frame)
    if cv2.waitKey(25) & 0xff==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

