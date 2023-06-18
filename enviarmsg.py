import sqlite3
import datetime

from autenticar import validar_login
conexao = sqlite3.connect ('cadastrosenha')
cursor = conexao.cursor ()

try:

    usuario =validar_login(cursor)
except Exception as ex :
    print (ex)
    exit ()

mensagem= input ("sua mensagem?")
hoje=datetime.date.today()
hoje= hoje.strftime('%Y-%m-%d')

sql = 'insert into mensagem (usuario,mensagem,data)values (?,?)'

valores= [usuario[0],mensagem,hoje]
cursor.execute (sql,valores)
conexao.commit ()
conexao.closer ()