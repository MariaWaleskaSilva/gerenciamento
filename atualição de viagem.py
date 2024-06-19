import customtkinter
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkComboBox, CTkTextbox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = CTk()
janela.geometry("200x400")

viagens = {
    "Viagem 1": {"destino": "Paris", "data_inicio": "01/07/2024", "data_fim": "10/07/2024", "roteiro": "Torre Eiffel, Louvre"},
    "Viagem 2": {"destino": "Roma", "data_inicio": "15/08/2024", "data_fim": "25/08/2024", "roteiro": "Coliseu, Vaticano"}
}

def carregar_dados(event):
    viagem_selecionada = combo_viagens.get()
    if viagem_selecionada in viagens:
        dados = viagens[viagem_selecionada]
        entry_destino.delete(0, "end")
        entry_destino.insert(0, dados["destino"])
        entry_data_inicio.delete(0, "end")
        entry_data_inicio.insert(0, dados["data_inicio"])
        entry_data_fim.delete(0, "end")
        entry_data_fim.insert(0, dados["data_fim"])
        text_roteiro.delete("1.0", "end")
        text_roteiro.insert("1.0", dados["roteiro"])

def salvar_viagem():
    viagem_selecionada = combo_viagens.get()
    destino = entry_destino.get()
    data_inicio = entry_data_inicio.get()
    data_fim = entry_data_fim.get()
    roteiro = text_roteiro.get("1.0", "end-1c")
    
    if viagem_selecionada in viagens:
        viagens[viagem_selecionada] = {
            "destino": destino,
            "data_inicio": data_inicio,
            "data_fim": data_fim,
            "roteiro": roteiro
        }
        print(f"Viagem '{viagem_selecionada}' atualizada com sucesso!")
    else:
        print(f"Erro: Viagem '{viagem_selecionada}' não encontrada!")

label_titulo = CTkLabel(janela, text="Atualizar Dados da Viagem")
label_viagem = CTkLabel(janela, text="Selecione a Viagem")
combo_viagens = CTkComboBox(janela, values=list(viagens.keys()), command=carregar_dados)

label_destino = CTkLabel(janela, text="Destino")
entry_destino = CTkEntry(janela, placeholder_text="Destino da viagem")
label_data_inicio = CTkLabel(janela, text="Data de Início")
entry_data_inicio = CTkEntry(janela, placeholder_text="Data de início (dd/mm/yyyy)")
label_data_fim = CTkLabel(janela, text="Data de Término")
entry_data_fim = CTkEntry(janela, placeholder_text="Data de término (dd/mm/yyyy)")
label_roteiro = CTkLabel(janela, text="Roteiro")
text_roteiro = CTkTextbox(janela, height=150, width=350)

botao_salvar = CTkButton(janela, text="Salvar Alterações", command=salvar_viagem)

label_titulo.pack(padx=10, pady=10)
label_viagem.pack(padx=10, pady=(10, 0))
combo_viagens.pack(padx=10, pady=(0, 10))
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
