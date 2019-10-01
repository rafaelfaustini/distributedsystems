from socket import *
from threading import Thread
import os

def atende (conn, cliente):
    conn.settimeout(10.00)
    try:
        d = conn.recv(4096)
        print(os.path.basename(d.decode("utf-8")))
        f=open(os.path.basename(d.decode("utf-8")), "w+")
        conn.send(str.encode("Recebido","UTF-8"))
    except:
        return
    while True:
        try:
            data = conn.recv (4096)
        except:
            print ("Erro na conexao com o cliente "+str(cliente))
            break
        if data == b'':
            break
        try:
            f.write(data.decode("utf-8"))
            conn.send(str.encode("Recebido" , "UTF-8"))        
        except:
            break
        finally:
            f.close()

        print ("Fim da conexao com "+str(cliente))
        conn.close

s = socket ()
host = "127.0.0.1"
porta = 8752
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
