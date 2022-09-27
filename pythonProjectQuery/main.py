import socket

import pyodbc
# Script de automatização de query para os pdvs


server = ''
database = 'PDV'
username = 'user'
password = 'password'

for loja in range(01, 201):

    print('Executando na loja {} '.format(loja))

    for pdv in range(21,24):
        server = '192.168.{}.{}'.format(loja, pdv)
        print('Executando no PDV {} '.format(pdv))

        try:
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password, timeout=1)
            cursor = cnxn.cursor()
            # Query a ser executada
            cursor.execute("UPDATE PARAMETROS SET OBRIGAR_LOTE_VALIDADE_PRE_VENCIDO = 'S';")
            cnxn.commit()
            print('OK\n')
        except pyodbc.ProgrammingError:
            print('Loja não existe ou está desconectada.')
        except pyodbc.OperationalError:
            print('Loja não existe ou está desconectada.')