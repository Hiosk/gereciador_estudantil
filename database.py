import sqlite3

class bancoDeDados():
    def __init__(self):
        self.conexao = sqlite3.connect('./database.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists alunos (
                    id integer primary key autoincrement ,
                    nome text,
                    email text type UNIQUE,
                    matricula text type UNIQUE,
                    senha text)""")
        self.conexao.commit()
        c.close()