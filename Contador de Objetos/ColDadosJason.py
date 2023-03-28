import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Ler arquivo Json
dados = pd.read_csv('dados_imagens_carros.json')

# Salvar como arquivo CSV

dados.to_csv('arquivo.csv', index=False)


# Processar e tratar dados
dados = dados.dropna() # Remover valores nulos
# dados = dados[(dados != 0).all(axis=1)] # Remover todas as linhas que contêm pelo menos um valor igual a zero
X = dados.iloc[:, :-1] # Selecionar todas as colunas exceto a última
y = dados.iloc[:, -1] # Selecionar a última coluna
encoder = LabelEncoder()
y = encoder.fit_transform(y) # Codificar os valores categóricos para valores numéricos

# Normalizar os dados
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Dividir dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar e avaliar o modelo
# ...
