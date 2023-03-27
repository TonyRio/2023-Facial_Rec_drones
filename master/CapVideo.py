import cv2

# Defina a captura de vídeo a partir da webcam
cap = cv2.VideoCapture(0)

# Defina o diretório de destino para salvar as imagens capturadas
diretorio_destino = "Cap_videos/"

# Defina o codec de vídeo e a taxa de frames (FPS)
codec = cv2.VideoWriter_fourcc(*'XVID')
fps = 30.0

# Defina o objeto de gravação de vídeo e as dimensões do quadro
saida_video = cv2.VideoWriter('CapVideo.avi', codec, fps, (640, 480))

# Inicie a captura de vídeo
while (cap.isOpened()):
    # Capturar um quadro da webcam
    ret, frame = cap.read()

    if ret == True:
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
saida_video.release()

# Feche todas as janelas abertas
cv2.destroyAllWindows()
