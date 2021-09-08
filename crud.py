#import MySQLdb
from pymysql import connect, cursors
#pip install pymysql

class BD:
    def __init__(self, host,user,passwd,schema):
        self.conn = connect(host = host ,user=user, passwd=passwd,  port=3306)
        self.schema = schema
    
    def ler_dado(self, dados, tabela, condicao = None, print_SLQ = False):
        try:
            cursor = self.conn.cursor()
            cursor.execute("USE {}".format(self.schema))
            if condicao == None:
                SQL = "SELECT {} FROM {}".format(dados,tabela)
            else:
                SQL = "SELECT {} FROM {} WHERE {}".format(dados,tabela,condicao)
            if print_SLQ:
                print(SQL)
            cursor.execute(SQL)
            cursor.close()
            return cursor.fetchall()
        except:
            print("Erro na leitura com os parametros:\n {} \n {}".format(dados,tabela))
            return False

    def escrever_dado(self, colunas,dados,tabela, print_SLQ = False):
        try:
            cursor = self.conn.cursor()
            cursor.execute("USE {}".format(self.schema))
            SQL = "INSERT INTO {} ({}) values ({});".format(tabela,colunas,dados)
            if print_SLQ:
                print(SQL)
            cursor.execute(SQL)
            cursor.close()
            self.conn.commit()
            return True
        except:
            print(SQL)
            print("Erro na escrita com os parametros:\n {} \n {} \n {}".format(colunas,dados,tabela))
            return False
    
    def deletar_dado(self, tabela, condicao, print_SLQ = False):
        try:
            cursor = self.conn.cursor()
            cursor.execute("USE {}".format(self.schema))
            SQL = "DELETE FROM {} WHERE {}".format(tabela,condicao)
            if print_SLQ:
                print(SQL)
            cursor.execute(SQL)
            cursor.close()
            self.conn.commit()
            return True
        except:
            print("Erro ao deletar com os parametros:\n {} \n {}".format(condicao,tabela))
            return False

            


bd = BD('127.0.0.1','root','','tbr_api') 

print(bd.ler_dado('id,nome,email','user'))

#print(bd.escrever_dado("id, email, nome, tel, endereco" , "NULL, 'test@gmail.com', 'Miguel', '23132', 'waewd'" , 'user'))
print(bd.deletar_dado('user','id = 9'))
print(bd.ler_dado('id,nome,email','user'))