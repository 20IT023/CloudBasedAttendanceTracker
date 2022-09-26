import requests
import datetime
import time
import cv2


for j in range(0, 1):
    current_time = datetime.datetime.now().strftime("%d-%m-%y  %H-%M-%S ")
    
    print(current_time)
    camera = cv2.VideoCapture(0)
    for i in range(20):
        return_value, image = camera.read()
        if (i == 19):
            cv2.imwrite('G:/Vs code/AI-Powered-Hourly-Attendance-Capturing-System-master/' + current_time + '.jpg', image)
    del (camera)

    time.sleep(20)
