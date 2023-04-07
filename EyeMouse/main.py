import cv2
import mediapipe as mp

## Variaveis Gerais

cam = cv2.VideoCapture(1)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True) # dados dos pontos do rosto

##### Capturand video
while True:
    _, frame = cam.read()
    frame = cv2.flip(frame,1)
## variavel reconhecimento facial
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame) #mostra o rosto em uma frame
    landmark_points = output.multi_face_landmarks # marca os pontos do rosto em Numeros
    frame_h, frame_w, _ = frame.shape  #Tamanho e forma

# condicão para transformar se existir rosto - mostrar posicao
    if landmark_points:
        landmarks =  landmark_points[0].landmark
        for landmark in landmarks [474:478]: # define a area do rosto que vou utilizar
            x = int(landmark.x * frame_w) # Define a largura do rosto
            y =int(landmark.y * frame_h) # define a altura do rosto

# desenha circulos em volta do rosto nos seus varios pontos
            cv2.circle(frame, (x,y), 3 , (0,255,0))
            print(x, y)


# mostrar imagem
    cv2.imshow("Mouse Ocular ", frame)
    cv2.waitKey(1)

