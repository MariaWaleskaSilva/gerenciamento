import customtkinter
from tkinter import Text

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x500")

def salvar_viagem():
    destino = entry_destino.get()
    data_inicio = entry_data_inicio.get()
    data_fim = entry_data_fim.get()
    roteiro = text_roteiro.get("1.0", "end-1c")
    print(f"Destino: {destino}")
    print(f"Data de Início: {data_inicio}")
    print(f"Data de Término: {data_fim}")
    print(f"Roteiro: {roteiro}")

label_titulo = customtkinter.CTKLabel(janela, text="Cadastro de Viagens")
label_destino = customtkinter.CTKLabel(janela, text="Destino")
entry_destino = customtkinter.CTKEntry(janela, placeholder_text="Destino da viagem")
label_data_inicio = customtkinter.CTKLabel(janela, text="Data de Início")
entry_data_inicio = customtkinter.CTKEntry(janela, placeholder_text="Data de início (dd/mm/yyyy)")
label_data_fim = customtkinter.CTKLabel(janela, text="Data de Término")
entry_data_fim = customtkinter.CTKEntry(janela, placeholder_text="Data de término (dd/mm/yyyy)")
label_roteiro = customtkinter.CTKLabel(janela, text="Roteiro")
text_roteiro = Text(janela, height=10, width=40)

botao_salvar = customtkinter.CTKButton(janela, text="Salvar Viagem", command=salvar_viagem)

label_titulo.pack(padx=10, pady=10)
label_destino.pack(padx=10, pady=(10, 0))
entry_destino.pack(padx=10, pady=(0, 10))
label_data_inicio.pack(padx=10, pady=(10, 0))
entry_data_inicio.pack(padx=10, pady=(0, 10))
label_data_fim.pack(padx=10, pady=(10, 0))
entry_data_fim.pack(padx=10, pady=(0, 10))
label_roteiro.pack(padx=10, pady=(10, 0))
text_roteiro.pack(padx=10, pady=(0, 10))
botao_salvar.pack(padx=10, pady=20)

janela.mainloop()
