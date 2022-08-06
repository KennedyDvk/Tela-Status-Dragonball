from tkinter import *
from tkinter import ttk

#importando Pillow para colocar imagens
from PIL import Image, ImageTk

from Dados import *

co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#ef5350"   # vermelha

janela = Tk()
janela.title('')
janela.geometry('800x500')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

#frame
frame_guerreiro = Frame(janela, width=550, height=290, relief='flat')
frame_guerreiro.grid(row=1, column=0)

def trocar_guerreiro(i):
    global imagem_guerreiro, pers_imagem

    #Cor do fundo do Frame
    frame_guerreiro['bg'] = personagem[i]['Raça'][3]

    #tipo guerreiro
    pers_nome['text'] = i
    pers_nome['bg'] = personagem[i]['Raça'][3]
    pers_tipo['text'] = personagem[i]['Raça'][1]
    pers_tipo['bg'] = personagem[i]['Raça'][3]
    pers_id['text'] = personagem[i]['Raça'][0]
    pers_id['bg'] = personagem[i]['Raça'][3]

    imagem_guerreiro = personagem[i]['Raça'][2]

    # imagens
    imagem_guerreiro = Image.open(imagem_guerreiro)
    imagem_guerreiro = imagem_guerreiro.resize((150, 238))
    imagem_guerreiro = ImageTk.PhotoImage(imagem_guerreiro)

    pers_imagem = Label(frame_guerreiro, image=imagem_guerreiro, relief='flat', bg=personagem[i]['Raça'][3], fg=co1)
    pers_imagem.place(x=200, y=50)

    pers_tipo.lift()

    #Status dos Guerreiros
    pers_hp['text'] = personagem[i]['status'][0]
    pers_ataque['text'] = personagem[i]['status'][1]
    pers_defesa['text'] = personagem[i]['status'][2]
    pers_velocidade['text'] = personagem[i]['status'][3]

    pers_hb_1['text'] = personagem[i]['Habilidades'][0]
    pers_hb_2['text'] = personagem[i]['Habilidades'][1]
    pers_hb_3['text'] = personagem[i]['Habilidades'][2]



#nome
pers_nome = Label(frame_guerreiro, text='', relief='flat', anchor=CENTER, font=('fixedsys 20'), fg=co1)
pers_nome.place(x=12, y=15)

#categoria
pers_tipo = Label(frame_guerreiro, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pers_tipo.place(x=12, y=50)

#id
pers_id = Label(frame_guerreiro, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pers_id.place(x=12, y=75)

#status
pers_status = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pers_status.place(x=70, y=310)

#HP
pers_hp = Label(janela, text='HP: 800', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pers_hp.place(x=70, y=360)

#Ataque
pers_ataque = Label(janela, text='Ataque: 1000', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pers_ataque.place(x=70, y=385)

#Defesa
pers_defesa = Label(janela, text='Defesa: 750', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pers_defesa.place(x=70, y=410)

#Velocidade
pers_velocidade = Label(janela, text='Velocidade: 500', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pers_velocidade.place(x=70, y=435)

#Habilidade
pers_habilidade = Label(janela, text='Habilidade', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pers_habilidade.place(x=400, y=310)

#Hb-1
pers_hb_1 = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pers_hb_1.place(x=400, y=360)

#Hb-2
pers_hb_2 = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pers_hb_2.place(x=400, y=385)

pers_hb_3 = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pers_hb_3.place(x=400, y=410)

#criando botões

#imagem botoes
#imagens
imagem_guerreiro_1 = Image.open('images/Son Gokutorso.png')
imagem_guerreiro_1 = imagem_guerreiro_1.resize((40, 40))
imagem_guerreiro_1 = ImageTk.PhotoImage(imagem_guerreiro_1)

pers_imagem_b1 = Button(janela, command=lambda:trocar_guerreiro('Son Goku'), image=imagem_guerreiro_1, text='Son Goku', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
pers_imagem_b1.place(x=600, y=10)

imagem_guerreiro_2 = Image.open('images/Vegetatorso.png')
imagem_guerreiro_2 = imagem_guerreiro_2.resize((40, 40))
imagem_guerreiro_2 = ImageTk.PhotoImage(imagem_guerreiro_2)

pers_imagem_b2 = Button(janela, command=lambda:trocar_guerreiro('Vegeta'), image=imagem_guerreiro_2, text='Vegeta', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
pers_imagem_b2.place(x=600, y=65)

imagem_guerreiro_3 = Image.open('images/Picolotorso.png')
imagem_guerreiro_3 = imagem_guerreiro_3.resize((40, 40))
imagem_guerreiro_3 = ImageTk.PhotoImage(imagem_guerreiro_3)

pers_imagem_b3 = Button(janela, command=lambda:trocar_guerreiro('Picollo'), image=imagem_guerreiro_3, text='Picollo', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
pers_imagem_b3.place(x=600, y=120)

imagem_guerreiro_4 = Image.open('images/Gohantorso.png')
imagem_guerreiro_4 = imagem_guerreiro_4.resize((55, 45))
imagem_guerreiro_4 = ImageTk.PhotoImage(imagem_guerreiro_4)

pers_imagem_b4 = Button(janela, command=lambda:trocar_guerreiro('Gohan'), image=imagem_guerreiro_4, text='Gohan', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
pers_imagem_b4.place(x=600, y=175)

imagem_guerreiro_5 = Image.open('images/Krillin torso.png')
imagem_guerreiro_5 = imagem_guerreiro_5.resize((55, 45))
imagem_guerreiro_5 = ImageTk.PhotoImage(imagem_guerreiro_5)

pers_imagem_b5 = Button(janela, command=lambda:trocar_guerreiro('Kuririn'), image=imagem_guerreiro_5, text='Kuririn', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
pers_imagem_b5.place(x=600, y=230)

imagem_guerreiro_6 = Image.open('images/brolietorso.png')
imagem_guerreiro_6 = imagem_guerreiro_6.resize((55, 45))
imagem_guerreiro_6 = ImageTk.PhotoImage(imagem_guerreiro_6)

pers_imagem_b6 = Button(janela, command=lambda:trocar_guerreiro('Broly'), image=imagem_guerreiro_6, text='Broly', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
pers_imagem_b6.place(x=600, y=285)

imagem_guerreiro_7 = Image.open('images/Future Trunks_Torso.png')
imagem_guerreiro_7 = imagem_guerreiro_7.resize((55, 45))
imagem_guerreiro_7 = ImageTk.PhotoImage(imagem_guerreiro_7)

pers_imagem_b7 = Button(janela, command=lambda:trocar_guerreiro('Trunks do Futuro'), image=imagem_guerreiro_7, text='Trunks', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
pers_imagem_b7.place(x=600, y=340)


imagem_guerreiro_8 = Image.open('images/Freezatorso.png')
imagem_guerreiro_8 = imagem_guerreiro_8.resize((55, 45))
imagem_guerreiro_8 = ImageTk.PhotoImage(imagem_guerreiro_8)

pers_imagem_b8 = Button(janela, command=lambda:trocar_guerreiro('Freeza'), image=imagem_guerreiro_8, text='Freeza', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
pers_imagem_b8.place(x=600, y=395)

import random

lista_guerreirosz = ['Son Goku', 'Vegeta', 'Picollo', 'Gohan', 'Kuririn', 'Freeza']
gurreiro_escolhido = random.sample(lista_guerreirosz, 1)

trocar_guerreiro(gurreiro_escolhido[0])


janela.mainloop()