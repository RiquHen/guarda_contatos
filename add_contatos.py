
# Faca um programa que permita que o usuario entre com diversos nomes e telefone para
# cadastro, e crie um arquivo com essas informacoes, uma por linha. O usuario finaliza a
# entrada com ‘0’ para o telefone.
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_agenda import Ui_Agenda
from db import BancoDado

class Agenda(QMainWindow, Ui_Agenda):
    def __init__(self):
        super(Agenda,self).__init__()
        self.setupUi(self)
        
        self.btn_salvar.clicked.connect(self.cadastro)
        self.btn_buscar.clicked.connect(self.buscar)
        self.btn_limpar.clicked.connect(self.limpar)
        self.btn_deletar.clicked.connect(self.deletar)
        
    def cadastro(self):
        """
        ==>Função de cadastro de novo contato, havendo um verificação 
        para conferir se os campos foram preenchidos

        :param nome, fone, email: Passado na tela pelo usuário, são capturados e adiconados
            ao banco de dados(contatos.db)
        """
        nome = self.ln_contato.text()
        if nome.isnumeric(): #Verificação de que o nome só possui letras, caso nao apresenta msg de erro
            QMessageBox.warning(QMessageBox(), 'ERRO','Nome Inválido!!!!')
        fone = self.ln_fone.text()
        if not fone.isnumeric(): # verifica se no telefone inserido há só numeros
            QMessageBox.warning(QMessageBox(), 'ERRO', "Número digitado inválido.")
        email = self.ln_email.text()   
        if not nome.isnumeric() and fone.isnumeric(): 
            b = BancoDado()
            conexao = b.conexao_banco('agenda.db') 
            #COmando de inserção da informações no banco de dados(contatos.db)                                
            query_inserir = f'INSERT INTO contatos (nome, telefone, email) VALUES ("{nome}","{fone}","{email}")'
            b.inserir_dados(conexao,query_inserir)
            conexao.close()
        self.limpar()

    def limpar(self):
        """  ==> Função que limpa os campos preenchidos e
        retorna o cursor ao estado inicial no campo contato
        """
        self.ln_contato.clear()
        self.ln_email.clear()
        self.ln_fone.clear()
        self.ln_contato.setFocus()
            
    # Funçao busca contato, e apresenta na tela do cadastro com as informações
    def buscar(self):
        """
        ==>Função que busca de contato que emite um aviso caso o contato não esteja
        nalista(banco de dados-agenda.db), busca feita atraves do NOME do contato.
        :param encontrado: recebe o resultado(lista dentro de uma tupla) da busca no bd,
        os itens da lista que serão repassados para seus respectivos campos.
        :param b: é um objeto da classe BancoDado que veio importado do arquivo db.py
        :param query_busca: comando sql para realizar a busca no banco de dados, agenda.db
        """
        b=BancoDado()
        conexao=b.conexao_banco('agenda.db')
        busca = self.ln_contato.text()
        if len(busca) == 0:
            QMessageBox.warning(QMessageBox(), 'Erro', "Busca realizada apenas pelo nome!")
            self.limpar()
        else:
            query_busca = f'SELECT * FROM contatos WHERE nome LIKE "%{busca}%"'
            encontrado =  b.buscar(conexao, query_busca)
            if len(encontrado) !=0:
                self.ln_contato.setText(encontrado[0][1])
                self.ln_fone.setText(encontrado[0][2])
                self.ln_email.setText(encontrado[0][3])
            else:
                QMessageBox.information(QMessageBox(), 'Erro', "Usuário não encontrado!")
                self.limpar()

    def deletar(self):
        """ ==> Função que deleta contato a partir do nome preenchido no campo ln_contato(nome)
        :param nome: retirado do campo ln_contato (nome), para a inserção no query_delete
        """
        nome = self.ln_contato.text()
        b=BancoDado()
        conexao = b.conexao_banco('agenda.db') # cria conexao com o banco de dados(contatos.db)
        query_delete = f'DELETE FROM contatos WHERE nome = "{nome}"'
        b.deletar(conexao,query_delete) 
        conexao.close() # fecha a conexão com o bando de dados(contatos.db)
       

app = QApplication(sys.argv)
w=Agenda()
w.show()
app.exit(app.exec())



