import requests
import urllib.parse

dns = "ec2-3-89-138-23.compute-1.amazonaws.com"
url_cliente = "http://%s/cliente/"%dns
url_pedido = "http://%s/pedido/"%dns

def getDados(url):
    return requests.get(url).json()

nome = input("Qual o nome do cliente ?")
url_cliente += urllib.parse.quote(nome)
id_cliente = getDados(url_cliente)[0]["CustomerId"]

url_pedido += urllib.parse.quote(str(id_cliente))
pedidos = getDados(url_pedido)

total = 0
for pedido in pedidos:
    total += pedido["total"]
print("Total gasto por %s: %.2f"%(nome,total))


    
