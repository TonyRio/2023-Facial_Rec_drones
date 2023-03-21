import cv2
import time
import os
import HandTrackingModule as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4, hCam)

folderPath = "FingerImages"
myList = os.listdir(folderPath)
print(myList)

overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
#    print(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))

pTime=0


detector = htm.handDetector(detectionCon=0)



tipIds = [4, 8, 12, 16, 20]
#img = detector.findHands(img)

while True:
# le a imagem e coloca do tamanho e coordenada
    success, img = cap.read()
    img= detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    #print(lmList)

    if len(lmList) != 0:
        fingers = []

# Loop para corrigir o polegar

        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

# Loop para 4 dedos

        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        #print(fingers)

# Contando a quantidade de dedos
            totalFinger = fingers.count(1)
            print(totalFinger)

# Imprimindo as imagens dos dedos

            h, w, c = overlayList[totalFinger-1].shape
            img[0:h, 0:w] = overlayList[totalFinger-1]

            cv2.rectangle(img, (20,480), (170, 700), (0,255,0), cv2.FILLED)
            cv2.putText(img, str(totalFinger), (45, 640), cv2.FONT_HERSHEY_PLAIN, 10,(255,0,0), 25)


# temporiza abertura

    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime

    cv2.putText(img, f"FPS: {int(fps)}", (400,70), cv2.FONT_HERSHEY_COMPLEX, 3, (255,0,0), 3 )
    cv2.imshow("Imagem", img)
    cv2.waitKey(1)
