from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pymysql

print('Conectando...')
# Conectando ao banco de dados
db_connection = pymysql.connect(
    host="localhost",  # O endereço do seu banco de dados (geralmente localhost)
    user="root",  # O nome de usuário do MySQL
    password="",  # A senha do MySQL
    database="novo_nordisk"  # O nome da sua database
)
print('Conectado')
# Criando um cursor para interagir com o banco de dados
cursor = db_connection.cursor()

# Configura o ChromeDriver com o WebDriverManager
service = Service(ChromeDriverManager().install())

# Inicializa o navegador com o ChromeDriver configurado
driver = webdriver.Chrome(service=service)

# URL da página da Novo Nordisk (exemplo)
url = 'https://www.novonordisk.com.br/about/who-we-are.html'

# Acessa a URL da página
driver.get(url)

# Aguarda a página carregar completamente
driver.implicitly_wait(10)

# Pega o HTML da página carregada
html = driver.page_source

# Passa o HTML para o BeautifulSoup para análise
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

#Categorias
categoria_quemSomos = "Quem Somos"
categoria_fatosNumeros = "Fatos e números"
categoria_carreiras = "Carreiras que mudam vidas"
categoria_novoWay = "Novo Nordisk Way"


# Exemplo de como pegar o título ou parágrafos
titulo_quemSomos = soup.find('h2', class_='h2 m-xxs-bottom')
titulo_fatosNumeros = soup.find('h2', class_='color-blue smalltitle')
titulo_carreiras = soup.find('h2', class_='h2 color-blue')
titulo_novoWay = soup.find('h3', class_='h2 color-blue')

# Exemplo de como pegar parágrafos de inovação

texto_quemSomos = soup.find_all('div', class_='long-description richtext color-blue')
conteudo_quemSomos = "\n".join([paragrafo.text for paragrafo in texto_quemSomos])

texto_fatosNumeros = soup.find_all('div', class_='tb-GridColumn tb-GridColumn--l--20 tb-GridColumn--m--22 tb-GridColumn--s--22 tb-GridColumn--xs--22 tb-GridColumn--offset--l--2 tb-GridColumn--offset--m--1 tb-GridColumn--offset--xs--1')
conteudo_fatosNumeros = "\n".join([paragrafo.text for paragrafo in texto_fatosNumeros])

texto_carreiras = soup.find_all('div', class_='columns m-m-top')
conteudo_carreiras = "\n".join([paragrafo.text for paragrafo in texto_carreiras])

texto_novoWay = soup.find_all('div', class_='color-blue introtext')
conteudo_novoWay = "\n".join([paragrafo.text for paragrafo in texto_novoWay])


# Fechar o navegador após a coleta
driver.quit()

# Query para inserir os dados na tabela
insert_query = """
    INSERT INTO novoinsights (titulo, conteudo, categoria)
    VALUES (%s, %s, %s)
"""

# Dados a serem inseridos

dados_quemSomos = (titulo_quemSomos.text if titulo_quemSomos else "Sem título", conteudo_quemSomos, categoria_quemSomos)
dados_fatosNumeros = (titulo_fatosNumeros.text if titulo_fatosNumeros else "Sem título", conteudo_fatosNumeros, categoria_fatosNumeros)
dados_carreiras = (titulo_carreiras.text if titulo_carreiras else "Sem título", conteudo_carreiras, categoria_carreiras)
dados_novoWay = (titulo_novoWay.text if titulo_novoWay else "Sem título", conteudo_novoWay, categoria_novoWay)



# Executando a query para inserir os dados
cursor.execute(insert_query, dados_quemSomos)
cursor.execute(insert_query, dados_fatosNumeros)
cursor.execute(insert_query, dados_carreiras)
cursor.execute(insert_query, dados_novoWay)

# Commit para salvar as alterações no banco de dados
db_connection.commit()

# Fechando a conexão
cursor.close()
db_connection.close()

print("Dados inseridos com sucesso!")