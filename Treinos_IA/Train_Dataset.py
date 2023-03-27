import cv2
import os

# Defina o diretório que contém os vídeos gravados
diretorio_videos = 'gravacoes'

# Defina o diretório onde as imagens do dataset serão salvas
diretorio_dataset = 'dataset'

# Crie o diretório do dataset, se ainda não existir
if not os.path.exists(diretorio_dataset):
    os.makedirs(diretorio_dataset)

# Defina o tamanho da imagem do dataset
tamanho_imagem = (224, 224)

# Inicie a leitura dos vídeos
for nome_arquivo in os.listdir(diretorio_videos):
    caminho_arquivo = os.path.join(diretorio_videos, nome_arquivo)
    if os.path.isfile(caminho_arquivo) and nome_arquivo.endswith('.avi'):
        print(f'Processando arquivo {nome_arquivo}...')

        # Defina o diretório onde as imagens deste vídeo serão salvas
        diretorio_video = os.path.join(diretorio_dataset, os.path.splitext(nome_arquivo)[0])
        if not os.path.exists(diretorio_video):
            os.makedirs(diretorio_video)

        # Abra o arquivo de vídeo
        cap = cv2.VideoCapture(caminho_arquivo)

        # Inicie a leitura do vídeo
        count = 0
        while cap.isOpened():
            # Capturar um frame do vídeo
            ret, frame = cap.read()

            if ret:
                # Redimensionar o frame para o tamanho desejado
                frame = cv2.resize(frame, tamanho_imagem)

                # Salvar o frame como uma imagem no diretório do vídeo
                nome_imagem = os.path.join(diretorio_video, f'frame{count:04}.jpg')
                cv2.imwrite(nome_imagem, frame)

                count += 1

                # Parar a leitura do vídeo após 1 minuto
                if count == 1800:
                    break
            else:
                break

        # Fechar o arquivo de vídeo
        cap.release()
