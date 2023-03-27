import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Defina o caminho para o diretório do dataset
diretorio_dataset = 'dataset'

# Defina o tamanho das imagens de entrada
tamanho_imagem = (224, 224)

# Defina o número de classes
num_classes = 2

# Defina o número de épocas de treinamento
num_epochs = 10

# Defina o tamanho do lote de treinamento
batch_size = 16

# Defina o gerador de imagens de treinamento
gerador_treinamento = ImageDataGenerator(
    rescale=1./255,
    horizontal_flip=True,
    vertical_flip=True,
    rotation_range=90,
    width_shift_range=0.1,
    height_shift_range=0.1,
    validation_split=0.2
)

## CRIADOR DE IMAGENS PRE PROCESSADAS

# Criar um gerador de imagens com pré-processamento
gerador_imagens = ImageDataGenerator(rescale=1./255,
                                      rotation_range=20,
                                      width_shift_range=0.2,
                                      height_shift_range=0.2,
                                      shear_range=0.2,
                                      zoom_range=0.2,
                                      horizontal_flip=True)

# Definir o caminho para o diretório de treinamento
diretorio_treinamento = 'gravacoes/treinamento'

if not os.path.exists(diretorio_treinamento):
    os.makedirs(diretorio_treinamento)


# Criar um gerador de lotes de dados a partir do diretório de treinamento
gerador_treinamento = gerador_imagens.flow_from_directory(diretorio_treinamento,
                                                           target_size=(64, 64),
                                                           batch_size=32,
                                                           class_mode='categorical')




"""# Crie os geradores de treinamento e validação
gerador_treinamento = gerador_treinamento.flow_from_directory(
    diretorio_dataset,
    target_size=tamanho_imagem,
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'
)
"""

gerador_validacao = gerador_treinamento.flow_from_directory(
diretorio_dataset,
target_size=tamanho_imagem,
batch_size=batch_size,
class_mode='categorical',
subset='validation'
)


# Crie o modelo de rede neural
modelo = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(num_classes, activation='softmax')
])

# Compile o modelo
modelo.compile(optimizer='adam',
               loss='categorical_crossentropy',
               metrics=['accuracy'])

# Treine o modelo
modelo.fit(
    gerador_treinamento,
    epochs=num_epochs,
    validation_data=gerador_validacao
)

# Salve o modelo treinado
modelo.save('modelo.h5')
