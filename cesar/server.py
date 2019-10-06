from socket import *
from threading import Thread
import cesar
ROTATION = 5
def atende (conn, cliente):

        conn.settimeout(10.00)
        command = conn.recv(4096)
        conn.send(str.encode("Recebido", "UTF-8"))
        try:
            data = conn.recv (4096)
        except:
            print ("Erro na conexao com o cliente "+str(cliente))
            return
        if command== b'' or data==b'':
            return
                
        texto=''
        if command == b'0':
            texto = cesar.encrypt(data.decode("utf-8"), ROTATION)
        elif command == b'1':
            texto = cesar.decrypt(data.decode("utf-8"), ROTATION)
        try:
            conn.send(str.encode(texto , "UTF-8"))
        except:
            return
        print ("Fim da conexao com "+str(cliente))
        conn.close

s = socket ()
host = "127.0.0.1"
porta = 8753
s.bind ((host, porta))
s.listen (100)
nthr = 0

while True:
        (conn, cliente) = s.accept ()

        print ("Recebi a conexao de "+str(cliente))
        nthr += 1
        print ("Criando thread "+str(nthr))
        t = Thread(target=atende,args=(conn, cliente,))
        t.start()
