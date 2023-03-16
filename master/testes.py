import cv2
from matplotlib import pyplot

# carrega o classificador haar cascade pré-treinado para detecção de faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# abre a webcam
cap = cv2.VideoCapture(0)

while True:
    # lê o frame da webcam
    ret, frame = cap.read()

    # converte o frame para escala de cinza para melhor desempenho
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detecta as faces no frame usando o classificador haar cascade
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # desenha um retângulo verde em cada face detectada
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # exibe o frame com as faces detectadas
    #cv2.imshow('Video', frame)
    pyplot.imshow('Video', frame)
    # espera por uma tecla para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# libera os recursos utilizados
cap.release()
cv2.destroyAllWindows()
