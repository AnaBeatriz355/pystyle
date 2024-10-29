from tkinter import *

def semComando():
    print("")

def gravarDados():
    if tb_nome.get() != "":
        vnome = tb_nome.get()
        vfone = tb_fone.get()
        vemail = tb_email.get()
        vobs = tb_obs.get("1.0", END).strip()
        
        # Aqui você pode adicionar o código para salvar os dados
        print(f"Nome: {vnome}, Telefone: {vfone}, Email: {vemail}, Observações: {vobs}")
        
        # Limpar os campos após gravar os dados
        tb_nome.delete(0, END)
        tb_fone.delete(0, END)
        tb_email.delete(0, END)
        tb_obs.delete(1.0, END)
        
        print("Dados Gravados")
    else:
        print("Erro: Nome não pode ser vazio")

def dadosProgramador():
    # Criar uma nova janela
    janela_programador = Toplevel(app)
    janela_programador.title("Dados do Programador")
    janela_programador.geometry("500x400")
    janela_programador.configure(bg="#f0f0f0")

    # Frame para organizar os labels
    frame_programador = Frame(janela_programador, bg="#f0f0f0")
    frame_programador.pack(pady=20)

    # Labels para exibir as informações
    Label(frame_programador, text="Nome: Ana Beatriz", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
    Label(frame_programador, text="Idade: 29 anos", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
    Label(frame_programador, text="by Ana Beatriz", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)

# Função para abrir a janela de cadastro
def novocadastro():     
    nova_janela = Toplevel(app)  
    nova_janela.title("Novo Cadastro")
    nova_janela.geometry("400x600")
    nova_janela.configure(bg="#f0f0f0")    

    global tb_nome, tb_fone, tb_email, tb_obs

    # Adiciona um título estilizado 
    Label(nova_janela, text="Cadastro de Contato", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333").pack(pady=10)

    # Frame para organizar os campos de entrada 
    frame_forn = Frame(nova_janela, bg="#f0f0f0")               
    frame_forn.pack(pady=10, padx=20)

    # Campo nome 
    Label(frame_forn, text="Nome:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, pady=10, sticky=W)
    tb_nome = Entry(frame_forn, width=30, font=("Arial", 12), bd=2, relief="groove")
    tb_nome.grid(row=0, column=1, pady=10)

    # Campo telefone
    Label(frame_forn, text="Telefone:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, pady=10, sticky=W)
    tb_fone = Entry(frame_forn, width=30, font=("Arial", 12), bd=2, relief="groove")
    tb_fone.grid(row=1, column=1, pady=10)

    # Campo email 
    Label(frame_forn, text="Email:", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=0, pady=10, sticky=W)
    tb_email = Entry(frame_forn, width=30, font=("Arial", 12), bd=2, relief="groove")
    tb_email.grid(row=2, column=1, pady=10)

    # Campo observações 
    Label(frame_forn, text="Observações:", font=("Arial", 12), bg="#f0f0f0").grid(row=3, column=0, pady=10, sticky=NW)
    tb_obs = Text(frame_forn, height=5, width=30, font=("Arial", 12), bd=2, relief="groove")
    tb_obs.grid(row=3, column=1, pady=10)

    # Botão para gravar dados com estilo
    Button(nova_janela, text="Gravar Dados", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=gravarDados, bd=3, relief="raised", width=20).pack(pady=20)

# Configuração principal da janela do aplicativo 
app = Tk()
app.title("Aprendendo como usar a biblioteca Tkinter")
app.geometry("500x500")
app.configure(background="#dde")


# Menu
barraDeMenus = Menu(app)

menuContatos = Menu(barraDeMenus, tearoff=0)
menuContatos.add_command(label="Novo", command=novocadastro)
menuContatos.add_command(label="Pesquisar", command=semComando)
menuContatos.add_command(label="Deletar", command=semComando)
menuContatos.add_separator()
menuContatos.add_command(label="Fechar", command=app.quit)
barraDeMenus.add_cascade(label="Contatos", menu=menuContatos)

menuManutencao = Menu(barraDeMenus, tearoff=0)
menuManutencao.add_command(label="Banco de Dados", command=semComando)
barraDeMenus.add_cascade(label="Manutenção", menu=menuManutencao)

menuSobre = Menu(barraDeMenus, tearoff=0)
menuSobre.add_command(label="CFB Cursos", command=semComando)
barraDeMenus.add_cascade(label="Sobre", menu=menuSobre)

menuRelatorio = Menu(barraDeMenus, tearoff=0)
menuRelatorio.add_command(label="Relatório 1", command=semComando)
menuRelatorio.add_command(label="Relatório 2", command=semComando)
menuRelatorio.add_command(label="Relatório 3", command=semComando)
barraDeMenus.add_cascade(label="Relatório", menu=menuRelatorio)

menuInformacoes = Menu(barraDeMenus, tearoff=0)
menuInformacoes.add_command(label="Programa", command=semComando)
menuInformacoes.add_command(label="Programadores", command=dadosProgramador)
menuInformacoes.add_separator()
menuInformacoes.add_command(label="Fechar", command=app.quit)
barraDeMenus.add_cascade(label="Informações", menu=menuInformacoes)

app.config(menu=barraDeMenus)
app.mainloop()
