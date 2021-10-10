# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 18:24:01 2021

@author: MV
"""
import random
def jogo():
   
    F=21#número de fósforos
    I=int(input("Se desejar jogar primeiro, prima 1, se deseja jogar em segundo, prima 2:\n"))#decisão do jogo
    s="s"#variável para recomeçar o jogo
    if I==1:
        F=21
        print("Existem 21 fósforos.")#Início do jogo
        while F>1:#limite de fósforos
            jogH=int(input("De 1 a 4, qual o número de fósforos que deseja retirar? "))#jogada do utilizador
            if jogH<=0:
                print("Por favor escolha um número entre 1 e 4.")#limite inferior da jogada
                F=F+jogH
            elif jogH>4:
                print("Por favor escolha um número entre 1 e 4.")#limite superior da jogada
                F=F+jogH
            F=F-jogH
            print("Existem",F,"fósforos.")
            #jogada humana^^
            if jogH==4:
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
            #possíveis jogadas do computador em vantagem^^
            if F==1:
                print("Apenas existe 1 fósforo na jogada do utilizador.\nO computador venceu.")
                print("O jogo terminou.")
                jog=input("Se desejar jogar de novo pressione s: ")#se quiserem recomeçar o jogo
                if jog==s:
                    jogo()
            #jogada final^^
    elif I==2:
        s="s"#variável para recomeçar o jogo
        E2=False#estratégia número 2 do computador (para entrar em vantagem)
        E3=False#estratégia número 3 do computador (para permanecer em vantagem)
        Block=False#bloquear qualquer próxima jogada depois do jogo terminar
        print("Existem 21 fósforos.")
        val=[1,2,3,4]#possíveis jogadas do computador
        jogC=random.choice(val)#escolha aleatória de uma jogada
        if jogC==1:
            print("O computador decidiu retirar 1 fósforo.")
        else:
            print("O computador decidiu retirar",jogC,"fósforos.")
        F=F-jogC
        print("Existem",F,"fósforos.")
        while F>1:#limite de fósforos
            jogH=int(input("De 1 a 4, qual o número de fósforos que deseja retirar? "))#jogada humana
            if jogH<=0:
                print("Por favor escolha um número entre 1 e 4.")#limite inferior da jogada
                F=F+jogH
            elif jogH>4:
                print("Por favor escolha um número entre 1 e 4.")#limite superior da jogada
                F=F+jogH
            F=F-jogH
            if F>1:
                print("Existem",F,"fósforos.")
            #jogada humana^^
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
            #últimas mensagens se o jogo terminar na jogada humana^^
            if E3==True:#se a estratégia número 3 for "ativada"
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
            #jogo de computador para permanecer em vantagem^^
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
                #transição do jogo de computador para vantagem^^
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
                #jogo do computador em desvantagem^^
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
                #linhas finais do jogo se o computador perder^^
    else:
        print("Valor inválido!")#se a decisão do jogo for inválida
        jogo()

jogo()


