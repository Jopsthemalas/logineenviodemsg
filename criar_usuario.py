import sqlite3
import hashlib

conexao = sqlite3.connect ('cadastrosenha')
cursor = conexao.cursor ()

nome = input ("qual seu nome?")
email = input ("qual seu email:")
while True :
  senha = input ("qual sua senha :")
  confirme_senha = input ("confirme sua senha :")
  if senha == confirme_senha :
    break
  else :
   print ("a confirmaçao de senha esta errada")

sql = 'insert into usuario  (nome,email,senha)values (?,?,?)'
senha =hashlib.sha256(senha.encode('utf-8')).hexdigest().decode('utf-8')
valores = [nome,email,senha]

cursor.execute (valores,sql)

conexao.commit ()
conexao.close ()