from usuarios import Alunos
from tkinter import *
from tkinter import ttk
import tkinter as tk
    

class Aplicacao(tk.Tk):
    def __init__(self, master=None):
        tk.Tk.__init__(self)
        self._frame = None
        self.attributes('-fullscreen', True)
        self.switch_frame(Index)


    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class Index(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.container = Frame(master)
        self.container["pady"] = 10
        self.container.pack()
        self.container2 = Frame(master)
        self.container2["pady"] = 10
        self.container2.pack()

        tk.Label(self.container, text="Universidade Estácio de Sá", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", padx=20, pady=5)
        tk.Button(self, text="Painel de controle",
                  command=lambda: master.switch_frame(PainelCRUD)).pack(pady=10, padx=10, side=LEFT)
        tk.Button(self, text="Painel do professor",
                  command=lambda: master.switch_frame(PainelProfessor)).pack(pady=10, padx=10, side=LEFT)
        tk.Button(self, text="Portal dos alunos",
                  command=lambda: master.switch_frame(PortalAluno)).pack(pady=10, padx=10, side=LEFT)

class PortalAluno(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.fonte = ("Verdana", "8")
        columns = ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8')

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        tree = ttk.Treeview(self.container1, columns=columns, show='headings')
        tree.heading('#1', text='Matrícula')
        tree.heading('#2', text='Nome')
        tree.heading('#3', text='AV1')
        tree.heading('#4', text='AV2')
        tree.heading('#5', text='AV3')
        tree.heading('#6', text='AVD')
        tree.heading('#7', text='AVDS')
        tree.heading('#8', text='Média')
        aluno = Alunos()
        alunos = []
        for n in aluno.selectAllAlunos():
            if n['AV1'] and n['AV2'] and n['AVD']:
                media = round((n['AV1'] + n['AV2'] + n['AVD'])/3, 2)
                alunos.append((n['matricula'], n['nome'], n['AV1'], n['AV2'], n['AV3'], n['AVD'], n['AVDS'], media))
            else:
                alunos.append((n['matricula'], n['nome'], n['AV1'], n['AV2'], n['AV3'], n['AVD'], n['AVDS']))
        for contact in alunos:
            tree.insert('', tk.END, values=contact)

        tree.pack()
        
        self.bntInsert = Button(self, text="Fechar",
        font=self.fonte, width=12)
        self.bntInsert["command"] = self.master.destroy
        self.bntInsert.pack (side=BOTTOM)

class PainelProfessor(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
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
        self.container7["padx"] = 10
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 10
        self.container8["pady"] = 5
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9["padx"] = 10
        self.container9["pady"] = 5
        self.container9.pack()
        self.container10 = Frame(master)
        self.container10["padx"] = 10
        self.container10["pady"] = 5
        self.container10.pack()
        self.container11 = Frame(master)
        self.container11["padx"] = 10
        self.container11["pady"] = 5
        self.container11.pack()

        self.container12 = Frame(master)
        self.container12["pady"] = 15
        self.container12.pack()
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

        self.lblav1= Label(self.container7, text="AV1:",
        font=self.fonte, width=10)
        self.lblav1.pack(side=LEFT)
        self.txtav1 = Entry(self.container7)
        self.txtav1["width"] = 25
        self.txtav1["font"] = self.fonte
        self.txtav1.pack(side=LEFT)

        self.lblav2= Label(self.container8, text="AV2:",
        font=self.fonte, width=10)
        self.lblav2.pack(side=LEFT)
        self.txtav2 = Entry(self.container8)
        self.txtav2["width"] = 25
        self.txtav2["font"] = self.fonte
        self.txtav2.pack(side=LEFT)

        self.lblav3= Label(self.container9, text="AV3:",
        font=self.fonte, width=10)
        self.lblav3.pack(side=LEFT)
        self.txtav3 = Entry(self.container9)
        self.txtav3["width"] = 25
        self.txtav3["font"] = self.fonte
        self.txtav3.pack(side=LEFT)

        self.lblavd= Label(self.container10, text="AVD:",
        font=self.fonte, width=10)
        self.lblavd.pack(side=LEFT)
        self.txtavd = Entry(self.container10)
        self.txtavd["width"] = 25
        self.txtavd["font"] = self.fonte
        self.txtavd.pack(side=LEFT)

        self.lblavds= Label(self.container11, text="AVDS:",
        font=self.fonte, width=10)
        self.lblavds.pack(side=LEFT)
        self.txtavds = Entry(self.container11)
        self.txtavds["width"] = 25
        self.txtavds["font"] = self.fonte
        self.txtavds.pack(side=LEFT)
        
        self.bntInsert = Button(self.container12, text="Atualizar notas",
        font=self.fonte, width=12)
        self.bntInsert["command"] = self.atualizarNotas
        self.bntInsert.pack (side=LEFT)

        self.bntInsert = Button(self, text="Fechar",
        font=self.fonte, width=12)
        self.bntInsert["command"] = self.master.destroy
        self.bntInsert.pack (side=BOTTOM)

        self.lblmsg = Label(self.container12, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def atualizarNotas(self):
        user = Alunos()
        user.id = self.txtid.get()
        user.av1 = self.txtav1.get()
        user.av2 = self.txtav2.get()
        user.av3 = self.txtav3.get()
        user.avd = self.txtavd.get()
        user.avds = self.txtavds.get()
        self.lblmsg["text"] = user.updateNotas()
        self.txtid.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtmatricula.delete(0, END)
        self.txtav1.delete(0, END)
        self.txtav2.delete(0, END)
        self.txtav3.delete(0, END)
        self.txtavd.delete(0, END)
        self.txtavds.delete(0, END)
    
    def buscarUsuario(self):
        user = Alunos()
        matricula = self.txtid.get()
        self.lblmsg["text"] = user.selectUser(matricula)
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)
        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.email)
        self.txtmatricula.delete(0, END)
        self.txtmatricula.insert(INSERT, user.matricula)
        self.txtav1.delete(0, END)
        self.txtav1.insert(INSERT, user.AV1)
        self.txtav2.delete(0, END)
        self.txtav2.insert(INSERT, user.AV2)
        self.txtav3.delete(0, END)
        self.txtav3.insert(INSERT, user.AV3)
        self.txtavd.delete(0, END)
        self.txtavd.insert(INSERT, user.AVD)
        self.txtavds.delete(0, END)
        self.txtavds.insert(INSERT, user.AVDS)
    
class PainelCRUD(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
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

        self.bntInsert = Button(self, text="Fechar",
        font=self.fonte, width=12)
        self.bntInsert["command"] = self.master.destroy
        self.bntInsert.pack (side=BOTTOM)
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
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)
        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.email)
        self.txtmatricula.delete(0, END)
        self.txtmatricula.insert(INSERT, user.matricula)
        self.txtsenha.delete(0, END)
        self.txtsenha.insert(INSERT,user.senha)

if __name__ == "__main__":
    app = Aplicacao()
    app.mainloop()