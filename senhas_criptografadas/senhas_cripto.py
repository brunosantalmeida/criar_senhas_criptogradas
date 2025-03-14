import sqlite3
import hashlib


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
    senha = input("Senha: ")
    senha_hash = hash_senha(senha)

    cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, senha_hash))
    conn.commit()
    print("Usuário cadastrado com sucesso!")

def login():
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    senha_hash = hash_senha(senha)

