import cv2
import datetime
import os
import time

# Crie uma pasta "gravações" no diretório atual, se ela ainda não existir
if not os.path.exists('gravações'):
    os.makedirs('gravações')

# Defina o caminho da pasta "gravações"
caminho_gravacoes = os.path.join(os.getcwd(), 'gravações')

# Defina a captura de vídeo a partir da webcam
cap = cv2.VideoCapture(0)

# Defina o codec de vídeo e a taxa de frames (FPS)
codec = cv2.VideoWriter_fourcc(*'XVID')
fps = 30.0

# Defina as dimensões do quadro
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Inicialize o objeto de gravação de vídeo
saida_video = None

# Defina a duração de cada pacote de vídeo (1 minuto)
pacote_duracao = datetime.timedelta(minutes=1)

# Defina a hora do início do primeiro pacote
hora_inicio_pacote = datetime.datetime.now()

# Inicie a captura de vídeo
while (cap.isOpened()):
    # Capturar um quadro da webcam
    ret, frame = cap.read()

    if ret == True:
        # Se o objeto de gravação de vídeo não tiver sido inicializado
        # ou se a duração do pacote atual tiver excedido 1 minuto,
        # inicie um novo pacote de vídeo
        if saida_video is None or (datetime.datetime.now() - hora_inicio_pacote) > pacote_duracao:
            # Feche o pacote de vídeo anterior, se existir
            if saida_video is not None:
                saida_video.release()

            # Defina o nome do arquivo com base na hora atual
            nome_arquivo = datetime.datetime.now().strftime('Cap-%Y%m%d_%H%M%S') + '.avi'

            # Crie um novo objeto de gravação de vídeo com o novo nome de arquivo
            saida_video = cv2.VideoWriter(os.path.join(caminho_gravacoes, nome_arquivo), codec, fps,
                                          (frame_width, frame_height))

            # Defina a hora de início do novo pacote
            hora_inicio_pacote = datetime.datetime.now()

        # Escreva o quadro no objeto de gravação de vídeo
        saida_video.write(frame)

        # Mostrar o quadro na janela de visualização
        cv2.imshow('frame', frame)

        # Aguarde 1 milissegundo para a próxima captura
        # Pressione a tecla 'q' para sair do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Libere a captura de vídeo e o objeto de gravação de vídeo
cap.release()
if saida_video is not None:
    saida_video.release()

# Feche todas as janelas abertas
cv2.destroyAllWindows()
