import cv2
import os
import dlib

# Caminho para o arquivo XML do classificador de faces do OpenCV
caminho_classificador = 'caminho/para/o/arquivo/haarcascade_frontalface_default.xml'

# Inicializa o classificador de faces do OpenCV
classificador = cv2.CascadeClassifier(caminho_classificador)

# Inicializa o detector de faces do dlib
detector = dlib.get_frontal_face_detector()

# Caminho para o diretório onde as imagens de rostos serão salvos
diretorio_rostos = 'caminho/para/o/diretorio/de/salvamento/rostos'

# Caminho para o arquivo de lista de faces conhecidas
arquivo_lista_faces_conhecidas = 'caminho/para/o/arquivo/lista_faces_conhecidas.txt'

# Lista de faces conhecidas
lista_faces_conhecidas = []

# Lê a lista de faces conhecidas do arquivo
with open(arquivo_lista_faces_conhecidas, 'r') as arquivo:
    lista_faces_conhecidas = arquivo.read().splitlines()

# Inicializa a captura de vídeo da GoPro Hero 3
cap = cv2.VideoCapture('http://10.5.5.9:8080/live/amba.m3u8')

while True:
    # Lê um quadro do vídeo da GoPro
    ret, quadro = cap.read()

    # Converte o quadro para escala de cinza
    gray = cv2.cvtColor(quadro, cv2.COLOR_BGR2GRAY)

    # Detecta as faces no quadro usando o classificador do OpenCV
    faces = classificador.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                          flags=cv2.CASCADE_SCALE_IMAGE)

    # Para cada face detectada
    for (x, y, w, h) in faces:
        # Desenha um retângulo ao redor da face no quadro
        cv2.rectangle(quadro, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Extrai a região da face do quadro
        regiao_face = quadro[y:y + h, x:x + w]

        # Detecta a face na região usando o detector do dlib
        dets = detector(regiao_face)

        # Para cada face detectada pelo dlib
        for det in dets:
            # Converte as coordenadas do dlib para coordenadas relativas ao quadro
            x1 = det.left() + x
            y1 = det.top() + y
            x2 = det.right() + x
            y2 = det.bottom() + y

            # Salva a imagem da face no diretório de rostos
            nome = input("Digite o nome para a face identificada: ")
            cv2.imwrite(os.path.join(diretorio_rostos, 'face_{}_{}.jpg'.format(nome, len(lista_faces_conhecidas))), regiao_face)

            # Adiciona o nome da face à lista de faces conhecidas
            lista_faces_conhecidas.append(nome)

            # Salva o nome da face
