
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sqlalchemy import create_engine

# Baixar os recursos necessários do NLTK se ainda não tiver
import nltk
nltk.download('punkt_tab')

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Conectar ao banco de dados (ajustar para seu banco)
engine = create_engine('mysql+pymysql://root:@localhost/novo_nordisk')  # Ajuste conforme necessário

# Carregar dados do banco de dados
df = pd.read_sql('SELECT * FROM novoinsights', engine)


# Função de pré-processamento
def preprocess_text(text):
    # 1. Remover valores nulos
    if not text:
        return ""

    # 2. Remover caracteres especiais e números
    text = re.sub(r'[^A-Za-záàâãéèêíïóôõúç]+', ' ', text)

    # 3. Converter para minúsculas
    text = text.lower()

    # 4. Tokenização
    tokens = word_tokenize(text)

    # 5. Remover stopwords (tanto para português quanto para inglês)
    stop_words = set(stopwords.words('portuguese')).union(set(stopwords.words('english')))
    tokens = [word for word in tokens if word not in stop_words]

    # 6. Lemmatização
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Recriar o texto com as palavras processadas
    return ' '.join(tokens)


# Aplicar o pré-processamento na coluna 'conteúdo'
df['conteudo_limpo'] = df['conteudo'].apply(preprocess_text)

# Exibir os dados processados
print(df[['conteudo', 'conteudo_limpo']].head())

# Atualizar o banco de dados com os dados limpos
# Conectar diretamente com o banco para atualizar os registros
from sqlalchemy import text

update_query = text("""
    UPDATE novoinsights
    SET conteudo = :conteudo
    WHERE id = :id
""")

# Atualizando com parâmetros nomeados
with engine.connect() as connection:
    for index, row in df.iterrows():
        connection.execute(update_query, {'conteudo': row['conteudo_limpo'], 'id': row['id']})

# Confirmação de que os dados foram atualizados
print("Conteúdo limpo foi salvo no banco de dados.")