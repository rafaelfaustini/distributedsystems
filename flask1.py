import mysql.connector
from flask import Flask
import json
from flask_jsonpify import jsonify

app = Flask(__name__) # __name__ variável do sistema que indica o nome do módulo ou 'main'

@app.route("/cliente/<country>")
def imprime_cliente (country=None):
        conn = mysql.connector.connect (host='sistemasdistribuidos.c9aa3shrbfs3.us-east-1.rds.amazonaws.com', user='admin',
passwd='mariojoao',port='3306', database='chinook')
        cursor = conn.cursor()
        qstr = "select * from customers where Country=\'"+country+"\'"
        print (qstr)
        query = cursor.execute(qstr)
        row_headers=[x[0] for x in cursor.description]
        print (row_headers)
        records = cursor.fetchall()
        print (records)
        result = [dict(zip(tuple (row_headers) ,i)) for i in records] #estrutura do json
        print (result)
        jret = jsonify(result)
        print (jret)
        conn.close()
        return jret

app.run(host='0.0.0.0', port='80')

