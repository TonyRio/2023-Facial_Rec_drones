import cv2
import datetime

# carrega o classificador haar cascade pré-treinado para detecção de faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# abre a webcam
cap = cv2.VideoCapture(0)

# loop infinito
while True:
    # lê o frame da webcam
    ret, frame = cap.read()

    # converte o frame para escala de cinza para melhor desempenho
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detecta as faces no frame usando o classificador haar cascade
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # loop sobre cada face detectada
    for (x, y, w, h) in faces:
        # desenha um retângulo verde em cada face detectada
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # reconhece o rosto e obtém o nome
        # você precisa implementar essa parte com o reconhecimento facial
        name = "sem Identidade :"

        # obtém a hora atual do sistema
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        # desenha o nome e a hora atual na tela
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.putText(frame, timestamp, (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # exibe o frame com as faces detectadas
    cv2.imshow('Video', frame)

    # espera por uma tecla para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# libera os recursos utilizados
cap.release()
cv2.destroyAllWindows()
