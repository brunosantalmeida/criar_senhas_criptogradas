import sqlite3
import hashlib
import getpass

# Conectar ao banco de dados
conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    senha TEXT
)
""")
def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def cadastrar():
    nome = input("Nome de usuário: ")
    senha = getpass.getpass("Senha: ") # Oculta a senha ao digitar
    senha_hash = hash_senha(senha)

    cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, senha_hash))
    conn.commit()
    print("Usuário cadastrado com sucesso!")

def login():
    nome = input("Nome de usuário: ")
    senha = getpass.getpass("Senha: ") # Oculta a senha ao digitar
    senha_hash = hash_senha(senha)

    cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND senha = ?", (nome, senha_hash))
    
    if cursor.fetchone():
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos!")

while True:
    opcao = input("\n1 - Cadastrar\n2 - Login\n3 - Sair\nEscolha: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        login()
    elif opcao == "3":
        break
    else:
        print("Opção inválida!")

conn.close()