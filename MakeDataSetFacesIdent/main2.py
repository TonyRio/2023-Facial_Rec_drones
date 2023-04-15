import cv2
import os
import datetime

# Obtém o caminho completo do arquivo de cascata de detecção de faces
cascPath = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml')

# Carrega o arquivo de cascata de detecção de faces
face_cascade = cv2.CascadeClassifier(cascPath)

# Define o diretório para salvar as imagens de rostos
faces_dir = 'faces_dataset'

# Cria o diretório se não existir
if not os.path.exists(faces_dir):
    os.makedirs(faces_dir)

# Captura de vídeo da GoPro
cap = cv2.VideoCapture(0)  # Use o índice correto da câmera GoPro

while True:
    # Lê o frame da câmera
    ret, frame = cap.read()

    # Converte o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta as faces no frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Desenha retângulos ao redor das faces detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Salva as imagens dos rostos detectados
        face_filename = os.path.join(faces_dir, f'face_{len(os.listdir(faces_dir)) + 1}.jpg')

        # Verifica se o arquivo já existe
        if os.path.exists(face_filename):
            # Obtém a data e hora atual
            current_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

            # Acrescenta a data e hora atual ao nome do arquivo
            face_filename = os.path.join(faces_dir, f'face_{len(os.listdir(faces_dir)) + 1}_{current_time}.jpg')

        cv2.imwrite(face_filename, frame[y:y + h, x:x + w])

        # Pede a nomeação do rosto
        nome = input("Digite o nome do rosto identificado (ou pressione Enter para pular): ")
        if nome:
            # Renomeia o arquivo com o nome do rosto
            novo_face_filename = os.path.join(faces_dir, f'{nome}.jpg')
            os.replace(face_filename, novo_face_filename)
            print(f"Rosto identificado como '{nome}' e salvo como '{novo_face_filename}'")

    # Mostra o frame com as faces detectadas
    cv2.imshow('GoPro Face Recognition', frame)

    # Sai do loop quando a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha as janelas
cap.release()
cv2.destroyAllWindows()
