import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("200x400")

def clique():
    print("Fazer Cadastro")
texto = customtkinter.CTkLabel(janela, text="fazer cadastro")
texto.pack(padx= 10, pady=10)

nome = customtkinter.CTkEntry(janela,
                               placeholder_text="nome")
senha = customtkinter.CTkEntry(janela,
                               placeholder_text="senha")
confirmarsenha= customtkinter.CTkEntry(janela,
                               placeholder_text="confirmar senha")

botao= customtkinter.CTkButton(janela, text= "Cadastrar",
                                command=clique )





nome.pack(padx=5, pady=5)
senha.pack(padx=5, pady=5)
confirmarsenha.pack(padx=5, pady=5)
botao.pack(padx=10, pady=10)

janela.mainloop()
