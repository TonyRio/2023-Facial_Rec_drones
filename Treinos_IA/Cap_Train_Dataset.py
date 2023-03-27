import cv2
import os

# Defina o diretório onde as imagens serão salvas
diretorio_dataset = 'dataset/'

# Crie o diretório do dataset, se ainda não existir
if not os.path.exists(diretorio_dataset):
    os.makedirs(diretorio_dataset)

# Defina o tamanho da imagem do dataset
tamanho_imagem = (224, 224)

# Inicie a captura de vídeo a partir da webcam
cap = cv2.VideoCapture(0)

# Inicie a leitura da captura de vídeo
count = 0
while cap.isOpened():
    # Capturar um frame da webcam
    ret, frame = cap.read()

    if ret:
        # Redimensionar o frame para o tamanho desejado
        frame = cv2.resize(frame, tamanho_imagem)

        # Salvar o frame como uma imagem no diretório do dataset
        nome_imagem = os.path.join(diretorio_dataset, f'frame{count:04}.jpg')
        cv2.imwrite(nome_imagem, frame)

        count += 1

        # Aguarde 1 milissegundo para a próxima captura
        # Pressione a tecla 'q' para sair do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Libere a captura de vídeo
cap.release()

# Feche todas as janelas abertas
cv2.destroyAllWindows()
