import cv2

def take_snapshot():
    vd = cv2.VideoCapture(0)
    result = True

    while(result):
        ret,frame = vd.read()
        cv2.inwrite("newpic.png", frame)
        result = false
    
    vd.release()
    cv2.destroyAllWindows()

take_snapshot()
