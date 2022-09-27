# Instalação do curl

import paramiko
import time
import socket
from scp import SCPClient


client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

command1 = "sudo su -c 'cp -r /home/caixa/Downloads/sources.list /etc/apt/sources.list'"
command2 = "sudo su -c 'apt update'"
command3 = "sudo su -c 'apt upgrade  -y'"
command4 = "sudo su -c 'apt install libcurl3-gnutls  -y'"
command5 = "sudo su -c 'apt install curl -y'"

lojaBegin = input("Informe qual a loja vai começar:\n")

lojaEnd = input("Informe a última loja:\n")

def sshRoot(command):

    client.get_transport()

    stdin, stdout, stderr = client.exec_command(command=command, get_pty=True)
    print("Comando enviado")
    time.sleep(0.5)
    stdin.write("pmp\n")
    print("Senha enviada")
    stdin.flush()
    print("Executando o comando...")

    if stderr.channel.recv_exit_status() != 0:

        print("Erro na execução do comando!\n")
    else:

        print('Comando OK!\n')
        #print("The following output was produced: \n{}".format(stdout.readlines())) # retorna saída no terminal

for loja in range(int(lojaBegin), int(lojaEnd) + 1):

    print('Loja ', loja)

    for balcao in range(1, 5):

        erro = False

        try:

            client.connect(hostname='192.168.{}.{}'.format(loja, balcao), username='user', password='password', timeout=2)

            # Arquivos a serem copiados

            print("copiando...\n Balcão {}".format(balcao))

            with SCPClient(client.get_transport()) as scp:

                scp.put('/home/batman/sources.list', '/home/caixa/Downloads')

            print(' OK!')



        except paramiko.ssh_exception.NoValidConnectionsError as e:

            print('Host inacessível')
            erro = True

        except socket.timeout as e:

            print('Host inacessível')
            erro = True

        if not erro:

            sshRoot(command1)
            sshRoot(command2)
            sshRoot(command3)
            sshRoot(command4)
            sshRoot(command5)

print('Operação concluída!')


client.close()
