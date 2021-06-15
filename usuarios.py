from database import bancoDeDados

class Alunos(object):
    def __init__(self, id = 0, nome = "",
        email = "", matricula = "", senha = "", AV1 = "", AV2 = "", AV3 = "", AVD = "", AVDS = ""):
        self.info = {}
        self.id = id
        self.nome = nome
        self.email = email
        self.matricula = matricula
        self.senha = senha
        self.AV1 = AV1
        self.AV2 = AV2
        self.AV3 = AV3
        self.AVD = AVD
        self.AVDS = AVDS

    def selectAllAlunos(self):
        database = bancoDeDados()
        try:
            c = database.conexao.cursor()
            c.execute("select * from alunos")
            
            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"
    
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
            "' where matricula = " + self.id +
            " ")
            database.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"
    def updateNotas(self):
        database = bancoDeDados()
        try:
            c = database.conexao.cursor()
            c.execute("update alunos set AV1 = '" + self.av1 +
            "', AV2 = '" + self.av2 +
            "', AV3 = '" + self.av3 +
            "', AVD = '" + self.avd +
            "', AVDS = '" + self.avds +
            "' where matricula = " + self.id +
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
                self.AV1 = linha[5]
                self.AV2 = linha[6]
                self.AV3 = linha[7]
                self.AVD = linha[8]
                self.AVDS = linha[9]
            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"