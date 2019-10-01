from socket import *
import threading

def atende(conn,cliente):
            while True:

                data = conn.recv (4096)
                if not data:
                        break
                print (str(cliente)+" enviou "+data.decode("utf-8") )
                conn.send (str.encode ("Mensagem: "+data.decode("utf-8") , "UTF-8"))
                print ("Finalizada conexao com "+str(cliente))

s = socket ()

host = "0.0.0.0"
porta = 8752
s.bind ((host, porta))
s.listen (10)

threads = []

while True:
    (conn,cliente) = s.accept()
    print("Recebi a conexao de "+str(i))
    threads.append(Thread(target=atende, args=(conn,cliente))
    
for i in range(5):
    print(
