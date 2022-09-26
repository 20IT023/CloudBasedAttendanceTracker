import boto3
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
            cv2.imwrite('G:/Vs code/CloudBasedTracker/' + current_time + '.jpg', image)
    del (camera)

    clients3 = boto3.client('s3', region_name='us-east-1')
    clients3.upload_file("Hourly Class Images/"+current_time+'.jpg', 'add your S3 bucket name', current_time+'.jpg')

    time.sleep(20)
