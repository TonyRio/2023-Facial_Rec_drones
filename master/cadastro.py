import json
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


class Pessoa:
    def __init__(self, nome="", idade=0, foto=None):
        self.nome = nome
        self.idade = idade
        self.foto = foto


class JanelaCadastro:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Pessoa")

        # Criação dos campos do formulário
        self.label_nome = Label(self.master, text="Nome")
        self.label_nome.grid(row=0, column=0)
        self.entry_nome = Entry(self.master)
        self.entry_nome.grid(row=0, column=1)

        self.label_idade = Label(self.master, text="Idade")
        self.label_idade.grid(row=1, column=0)
        self.entry_idade = Entry(self.master)
        self.entry_idade.grid(row=1, column=1)

        self.label_foto = Label(self.master, text="Foto")
        self.label_foto.grid(row=2, column=0)
        self.button_foto = Button(self.master, text="Selecionar Foto", command=self.selecionar_foto)
        self.button_foto.grid(row=2, column=1)

        self.label_imagem = Label(self.master)
        self.label_imagem.grid(row=3, columnspan=2)

        self.button_salvar = Button(self.master, text="Salvar", command=self.salvar_pessoa)
        self.button_salvar.grid(row=4, columnspan=2)

        # Criação da barra de menu
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)
        self.menu_consulta = Menu(self.menu)
        self.menu.add_cascade(label="Consulta", menu=self.menu_consulta)
        self.menu_consulta.add_command(label="Buscar Pessoa", command=self.buscar_pessoa)

        self.pessoa = Pessoa()

    def selecionar_foto(self):
        # Abre a janela de seleção de arquivo
        filename = filedialog.askopenfilename(initialdir="/", title="Selecionar Foto",
                                              filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
        if filename:
            # Abre a imagem selecionada e mostra na janela
            imagem = Image.open(filename)
            imagem.thumbnail((200, 200))
            foto = ImageTk.PhotoImage(imagem)
            self.label_imagem.configure(image=foto)
            self.label_imagem.image = foto
            self.pessoa.foto = filename

    def salvar_pessoa(self):
        # Preenche os atributos do objeto pessoa com os valores dos campos do formulário
        self.pessoa.nome = self.entry_nome.get()
        self.pessoa.idade = self.entry_idade.get()

     # Salva as informações da pessoa em um arquivo JSON
        with open("pessoas.json", "a+") as arquivo:
            arquivo.seek(0)
            conteudo = arquivo.read()
            if conteudo:
                lista_pessoas = json.loads(conteudo)
