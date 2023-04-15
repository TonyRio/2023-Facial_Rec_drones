import cv2
import numpy as np
from PIL import Image, ImageGrab


# Função para capturar a tela da GoPro
def capture_gopro_screen():
    # Capturar a tela utilizando o OpenCV
    screen = np.array(ImageGrab.grab())
    # Converter a imagem para escala de cinza
    gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    return gray

# Função para detectar rostos em uma imagem
def detect_faces(image):
    # Carregar o classificador de rostos do OpenCV
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Detectar rostos na imagem
    faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                          flags=cv2.CASCADE_SCALE_IMAGE)
    return faces

# Função para salvar imagens de rostos encontrados
def save_faces(image, faces, names):
    # Loop através dos rostos detectados
    for i, (x, y, w, h) in enumerate(faces):
        # Recortar a região do rosto
        face = image[y:y + h, x:x + w]
        # Salvar a imagem do rosto com o nome informado
        name = names[i]
        cv2.imwrite(f'{name}_{i}.jpg', face)

# Função para criar o dataset de rostos
def create_face_dataset():
    # Capturar a tela da GoPro
    screen = capture_gopro_screen()
    # Detectar rostos na imagem capturada
    faces = detect_faces(screen)
    # Pedir nomeação para cada rosto identificado
    names = []
    for i in range(len(faces)):
        name = input(f'Por favor, informe o nome para o rosto {i + 1}: ')
        names.append(name)
    # Salvar as imagens dos rostos encontrados
    save_faces(screen, faces, names)

# Função para realizar o reconhecimento facial
def recognize_faces(known_faces):
    # Capturar a tela da GoPro
    screen = capture_gopro_screen()
    # Detectar rostos na imagem capturada
    faces = detect_faces(screen)
    # Loop através dos rostos detectados
    for i, (x, y, w, h) in enumerate(faces):
        # Recortar a região do rosto
        face = screen[y:y + h, x:x + w]
        # Realizar o reconhecimento facial comparando com a lista prévia de rostos conhecidos
        # (neste exemplo, vamos apenas verificar se o rosto é igual a algum dos rostos conhecidos)
        face_match = False
        for known_face in known_faces:
            # Comparar as imagens de rostos utilizando a diferença absoluta dos pixels
            diff = cv2.absdiff(face, known_face)
            diff = cv
