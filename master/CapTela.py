import cv2
import os

# Defina o diretório de destino para salvar as imagens capturadas
diretorio_destino = "imagens/"

# Crie o diretório, se ele ainda não existir
if not os.path.exists(diretorio_destino):
    os.makedirs(diretorio_destino)

# Inicie a captura de vídeo a partir da webcam
cap = cv2.VideoCapture(0)

# Defina o número de imagens que você deseja capturar
num_imagens = 100

# Loop para capturar as imagens
for i in range(num_imagens):
    # Capturar um quadro da webcam
    ret, frame = cap.read()

    # Mostrar o quadro na janela de visualização
    cv2.imshow('frame', frame)

    # Defina o nome do arquivo de imagem com base no número de sequência
    nome_arquivo = diretorio_destino + "imagem_" + str(i) + ".png"

    # Salvar a imagem no diretório de destino
    cv2.imwrite(nome_arquivo, frame)

    # Aguarde 100 milissegundos para a próxima captura
    cv2.waitKey(1000)

# Libere a captura de vídeo
cap.release()

# Feche todas as janelas abertas
cv2.destroyAllWindows()