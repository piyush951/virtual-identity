#import dataset
#import detector
while True:
     print("1.add user")
     print("2. check user ")
     print("3. exit ")
     n=int(input("enter ur choice"))
     if(n==1):
     #userdata()
          import dataset
     elif(n==2):
    #detect()
          import detector
          detector.detect()
     elif n==3:
         break
     else:
          print("Invalid input")


