import socket

import pyodbc
# Script de automatização de query para os servidores

server = ''
database = 'LOJA'
username = 'sa'
password = 'mkt$Admin'



for i in range(70,202):
    server= '192.168.{}.253'.format(i)
    print('Executando na loja {} '.format(i))
    try:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password, timeout=1)
        cursor = cnxn.cursor()

        # Query a ser executada
        cursor.execute("UPDATE PARAMETROS SET OBRIGAR_LOTE_VALIDADE_PRE_VENCIDO = 'S';")
        cnxn.commit()
        print('OK\n')
    except pyodbc.OperationalError as e:
        print(e)



