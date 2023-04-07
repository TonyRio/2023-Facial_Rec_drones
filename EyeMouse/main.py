import cv2
import mediapipe as mp
import pyautogui as ptg

## Variaveis Gerais

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True) # dados dos pontos do rosto
screen_w, screen_h = ptg.size()
##### Capturand video
while True:
    _, frame = cam.read()
    frame = cv2.flip(frame,1)  # espelha a imagem, ou inverte
## variavel reconhecimento facial
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame) #mostra o rosto em uma frame
    landmark_points = output.multi_face_landmarks # marca os pontos do rosto em Numeros
    frame_h, frame_w, _ = frame.shape  #Tamanho e forma

# condicão para transformar se existir rosto - mostrar posicao
    if landmark_points:
        landmarks =  landmark_points[0].landmark
        for id, landmark in enumerate(landmarks [474:478]): # define a area do rosto que vou utilizar
            x = int(landmark.x * frame_w) # Define a largura do rosto
            y =int(landmark.y * frame_h) # define a altura do rosto

# desenha circulos em volta do rosto nos seus varios pontos
            cv2.circle(frame, (x,y), 3 , (0,255,0))
# direciona a posicao do olho para controlar o cursor do mouse
            if id ==1:
# coordenadas transferidas para o cursor pelo tamanho da tela
                screen_x = screen_w / frame_w *x
                screen_y = screen_h /frame_h *y
                ptg.moveTo(screen_x,screen_y)
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)  # Define a largura do Frame
            y = int(landmark.y * frame_h)  # define a altura do Frame
# desenha circulos em volta do rosto nos seus varios pontos
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
            #print(left[0].y - left[1].y)
# prepara para quando valor for menor clicar
        if (left[0].y - left[1].y ) < 0.01:
            ptg.click()
            ptg.sleep(.5)
            print(" C L I C K ")
# mostrar imagem
    cv2.imshow("Mouse Ocular ", frame)
    cv2.waitKey(1)

