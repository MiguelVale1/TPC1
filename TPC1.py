# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 18:24:01 2021

@author: MV
"""
import random
def jogo():
   
    F=21#número de fósforos
    I=int(input("Se desejar jogar primeiro, prima 1, se deseja jogar em segundo, prima 2:\n"))
    s="s"
    if I==1:
        F=21
        print("Existem 21 fósforos.")#Início do jogo
        while F>2:#limite de fósforos
            jogH=int(input("De 1 a 4, qual o número de fósforos que deseja retirar? "))#jogada do utilizador
            if jogH<=0:
                print("Por favor escolha um número entre 1 e 4.")
                F=F+jogH
            elif jogH>4:
                print("Por favor escolha um número entre 1 e 4.")
                F=F+jogH
            F=F-jogH
            print("Existem",F,"fósforos.")
            #jogada humana
            if F==2:
                print("O computador decidiu retirar um fósforo.\nApenas existe um fósforo na jogada do utilizador.\nO computador venceu.")
                print("O jogo terminou.")
                jog=input("Se desejar jogar de novo pressione s: ")
                if jog==s:
                    jogo()
            elif F==jogH:
                print("O utilizador retirou o(s) último(s) fósforo(s).\nO computador venceu.")
                print("O jogo terminou.")
                jog=input("Se desejar jogar de novo pressione s: ")
                if jog==s:
                    jogo()
            #fim do jogo
            elif jogH==4:
                print("O computador decidiu retirar 1 fósforo.")
                F=F-1
                print("Existem",F, "fósforos.")
            elif jogH==3:
                print("O computador decidiu retirar 2 fósforos.")
                F=F-2
                print("Existem",F, "fósforos.")
            elif jogH==2:
                print("O computador decidiu retirar 3 fósforos.")
                F=F-3
                print("Existem",F, "fósforos.")
            elif jogH==1:
                print("O computador decidiu retirar 4 fósforos.")
                F=F-4
                print("Existem",F, "fósforos.")
            if F==1:
                print("Apenas existe 1 fósforo na jogada do utilizador.\nO computador venceu.")
                print("O jogo terminou.")
                jog=input("Se desejar jogar de novo pressione s: ")
                if jog==s:
                    jogo()
            elif F==jogH:
                print("O utilizador retirou o(s) último(s) fósforo(s).\nO computador venceu.")
                print("O jogo terminou.")
                jog=input("Se desejar jogar de novo pressione s: ")
                if jog==s:
                    jogo()
            #possibilidades do computador   
    elif I==2:
        s="s"
        E2=False
        E3=False
        Block=False
        print("Existem 21 fósforos.")
        val=[1,2,3]
        jogC=random.choice(val)
        if jogC==1:
            print("O computador decidiu retirar 1 fósforo.")
        else:
            print("O computador decidiu retirar",jogC,"fósforos.")
        F=F-jogC
        print("Existem",F,"fósforos.")
        while F>1:
            jogH=int(input("De 1 a 4, qual o número de fósforos que deseja retirar? "))
            if jogH<=0:
                print("Por favor escolha um número entre 1 e 4.")
                F=F+jogH
            elif jogH>4:
                print("Por favor escolha um número entre 1 e 4.")
                F=F+jogH
            F=F-jogH
            if F>1:
                print("Existem",F,"fósforos.")
            #jogo humano
            F=F+jogH
            if 1<=jogH and jogH<=4:
                if F==jogH:
                   print("Retirou o resto dos fósforos, logo perdeu.\nPerdeu.\nO jogo terminou.") 
                   Block=True
                   jog=input("Se desejar jogar de novo pressione s: ")
                   if jog==s:
                       jogo()
                elif F-jogH==1:
                    print("Apenas restou 1 fósforo depois da sua jogada, logo o computador perdeu.\nVenceu!\nO jogo terminou.")
                    Block=True
                    jog=input("Se desejar jogar de novo pressione s: ")
                    if jog==s:
                        jogo()
            F=F-jogH
            #linhas finais
            if E3==True:
                if jogH==4:
                    jogC=1
                    print("O computador decidiu retirar 1 fósforo.")
                    F=F-1
                elif jogH==3:
                    jogC=2
                    print("O computador decidiu retirar 2 fósforos.")
                    F=F-2
                elif jogH==2:
                    jogC=3
                    print("O computador decidiu retirar 3 fósforos.")
                    F=F-3
                elif jogH==1:
                    jogC=4
                    print("O computador decidiu retirar 4 fósforos.")
                    F=F-4
                if F==1:
                    print("Existe 1 fósforo.")
                else:
                    print("Existem",F,"fósforos.")
            #jogo de computador em vantagem
            if Block==False and 1<=jogH and jogH<=4:
                if (jogH+jogC<5 or jogH+jogC>5 or E2==True) and E3==False:
                    E2=True
                    E3=True
                    if jogH+jogC==4 or jogC+jogH==9:
                        jogC=1
                        print("O computador decidiu retirar 1 fósforo.")
                        F=F-1
                    elif jogH+jogC==3 or jogH+jogC==8:
                        jogC=2
                        print("O computador decidiu retirar 2 fósforos.")
                        F=F-2
                    elif jogH+jogC==2 or jogH+jogC==7:
                        jogC=3
                        print("O computador decidiu retirar 3 fósforos.")
                        F=F-3
                    elif jogH+jogC==6:
                        jogC=4
                        print("O computador decidiu retirar 4 fósforos.")
                        F=F-4
                    if F==1:
                        print("Existe 1 fósforo.")
                    else:
                        print("Existem",F,"fósforos.")
                #transição do jogo de computador para vantagem
                if jogH+jogC==5 and E2==False and E3==False:
                    jogC=random.choice(val)
                    if jogC==1:
                        print("O computador decidiu retirar 1 fósforo.")
                        F=F-1
                    else:
                        print("O computador decidiu retirar",jogC,"fósforos.") 
                        F=F-jogC
                    if F==1:
                        print("Existe 1 fósforo.")
                    else:
                        print("Existem",F,"fósforos.")
                #jogo do computador em desvantagem
                F=F+jogC
                if F==jogC:
                    print("O computador retirou o resto dos fósforos, logo este perdeu.\nVenceu!\nO jogo terminou.")
                    jog=input("Se desejar jogar de novo pressione s: ")
                    if jog==s:
                        jogo()
                elif F-jogC==1:
                    print("Apenas restou 1 fósforo depois da jogada do computador, logo o jogador perdeu.\nPerdeu.\nO jogo terminou.")
                    jog=input("Se desejar jogar de novo pressione s: ")
                    if jog==s:
                        jogo()
                F=F-jogC
                #linhas finais
    else:
        print("Valor inválido!")
        jogo()

jogo()


