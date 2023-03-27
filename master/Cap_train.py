import cv2
import os

# Defina o caminho do arquivo de vídeo
caminho_video = 'gravações/video.avi'

# Defina o diretório de saída para as imagens
caminho_imagens = 'imag_Train'

# Crie o diretório de saída se ele ainda não existir
if not os.path.exists(caminho_imagens):
    os.makedirs(caminho_imagens)

# Carregue o vídeo
cap = cv2.VideoCapture(caminho_video)

# Defina um contador para o nome dos arquivos de imagem
contador = 0

# Capture cada quadro do vídeo e salve-o como uma imagem
while (cap.isOpened()):
    # Capturar um quadro do vídeo
    ret, frame = cap.read()

    if ret == True:
        # Defina o nome do arquivo de imagem
        nome_arquivo = '{:05d}.jpg'.format(contador)

        # Salve o quadro como uma imagem
        cv2.imwrite(os.path.join(caminho_imagens, nome_arquivo), frame)

        # Incremente o contador
        contador += 1
    else:
        break

# Libere a captura de vídeo
cap.release()
