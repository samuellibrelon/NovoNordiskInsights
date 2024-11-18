from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # Para instalar automaticamente o ChromeDriver#
from bs4 import BeautifulSoup
import pymysql

print('Conectando...')
# Conectando ao banco de dados
db_connection = pymysql.connect(
    host="localhost",        # O endereço do seu banco de dados (geralmente localhost)
    user="root",   # O nome de usuário do MySQL
    password="",       # A senha do MySQL
    database="novo_nordisk"  # O nome da sua database
)
print('conectado')
# Criando um cursor para interagir com o banco de dados
cursor = db_connection.cursor()

# Configura o ChromeDriver com o WebDriverManager
service = Service(ChromeDriverManager().install())

# Inicializa o navegador com o ChromeDriver configurado
driver = webdriver.Chrome(service=service)

# URL da página da Novo Nordisk (exemplo)
url = 'https://www.novonordisk.com.br/innovation-in-our-company-brazil.html'

# Acessa a URL da página
driver.get(url)

# Aguarda a página carregar completamente
driver.implicitly_wait(10)

# Pega o HTML da página carregada
html = driver.page_source

# Passa o HTML para o BeautifulSoup para análise
soup = BeautifulSoup(html, 'html.parser')

categoria_inovacao = "Inovação"
categoria_conquistas = "Conquistas"

# Exemplo de como pegar o título ou parágrafos
titulo_principal = soup.find('h2', class_='text plaintexttitle title color-blue smalltitle')
titulo_conquistas = soup.find('h2', class_='h5-s m-xs-bottom title')

# Coleta de parágrafos de inovação
texto_inovacao = soup.find_all('div', class_='text color-blue introtext')
conteudo_inovacao = "\n".join([paragrafo.text for paragrafo in texto_inovacao])

# Coleta de parágrafos de conquistas
texto_conquistas = soup.find_all('p', class_='description leadtext m-m-bottom')
conteudo_conquistas = "\n".join([paragrafo.text for paragrafo in texto_conquistas])

detalhe_conquistas = soup.find_all('p', class_='color-blue subtext paragraph-s paragraph-line-break rtl-text')
conteudo_conquistas += "\n".join([paragrafo.text for paragrafo in detalhe_conquistas])

# Fechar o navegador após a coleta
driver.quit()

# Query para inserir os dados na tabela
insert_query = """
    INSERT INTO novoinsights (titulo, conteudo, categoria)
    VALUES (%s, %s, %s)
"""

# Dados a serem inseridos
dados_inovacao = (titulo_principal.text if titulo_principal else "Sem título", conteudo_inovacao, categoria_inovacao)
dados_conquistas = (titulo_conquistas.text if titulo_conquistas else "Sem título", conteudo_conquistas, categoria_conquistas)

# Executando a query para inserir os dados
cursor.execute(insert_query, dados_inovacao)
cursor.execute(insert_query, dados_conquistas)

# Commit para salvar as alterações no banco de dados
db_connection.commit()

# Fechando a conexão
cursor.close()
db_connection.close()

print("Dados inseridos com sucesso!")
