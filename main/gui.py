from tkinter import *
import random

def mainFunction():
    raça = ['Anão da montanha','Anão da Colina','Elfo da Floresta','Alto elfo','Elfo negro','Halfling','Humano','Draconato','Gnomo','Meio-elfo','meio-orc','Tiefling','Gnomo da Floresta','Halfling Robusto','Gnomo das rochas','Drow','Halfling pés-leves']
    raça_result = random.choice(raça)

    classe = ['Paladino','Monge','Mago','Ladino','Guerreiro','Guardião','Feiticeiro','Druida','Clérigo','Bruxo','Bardo','Bárbaro']
    classe_result = random.choice(classe)

    tendencias = ['Leal Bom','Neutro Bom','Caótico Bom','Leal Neutro','Neutro','Caótico Neutro','Leal Mau','Neutro Mau','Caótico Mau',]
    tendencias_result = random.choice(tendencias)

    #Atributos
    força = random.randint(1,18)
    destreza = random.randint(1,18)
    constituição = random.randint(1,18)
    inteligencia = random.randint(1,18)
    sabedoria = random.randint(1,18)
    carisma = random.randint(1,18)

    idiomas = ['Anão','Élfico','Gigante','Gnômico','Goblin','Halfling','Orc']
    idiomas_result = random.choice(idiomas)


    Info = f"""
    
    Raça:{raça_result}
    Classe:{classe_result}
    Tendencia:{tendencias_result}
    Atributos:
    Força:{força} | Destreza:{destreza} | Constituição:{constituição}
    Inteligencia:{inteligencia} | Sabedoria:{sabedoria} | Carisma:{carisma} 

    Deslocamento: Padrão (Varia de acordo com o personagem)

    Idiomas: Comum {idiomas_result}
    
    
    """
    #raça_resultado = raça_select
    infoLabel ['text'] = Info


#GUI
App = Tk()
App.title('RPG Generator')

Title = Label(App, text='Generate a random D&D character', font='Arial 15 bold')
Title.grid(column=0,row=0)

infoLabel = Label(App, text='')
infoLabel.grid(column=0,row=1)

generateButton = Button(App,command=mainFunction,text='Gerar Personagem')
generateButton.grid(column=0,row=2, pady=2)

App.mainloop()
