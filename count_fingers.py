import cv2
import pyautogui
import mediapipe as mp
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

f_num =[(8,6),(12,10),(16,14),(20,18)]
webcam = cv2.VideoCapture(0)
while webcam.isOpened():
    r,f = webcam.read()
    height,width,x=f.shape
    f = cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
    result = hands.process(f)
    f = cv2.cvtColor(f,cv2.COLOR_RGB2BGR)
    if result.multi_hand_landmarks:
        lmlist=[]
        for handLms in result.multi_hand_landmarks:
            # mpDraw.draw_landmarks(f,handLms,mpHands.HAND_CONNECTIONS)
            
            for id , landmark in enumerate(handLms.landmark):
                
                x = int(landmark.x*width)
                y = int (landmark.y * height) 
                lmlist.append((x,y))
            upcount =0
            if lmlist[4][0] > lmlist[3][0]:
                upcount+=1
            for x in f_num:
                if lmlist[x[0]][1]<lmlist[x[1]][1]:
                    upcount+=1
            cv2.putText(f,"Number of up fingers : "+str(upcount),(50,50),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255))
            
                    
                       
    if r== True:
        cv2.flip(f,1)
        cv2.imshow("gesture volume control",f)
        if cv2.waitKey(25) & 0xff == ord("q"):
            break
    else:
        break
webcam.release()
cv2.destroyAllWindows()