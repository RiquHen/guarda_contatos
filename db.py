import sqlite3 as sql
from sqlite3 import Error
class BancoDado:
   
    def open(self, banco):
        try: 
            self.conn =sql.connect(banco)
            self.cursor = self.conn.cursor()
            print('Conexão Criada com sucesso!!!')
        except sql.Error as e:
            print('Não foi possível criar conexão!')

    def conexao_banco(self, nome):
        con = None
        try:
            con = sql.connect(nome)
        except Error as ex:
            print(ex)
        return con
    
    def criar_tabela(self, conexao, comando):
        try:
            cur=conexao.cursor()
            cur.execute(comando)
            print('Tabela Criada')
        except Error as ex:
            print(ex)
    #Inserção de dados em uma tabel
    def inserir_dados(self, conexao, comando):
        try:
            con = conexao.cursor()
            con.execute(comando)
            conexao.commit()
            print('Cadastrado com sucesso')
        except Error as ex:
            print(ex)

    #Deletar item da tabela
    def deletar(self, conexao, comando):
        try:
            cur = conexao.cursor()
            cur.execute(comando)
            conexao.commit()
        except Error as ex:
            print(ex)
        finally:
            print("Registro Removido")

    #Atualizar um item 
    def atualizar(self, conexao, comando):
        try:
            cur = conexao.cursor()
            cur.execute(comando)
            conexao.commit()
            print('Alterado com sucesso.')
        except Error as ex:
            print('Não foi possivel realizar a alteração.')

    def buscar(self, conexao,comando ):
        try:
            cur = conexao.cursor()
            cur.execute(comando)
            resultado = cur.fetchall()
            return resultado
        except Error as ex:
            print(ex)


b=BancoDado()
b.conexao_banco('testantdo.db')