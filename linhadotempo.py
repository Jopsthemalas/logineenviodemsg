import sqlite3
import datetime

import sqlite3

from autenticar import validar_login

conexao = sqlite3.connect ('cadastrosenha')
cursor = conexao.cursor ()

try:

    usuario =validar_login(cursor)
except Exception as ex :
    print (ex)
    exit ()

sql ='''selec u.nome, u.texto, m.data, from mensagem m inner join usuario u on m.usuario_id=u.id
    where m.usuario_id in (select c.alvo_id from conexao c where  c.usuario_id= ? )or m.usuario_id=?'''

valores = [usuario[0],usuario[0]]
consulta = cursor.execute (sql,valores)
for resultado in consulta :
  print ( 'nome:',resultado[0],'texto:'resultado[1],'data:'usuario[2])

conexao.close()