from usuarios import Alunos
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        self.lblid = Label(self.container2,
        text="Matrícula:", font=self.fonte, width=10)
        self.lblid.pack(side=LEFT)

        self.txtid = Entry(self.container2)
        self.txtid["width"] = 10
        self.txtid["font"] = self.fonte
        self.txtid.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar",
        font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarUsuario
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:",
        font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)


        self.lblemail= Label(self.container5, text="E-mail:",
        font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.container5)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        self.lblusuario= Label(self.container6, text="Matrícula:",
        font=self.fonte, width=10)
        self.lblusuario.pack(side=LEFT)

        self.txtmatricula = Entry(self.container6)
        self.txtmatricula["width"] = 25
        self.txtmatricula["font"] = self.fonte
        self.txtmatricula.pack(side=LEFT)

        self.lblsenha= Label(self.container7, text="Senha:",
        font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.container7)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir",
        font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirUsuario
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar",
        font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarUsuario
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir",
        font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirUsuario
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()


    def inserirUsuario(self):
        user = Alunos()

        user.nome = self.txtnome.get()
        user.email = self.txtemail.get()
        user.matricula = self.txtmatricula.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.insertUser()

        self.txtid.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtmatricula.delete(0, END)
        self.txtsenha.delete(0, END)



    def alterarUsuario(self):
        user = Alunos()

        user.id = self.txtid.get()
        user.nome = self.txtnome.get()
        user.email = self.txtemail.get()
        user.matricula = self.txtmatricula.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.updateUser()

        self.txtid.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtmatricula.delete(0, END)
        self.txtsenha.delete(0, END)



    def excluirUsuario(self):
        user = Alunos()

        user.id = self.txtid.get()

        self.lblmsg["text"] = user.deleteUser()

        self.txtid.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtmatricula.delete(0, END)
        self.txtsenha.delete(0, END)


    def buscarUsuario(self):
        user = Alunos()

        matricula = self.txtid.get()

        self.lblmsg["text"] = user.selectUser(matricula)



        self.txtid.delete(0, END)
        self.txtid.insert(INSERT, user.id)
        print(user.id)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)
        print(user.nome)

        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.email)
        print(user.email)

        self.txtmatricula.delete(0, END)
        self.txtmatricula.insert(INSERT, user.matricula)
        print(user.matricula)

        self.txtsenha.delete(0, END)
        self.txtsenha.insert(INSERT,user.senha)
        print(user.senha)

root = Tk()
Application(root)
root.mainloop()