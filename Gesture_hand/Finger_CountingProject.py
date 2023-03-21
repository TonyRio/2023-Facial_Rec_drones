import cv2
import time
import os

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4, hCam)

folderPath = "FingerImages"
myList = os.listdir(folderPath)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
#    print(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))

while True:

    success, img = cap.read()

    img[0:200, 0:200] = overlayList[0]
    cv2.imshow("Imagem", img)
    cv2.waitKey(1)
