import mysql.connector
from flask import Flask
import json
from flask_jsonpify import jsonify

app = Flask(__name__) # __name__ variável do sistema que indica o nome do módulo ou 'main'

host = "sistemasdistribuidos.czeko0kluoj5.us-east-1.rds.amazonaws.com"
user = 'admin'
senha = ''
porta = '3306'
banco = 'chinook'

@app.route("/cliente/<nome>")
def imprime_cliente (nome=None):
    conn = mysql.connector.connect (host=host, user=user, passwd=senha, port=porta, database=banco)
    cursor = conn.cursor()
    qstr = "select CustomerId from customers where FirstName=\'"+nome+"\'"
    print (qstr)
    query = cursor.execute(qstr)
    row_headers=[x[0] for x in cursor.description]
    records = cursor.fetchall()
    print (records)
    result = [dict(zip(tuple (row_headers) ,i)) for i in records]
    print (result)
    jret = jsonify(result)
    print (jret)
    conn.close()
    return jret

@app.route("/pedido/<id>")
def imprime_pedidos (id=None):
    conn = mysql.connector.connect (host=host, user=user, passwd=senha, port=porta, database=banco)
    cursor = conn.cursor()
    qstr = "select total from invoices where CustomerId=%s"%id
    print (qstr)
    query = cursor.execute(qstr)
    row_headers=[x[0] for x in cursor.description]
    records = cursor.fetchall()
    print (records)
    j=0
    for i in records:
        records[j] = [float(i[0])]
        j+=1
    result = [dict(zip(tuple (row_headers) , i)) for i in records]
    print (result)
    jret = jsonify(result)
    print (jret)
    conn.close()
    return jret


app.run(host='0.0.0.0', port='80')

