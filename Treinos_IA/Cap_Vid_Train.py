import cv2
import os

# Defina a captura de vídeo a partir da webcam
cap = cv2.VideoCapture(0)

# Defina o codec de vídeo e a taxa de frames (FPS)
codec = cv2.VideoWriter_fourcc(*'XVID')
fps = 30.0

# Defina o nome do diretório de saída dos vídeos
diretorio_saida = 'gravacoes/'

# Crie o diretório de saída se ele ainda não existir
if not os.path.exists(diretorio_saida):
    os.makedirs(diretorio_saida)

# Defina a duração do pacote de vídeo (em segundos)
duracao_pacote = 60

# Defina o número do pacote
num_pacote = 1

# Inicie a captura de vídeo
while (cap.isOpened()):
    # Defina o nome do arquivo de vídeo
    nome_arquivo = f"{diretorio_saida}/video_{num_pacote}.avi"

    # Defina o objeto de gravação de vídeo e as dimensões do quadro
    saida_video = cv2.VideoWriter(nome_arquivo, codec, fps, (640, 480))

    # Defina o tempo de início do pacote
    tempo_inicio_pacote = cv2.getTickCount()

    while (True):
        # Capturar um quadro da webcam
        ret, frame = cap.read()

        if ret == True:
            # Escreva o quadro no objeto de gravação de vídeo
            saida_video.write(frame)

            # Mostrar o quadro na janela de visualização
            cv2.imshow('frame', frame)

            # Verifique se o pacote de vídeo atingiu a duração desejada
            tempo_atual = cv2.getTickCount()
            duracao_atual = (tempo_atual - tempo_inicio_pacote) / cv2.getTickFrequency()
            if duracao_atual >= duracao_pacote:
                break

            # Aguarde 1 milissegundo para a próxima captura
            # Pressione a tecla 'q' para sair do loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Libere o objeto de gravação de vídeo
    saida_video.release()

    # Verifique se o pacote de vídeo foi gravado com sucesso
    if os.path.exists(nome_arquivo):
        print(f"Pacote de vídeo {num_pacote} gravado com sucesso!")
    else:
        print(f"Erro ao gravar pacote de vídeo {num_pacote}.")

    # Verifique se o tempo de gravação excedeu o tempo desejado
    if duracao_atual >= duracao_pacote:
        break

    # Incremente o número do pacote
    num_pacote += 1

# Libere a captura de vídeo
cap.release()

# Feche todas as janelas abertas
cv2.destroyAllWindows()

# Criar um conjunto de dados de imagens a partir dos vídeos
import glob
import numpy as np

diretorio_videos = "gravacoes"
diretorio_imagens = "dataset"

if not os.path.exists(diretorio_imagens):
    os.makedirs(diretorio_imagens)

# Obter
