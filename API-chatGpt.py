import os
import openai
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Define sua chave de API (recomendado usar variáveis de ambiente)
openai_api_key = os.environ.get("OPENAI_API_KEY")  # Certifique-se de configurar a variável de ambiente
if openai_api_key is None:
    openai_api_key = 'sua-chave-de-api-aqui'  # Caso contrário, defina manualmente aqui (não recomendado)

# Configura a chave de API da OpenAI
openai.api_key = openai_api_key

# Função para chamar a API da OpenAI
def call_openai_api(prompt):
    try:
        # Criando a requisição de chat
        chat_completion = openai.ChatCompletion.create(
            messages=[{"role": "user", "content": prompt}],
            model="gpt-3.5-turbo",  # ou gpt-3.5-turbo se preferir um modelo mais barato
            max_tokens=150,  # ajusta a quantidade de tokens na resposta
            temperature=0.7  # controla a criatividade da resposta
        )
        return chat_completion['choices'][0]['message']['content'].strip()  # Retorna o conteúdo da resposta
    except Exception as e:
        print(f"Erro ao chamar a API da OpenAI: {e}")
        return None

# Exemplo de uso
prompt = "Escreva um resumo sobre a importância da inovação na saúde."
response_text = call_openai_api(prompt)

if response_text:
    print("Resposta da OpenAI:", response_text)
