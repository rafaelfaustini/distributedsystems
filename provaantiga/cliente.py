from socket import  *
import os

s = socket ()


servidor="127.0.0.1"
porta=8752
s.connect((servidor, porta))

def envia(conexao,texto):
    conexao.send(str.encode(texto, "UTF-8"))
    print(texto)

nome = input("Digite o nome do arquivo: ")
envia(s, nome)
data = s.recv (8192)
print(data.decode("UTF-8"))
with open(nome, "r") as f:
    for linha in f: 
        envia(s,linha)
    envia(s,"")
s.close ()
