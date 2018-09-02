import cv2
import sqlite3
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('Classifiers/face.xml')

def insertorUpdate(Id,Name):
    conn=sqlite3.connect("faceid.db")
    cmd="SELECT * From People WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE PEOPLE SET Name='"+str(Name)+"'WHERE ID="+str(Id)
    else:
        cmd="INSERT INTO People(ID,Name) Values("+str(Id)+",'"+str(Name)+"')"
    conn.execute(cmd)
    conn.commit()
    conn.close()

def userdata():
        id=raw_input("enter your id")
        name=raw_input('enter your name')
        insertorUpdate(id,name)
        sampleNum=0
        while True:
              ret, im =cam.read()
              gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
              faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
              for(x,y,w,h) in faces:
                  sampleNum=sampleNum+1
                  cv2.imwrite("DataSet/user."+id+'.'+str(sampleNum) +".jpg",gray[y:y+h,x:x+h])
                  cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
              cv2.imshow('im',im)
              if cv2.waitKey(30)&0xFF==ord('q'):
                  break
              if sampleNum>20:
                   cam.release()
                   cv2.destroyAllWindows()
                   break
userdata()                

