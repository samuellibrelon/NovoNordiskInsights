import fitz  # PyMuPDF
import pymysql

print('Conectando...')
# Conectando ao banco de dados
db_connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="novo_nordisk"
)
print('Conectado')
cursor = db_connection.cursor()

# Definição de categorias e títulos
categorias_titulos = [
    ("LETTER FROM THE CHAIR AND THE CEO", 3, 5),
    ("Visão geral", 6, 7),
    ("Strategy", 7, 8),
    ("Financial highlights", 8, 9),
    ("Strategic Aspirations", 10, 19),
    ("Corporate Governance", 19, 20),
    ("ESG Governance", 20, 21),
    ("EU Taxonomy", 21, 22),
    ("Long-term innovation", 22, 23),
    ("Other strategies", 23, 33),
    ("Other financials", 33, 39),
    ("Risk", 40, 42),
    ("Management", 43, 47),
    ("Consolidated financial statements", 49, 83),
    ("Environmental performance", 87, 95),
    ("Auditor", 95, 98),
    ("Additional information", 99, 111)
]

# Abrir o PDF
pdf_path = 'Documents/novo-nordisk-annual-report-2023.pdf'
with fitz.open(pdf_path) as pdf:
    for titulo, start, end in categorias_titulos:
        conteudo = ""
        for page_num in range(start, end):
            page = pdf[page_num]
            conteudo += page.get_text() + "\n"

        # Inserindo no banco de dados
        insert_query = "INSERT INTO novoinsights (titulo, conteudo, categoria) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (titulo, conteudo.strip(), titulo))

# Commit das alterações
db_connection.commit()
cursor.close()
db_connection.close()
print("Dados inseridos com sucesso!")
