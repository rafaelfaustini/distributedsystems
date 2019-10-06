from socket import  *

s = socket ()


servidor="127.0.0.1"
porta=8753
s.connect((servidor, porta))

command = input("Type 0 to decrypt and 1 to encrypt: ")
s.send(str.encode(command,"UTF-8"))
data = s.recv(8192)
print(data.decode("UTF-8"))
minhastr = input("Digite o texto: ")
if (minhastr == ""):
    exit()
print (minhastr)
meusbytes=str.encode (minhastr, "UTF-8")
s.send (meusbytes)
data = s.recv (8192)
print("_______________________")
print (data.decode("utf-8"))
print("_______________________")
s.close ()
