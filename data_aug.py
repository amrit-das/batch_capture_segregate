import cv2
import numpy as np

import argparse

import sys
import os

cap = cv2.VideoCapture(0)
max_cap = 100

filename = sys.argv[1]
delay = int(sys.argv[2])

exist = os.path.exists("/home/amrit/Desktop/Nymble/Dataset/"+"fielname")
print filename," exists ",exist

if not exist:
    try:
        os.mkdir(filename)
    except OSError:
        pass
cnt = 1
while max_cap>=cnt:
    ret,frame = cap.read()
    cv2.imshow("Video",frame)
    cv2.imwrite(filename+"/"+filename+str(cnt)+".png",frame)
    cnt +=1
    if cv2.waitKey(delay) == 27:
        break
cap.release()
cv2.destroyAllWindows()
