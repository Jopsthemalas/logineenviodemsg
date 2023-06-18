
import hashlib

def validar_login(cursor):
 email =input("digite seu email:")
 senha = input('digite sua senha :')

 sql = 'select id,nome,email,senha from usuario where email =?  and senha= ?'
 senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()

 valores =[email,senha]
 
 consulta = cursor.execute (sql,valores)

 usuario=None
 for resultado in consulta:
   usuario =resultado
   break

 if usuario is None:
   raise Exception("email ou senha invalidos")
 return usuario