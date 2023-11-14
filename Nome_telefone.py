# Faca um programa que permita que o usuario entre com diversos nomes e telefone para
# cadastro, e crie um arquivo com essas informacoes, uma por linha. O usuario finaliza a
# entrada com ‘0’ para o telefone.
import os, sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_agenda import Ui_Agenda


nomes = []
numeros = []
emails =[]
class Agenda(QMainWindow, Ui_Agenda):
    def __init__(self):
        super(Agenda,self).__init__()
        self.setupUi(self)
        
        self.btn_salvar.clicked.connect(self.cadastro)
        
    def cadastro(self):
        with open('agenda.txt', 'a', encoding='utf8') as a:
            nome = self.ln_contato.text()
            if nome.isnumeric():
                QMessageBox.warning(QMessageBox(), 'ERRO','Nome Inválido!!!!')
            fone = self.ln_fone.text()
            if not fone.isnumeric():
                QMessageBox.warning(QMessageBox(), 'ERRO', "Número digitado inválido.")
            email = self.ln_email.text()   
            if not nome.isnumeric() and fone.isnumeric():
                nomes.append(nome)
                numeros.append(fone)
                emails.append(email)
            self.limpar()
                    
                
            for i in range(len(nomes)):
                a.write(f'\n{nomes[i]:<15}{numeros[i]:>11}')

        """with open('agenda.txt', 'r', encoding='utf8') as a:
            print(a.read())"""

    def limpar(self):
        self.ln_contato.clear()
        self.ln_email.clear()
        self.ln_fone.clear()
        self.ln_contato.setFocus()
            
app = QApplication(sys.argv)
w=Agenda()
w.show()
app.exit(app.exec())



