import cv2
import pandas as pd
import os

# Definir caminho da pasta com as imagens
folder_path = '\Carros\cars_train'

# Criar lista para armazenar DataFrames
dfs = []

# Iterar sobre as imagens na pasta
for filename in os.listdir(folder_path):
    # Verificar se o arquivo é uma imagem
    if filename.endswith('.jpg'):
        # Carregar imagem
        img = cv2.imread(os.path.join(folder_path, filename))
        # Converter para escala de cinza
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Achatar em matriz unidimensional
        flat = gray.flatten()
        # Criar DataFrame com a matriz unidimensional
        df = pd.DataFrame(flat)
        # Adicionar DataFrame à lista
        dfs.append(df)
        print(dfs)

# Concatenar DataFrames em um único DataFrame
result_df = pd.concat(dfs, axis=1)

# Salvar DataFrame em arquivo CSV
file_path = 'arquivo.csv'

# verifica se o arquivo já existe
if not os.path.isfile(file_path):
    # se o arquivo não existir, cria o arquivo
    result_df.to_csv(file_path, index=False)
    print(f'Arquivo "{file_path}" criado com sucesso!')
else:
    print(f'O arquivo "{file_path}" já existe!')
