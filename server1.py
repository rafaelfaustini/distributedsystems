from socket import *

s = socket ()

host = "0.0.0.0"
porta = 8752
s.bind ((host, porta))
s.listen (10)

while True:
        (conn, cliente) = s.accept ()

        print ("Conectado com "+str(cliente))

        while True:
                data = conn.recv (4096)

                if not data:
                        break

                print (str(cliente)+" enviou "+data.decode("utf-8") )

                conn.send (str.encode ("Mensagem: "+data.decode("utf-8") , "UTF-8"))

        print ("Finalizada conexao com "+str(cliente))

        conn.close
