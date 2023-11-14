# Faca um programa que permita que o usuario entre com diversos nomes e telefone para
# cadastro, e crie um arquivo com essas informacoes, uma por linha. O usuario finaliza a
# entrada com ‘0’ para o telefone.
import os, sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_agenda import Ui_Agenda


nomes = []
numeros = []
email =[]
class Agenda(QMainWindow, Ui_Agenda):
    
    with open('agenda.txt', 'a', encoding='utf8') as a:
        while True:
            nome = str(input("Nome(0 - SAIR): "))
            if nome.isnumeric():
                if int(nome) == 0:
                    print("Fechando a Agenda!!! Obrigado!")
                    break    
            fone = str(input("Telefone: "))     
            if not nome.isnumeric() and fone.isnumeric():
                nomes.append(nome)
                numeros.append(fone)
            if not fone.isnumeric():
                print("Número digitado inválido.")
                
            
        for i in range(len(nomes)):
            a.write(f'\n{nomes[i]:<15}{numeros[i]:>11}')

    with open('agenda.txt', 'r', encoding='utf8') as a:
        print(a.read())




