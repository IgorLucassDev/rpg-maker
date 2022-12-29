#Character creator for RPG-D&D
from tkinter import *
import random

"""

 Raça
    elfo da floresta
    halfling
    anão da colina
    anão da montanha
    humano
    alto elfo
    elfo negro
    gnomo
    draconato
    tieflings
    meio-elfo
    meio-orc
        

 Classe
    Guerreiro
 Personalidade e Aparencia
 Antecedentes do personagem


 Tipo de aventureiro
    Guerreiro corajoso
    Ladino Furtivo
    Clérigo ferveroso
    Mago extravagante

    Atirador de Elite

"""

raça = ['Anão da montanha','Anão da Colina','Elfo da Floresta','Alto elfo','Elfo negro','Halfling','Humano','Draconato','Gnomo','Meio-elfo','meio-orc','Tiefling','Gnomo da Floresta','Halfling Robusto','Gnomo das rochas','Drow','Halfling pés-leves']
raça_resultado = random.choice(raça)

tendencias = ['Leal Bom','Neutro Bom','Caótico Bom','Leal Neutro','Neutro','Caótico Neutro','Leal Mau','Neutro Mau','Caótico Mau',]


print('O seu personagem é um {}'.format(raça_resultado))

print('Tendencia:', random.choice(tendencias))


força = random.randint(1,18)
destreza = random.randint(1,18)
Constituição = random.randint(1,18)
inteligencia = random.randint(1,18)
sabedoria = random.randint(1,18)
carisma = random.randint(1,18)
print('Atributos: \n ''Força: {:1} Destreza: {} Constituição: {} \n Inteligencia: {} Sabedoria: {} Carisma: {}'.format(força,destreza,Constituição,inteligencia,sabedoria,carisma))

print('Deslocamento: 9m')

idiomas = ['Anão','Élfico','Gigante','Gnômico','Goblin','Halfling','Orc']
print('Idiomas: Comum,', random.choice(idiomas))

print('Bonus de Proficiência: +2')

#10:35
