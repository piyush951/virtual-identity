import cv2,os
import numpy as np
from PIL import Image
import pickle
import sqlite3

recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load('trainner/trainner.yml')
cascadePath = "Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path='Dataset'

def getProfile(id):
    conn=sqlite3.connect("faceid.db")
    cmd="SELECT * FROM People WHERE ID="+str(id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile


def detect():
        cam = cv2.VideoCapture(0)
        font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, .5, 0, 2, 1)
        while True:
            ret,im=cam.read()
            gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2 ,minNeighbors=5 ,minSize=(100,100),flags=cv2.CASCADE_SCALE_IMAGE)
    
            for(x,y,w,h) in faces:
        
                nbr_predicted,conf = recognizer.predict(gray[y:y+h,x:x+w])
                cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
                profile=getProfile(nbr_predicted)
                if(profile!=None): 
                    cv2.cv.PutText(cv2.cv.fromarray(im),str(profile[1]),(x,y+h+30),font,255)
                    cv2.cv.PutText(cv2.cv.fromarray(im),str(profile[2]),(x,y+h+60),font,255)
                    cv2.cv.PutText(cv2.cv.fromarray(im),str(profile[3]),(x,y+h+90),font,255)
                    #cv2.cv.PutText(cv2.cv.fromarray(im),str(profile[4]),(x,y+h+120),font,255)
                    print(str(profile[1]))
                    print(str(profile[3]))
                    print(str(profile[2]))
                elif profile==None:
                    cv2.cv.PutText(cv2.cv.fromarray(im),"stranger",(x,y+h+30),font,255)
                    
            if cv2.waitKey(30)&0xFF==ord('q'):
                cam.release()
                cv2.destroyAllWindows()
                break
                
            cv2.imshow('im',im)
            cv2.waitKey(10)
detect() 
  
