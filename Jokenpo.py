
from random import *
from emoji import *
from time import *

def separador():
    print("*----------------------------------------------------------------*")

def escolhaPedra():
    if escolhadopc == jogo[2]:
        print(f"Voce escolheu PEDRA e eu escolhi {escolhadopc} VOCE GANHOU!!!  ")
    elif escolhadopc == jogo[0]:
        print(f"Voce escolheu PEDRA e eu escolhi {escolhadopc} EMPATAMOS")
    else:
        print(f"Voce escolheu PEDRA e eu escolhi {escolhadopc} EU GANHEI!!!!!")

def escolhaPapel():
    if escolhadopc == jogo[0]:
        print(f"Voce escolheu {jogo[1]} e eu escolhi {escolhadopc} VOCE GANHOU!!!")
    elif escolhadopc == jogo[1]:
        print(f"Voce escolheu {jogo[1]} e eu escolhi {escolhadopc} EMPATAMOS")
    else:
        print(f"Voce escolheu {jogo[1]} e eu escolhi {escolhadopc} EU GANHEI!!!!!")

def escolhatesoura():
    if escolhadopc == jogo[1]:
        print(f"Voce escolheu {jogo[2]} e eu escolhi {escolhadopc} VOCE GANHOU!!!")
    elif escolhadopc == jogo[2]:
        print(f"Voce escolheu {jogo[2]} e eu escolhi {escolhadopc} EMPATAMOS")
    else:
        print(f"Voce escolheu {jogo[2]} e eu escolhi {escolhadopc} EU GANHEI!!!!!")




print("")
print("---------------------------------*Bem Vindo ao Pedra , Papel , Tesoura-------------------------*")
print(emojize("Escolha :\n1 - Pedra :rock: \n2 - Papel :page_facing_up: \n3 - Tesoura :scissors:" , use_aliases= True))
separador()
escolha = int(input("Qual sua escolha"))


jogo = ["PEDRA" , "PAPEL" , "TESOURA"]
escolhadopc=choice(jogo)
if escolha == 1:
    separador()
    print("Estou pensando....")
    sleep(5)
    escolhaPedra()

elif escolha == 2:
    separador()
    print("Estou pensando....")
    separador()
    sleep(5)
    escolhaPapel()
else:
    separador()
    print("Estou pensando....")
    separador()
    sleep(5)

    escolhatesoura()








