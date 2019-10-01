from socket import  *

s = socket ()

#minhastr = "GET /rj/ HTTP/1.1\r\nHost: unilasalle.edu.br\r\nConnection: keep-alive\r\n\r\n"
minhastr = input("O que você quer dizer?")

meusbytes=str.encode (minhastr, "UTF-8")

servidor="127.0.0.1"
porta=8752

s.connect((servidor, porta))
s.send (meusbytes)

data = s.recv (4096)

print (data.decode("UTF-8"))

s.close ()
