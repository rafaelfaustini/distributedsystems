from socket import  *

s = socket ()


servidor="127.0.0.1"
porta=8753
s.connect((servidor, porta))

while True:
    minhastr = input("Digite o que será enviado: ")

    if (minhastr == ""):
        break
    meusbytes=str.encode (minhastr, "UTF-8")
    s.send (meusbytes)
    data = s.recv (8192)
    print(data.decode("UTF-8"))

s.close ()
