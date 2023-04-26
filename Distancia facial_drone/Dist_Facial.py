import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import mediapipe as mp

# Inicialização do objeto para captura da imagem da webcam
cap = cv2.VideoCapture(0)

# Inicialização do classificador Haar Cascade para detecção facial
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicialização do objeto para detecção de mãos com o Mediapipe
mp_hands = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)

# Loop infinito para capturar a imagem da webcam e realizar as operações
while True:
    # Captura da imagem da webcam
    ret, frame = cap.read()

    # Conversão da imagem para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecção de faces na imagem
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Detecção de mãos na imagem com o Mediapipe
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_hands.process(rgb)
    hand_landmarks = None
    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            hand_landmarks = hand_lms

    # Divisão da tela em 8 partes
    height, width = gray.shape
    mid_x = int(width/2)
    mid_y = int(height/2)
    p1 = (0, 0)
    p2 = (width, height)
    p3 = (mid_x, 0)
    p4 = (mid_x, height)
    p5 = (0, mid_y)
    p6 = (width, mid_y)
    p7 = (mid_x, mid_y)
    p8 = (0, 0)
    points = [p1, p2, p3, p4, p5, p6, p7, p8]

    # Desenho do ponto central
    cv2.circle(frame, (mid_x, mid_y), 5, (0, 0, 255), -1)

    # Desenho do quadrado no rosto reconhecido, medida da distância do rosto ao ponto central e indicação se o rosto está a direita ou a esquerda do ponto central
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face_center_x = int(x + w / 2)
        face_center_y = int(y + h / 2)
        cv2.circle(frame, (face_center_x, face_center_y), 5, (0, 255, 0), -1)
        face_center_point = (face_center_x, face_center_y)
        distances = []
        for point in points:
            distance = math.sqrt((point[0] - face_center_x) ** 2 + (point[1] - face_center_y) ** 2)
            distances.append(distance)
            min_distance = min(distances)
            if min_distance < 50:
                cv2.putText(frame, "F", (face_center_x, face_center_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                            cv2.LINE_AA)
            else:
                for i in range(len(points) - 1):
                    if min_distance == distances[i]:
                        if i == 0 or i == 7:
                           cv2.rectangle(frame, (0, 0), (mid_x, mid_y), (0, 0, 255), -1)
                        elif i == 1 or i == 6:
                                cv2.rectangle(frame, (mid_x, mid_y), (width, height), (0, 0, 255), -1)
                        elif i == 2 or i == 3:
                                cv2.rectangle(frame, (mid_x, 0), (width, height), (0, 255, 255), -1)
                        elif i == 4 or i == 5:
                                cv2.rectangle(frame, (0, mid_y), (width, height), (0, 255, 0), -1)






            distances.append(distance)
        min_distance_index = np.argmin(distances)
        min_distance_point = points[min_distance_index]
        cv2.line(frame, (face_center_x, face_center_y), min_distance_point, (0, 255, 255), 2)

    # Exibição da imagem capturada com o quadrado no rosto reconhecido e o ponto no centro da tela
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Finalização da captura da
cap.release()
cv2.destroyAllWindows()