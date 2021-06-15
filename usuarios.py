from database import bancoDeDados

class Alunos(object):
    def __init__(self, id = 0, nome = "",
        email = "", matricula = "", senha = ""):
        self.info = {}
        self.id = id
        self.nome = nome
        self.email = email
        self.matricula = matricula
        self.senha = senha
    
    def insertUser(self):
        database = bancoDeDados()
        try:
            c = database.conexao.cursor()
            c.execute("insert into alunos (nome, email, matricula, senha) values ('" + 
            self.nome + "', '" + 
            self.email + "', '" +
            self.matricula + "', '" + 
            self.senha + "' )")
            database.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):
        database = bancoDeDados()
        try:
            c = database.conexao.cursor()
            c.execute("update alunos set nome = '" + self.nome +
            "', email = '" + self.email +
            "', matricula = '" + self.matricula +
            "', senha = '" + self.senha +
            "' where id = " + self.id +
            " ")
            database.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):
        database = bancoDeDados()
        try:
            c = database.conexao.cursor()
            c.execute("delete from alunos where id = " + self.id + " ")
            database.conexao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"
            
    def selectUser(self, matricula):
        database = bancoDeDados()
        try:
            c = database.conexao.cursor()
            c.execute("select * from alunos where matricula = " + matricula + "  ")
            for linha in c:
                self.id = linha[0]
                self.nome = linha[1]
                self.email = linha[2]
                self.matricula = linha[3]
                self.senha = linha[4]
            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"