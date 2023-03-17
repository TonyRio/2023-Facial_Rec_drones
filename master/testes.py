#Inicio dos testes
import cv2
import numpy as np

# Carrega o modelo YOLO
net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")

# Define as classes que o modelo pode identificar
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Configura a webcam
cap = cv2.VideoCapture(0)

while True:
    # Captura um quadro da webcam
    ret, frame = cap.read()

    # Cria um blob de imagem para o modelo YOLO
    blob = cv2.dnn.blobFromImage(frame, 1 / 255, (416, 416), (0, 0, 0), True, crop=False)

    # Passa o blob de imagem para o modelo YOLO
    net.setInput(blob)

    # Obtém as detecções
    outs = net.forward(net.getUnconnectedOutLayersNames())

    # Processa as detecções
    for detection in outs:
        for obj in detection:
            # Obtém as informações da classe e confiança da detecção
            scores = obj[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            # Verifica se a detecção tem uma confiança suficientemente alta
            if confidence > 0.5:
                # Obtém as coordenadas da detecção
                center_x = int(obj[0] * frame.shape[1])
                center_y = int(obj[1] * frame.shape[0])
                width = int(obj[2] * frame.shape[1])
                height = int(obj[3] * frame.shape[0])

                # Calcula as coordenadas do canto superior esquerdo
                x = int(center_x - width / 2)
                y = int(center_y - height / 2)

                # Desenha o retângulo da detecção e o texto da classe
                cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
                cv2.putText(frame, classes[class_id], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Mostra a imagem com as detecções
    cv2.imshow("Webcam", frame)

    # Aguarda a tecla 'q' para sair
    if cv2.waitKey(1) == ord('q'):
        break

# Libera a webcam e fecha a janela
cap.release()
cv2.destroyAllWindows()
