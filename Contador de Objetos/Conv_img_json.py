import os
import json

# Definir o caminho da pasta que contém as imagens
folder_path = '\\Carros\\cars_train\\'

# Listar as imagens na pasta
images = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

# Criar uma lista para armazenar as informações de cada imagem
data = []

# Loop para percorrer cada imagem e obter informações
for image in images:
    # Obter o caminho completo da imagem
    image_path = os.path.join(folder_path, image)

    # Obter informações adicionais da imagem, se necessário
    # Por exemplo, se a imagem contém um objeto específico, podemos incluir uma label

    # Adicionar as informações em um dicionário
    image_data = {'image_path': image_path}

    # Adicionar o dicionário à lista de dados
    data.append(image_data)

# Salvar as informações em um arquivo JSON
with open('dados_imagens_carros.json', 'w') as f:
    json.dump(data, f)
