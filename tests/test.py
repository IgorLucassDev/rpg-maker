import random
import tkinter as tk

# lista de valores possíveis para as características do personagem
racas = ['Humano', 'Elfo', 'Anão', 'Orc', 'Halfling']
classes = ['Guerreiro', 'Mago', 'Ladino', 'Clérigo', 'Bardo']
habilidades = ['Força', 'Destreza', 'Constituição', 'Inteligência', 'Sabedoria', 'Carisma']

# função para gerar uma ficha de personagem aleatória
def gerar_ficha():
    nome = "Personagem Aleatório"
    raca = random.choice(racas)
    classe = random.choice(classes)
    historia = f"Este personagem é um {raca} {classe} de origem desconhecida."
    atributos = {hab: random.randint(1, 20) for hab in habilidades}
    equipamentos = ['Espada curta', 'Armadura de couro', 'Poção de cura', 'Corda de escalada']
    
    # criar janela para mostrar a ficha
    janela_ficha = tk.Toplevel(root)
    janela_ficha.title("Ficha do Personagem")

    # criar widgets para mostrar as informações da ficha
    tk.Label(janela_ficha, text=f"Nome: {nome}").pack()
    tk.Label(janela_ficha, text=f"Raça: {raca}").pack()
    tk.Label(janela_ficha, text=f"Classe: {classe}").pack()
    tk.Label(janela_ficha, text=f"História: {historia}").pack()
    tk.Label(janela_ficha, text="Atributos:").pack()
    for hab, valor in atributos.items():
        tk.Label(janela_ficha, text=f"{hab}: {valor}").pack()
    tk.Label(janela_ficha, text="Equipamentos:").pack()
    for equip in equipamentos:
        tk.Label(janela_ficha, text=equip).pack()

# criar janela principal
root = tk.Tk()
root.title("Gerador de Ficha de Personagem")

# criar botão para gerar a ficha
botao_gerar = tk.Button(root, text="Gerar Ficha", command=gerar_ficha)
botao_gerar.pack()

# iniciar loop principal da interface gráfica
root.mainloop()
