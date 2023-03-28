import cv2
import numpy as np
import tensorflow as tf

# Carregar modelo de detecção de objetos treinado
model = tf.keras.models.load_model('modelo_carros.h5')

# Configurações da webcam
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Contador de carros
count = 0

while True:
    # Ler um frame da webcam
    ret, frame = camera.read()

    # Pré-processar o frame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (224, 224))
    frame = frame / 255.0
    frame = np.expand_dims(frame, axis=0)

    # Fazer a detecção de objetos no frame
    pred = model.predict(frame)[0]
    label = np.argmax(pred)
    confidence = pred[label]

    # Verificar se o objeto detectado é um carro
    if label == 0 and confidence > 0.5:
        # Incrementar o contador de carros
        count += 1

        # Salvar o frame como uma imagem no dataset
        cv2.imwrite(f'carro_{count}.jpg', frame)

    # Exibir o número de carros detectados no frame
    cv2.putText(frame, f"Carros: {count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

    # Exibir o frame na tela
    cv2.imshow("Detector de Carros", frame)

    # Esperar pela tecla "q" para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Encerrar a câmera e fechar a janela
camera.release()
cv2.destroyAllWindows()
