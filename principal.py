import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("200X400")

def clique():
    print("Seja vem vindo!")

texto = customtkinter.CTkLabel(janela, text="Seja bem vindo!")
texto.pack(padx= 10, pady=10)

viagens = customtkinter.CTkButton(janela, text= "Para onde vamos hoje?",
                                command=clique )
visitei = customtkinter.CTkButton(janela, text= "Lugares que já visitei",
                                command=clique )
atualizaçao = customtkinter.CTkButton(janela, text= "Atualização de dados",
                                command=clique )
sair = customtkinter.CTkButton(janela, text= "voltar ao início",
                               command=clique )

viagens.pack(padx= 10, pady=10)
viagens.pack(padx=5, pady=5)
visitei.pack(padx=5, pady=5)
atualizaçao.pack(padx=5, pady=5)
sair.pack(padx=5, pady=5)

janela.mainloop()
