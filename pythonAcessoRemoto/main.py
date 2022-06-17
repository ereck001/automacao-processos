
#Criação de pastas e arquivos na rede da PMP

import socket
import paramiko

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for loja in range(70,202,+1):
        print('Loja ', loja)
        try:
            for balcao in range(1,8,+1):
                try:
                    ssh.connect(hostname='192.168.{}.{}'.format(loja, balcao), username='balcao', password='pmp', timeout= 4)
                    #Comandos a serem executados
                    ssh.exec_command('cd')
                    ssh.exec_command('mkdir teste{}'.format(balcao))
                    ssh.exec_command('echo "teste de string " >> teste{}/novo_teste{}.txt'.format(balcao, balcao))
                    print('Balcão {}'.format(balcao))
                except paramiko.ssh_exception.NoValidConnectionsError as e:
                    print('Host inacessível')
                except socket.timeout as e:
                    print('Host inacessível')

            for caixa in range(1, 4, +1):
                try:
                    ssh.connect(hostname='192.168.{}.{}'.format(loja, caixa +20), username='caixa', password='pmp', timeout=4)
                    # Comandos a serem executados
                    ssh.exec_command('cd')
                    ssh.exec_command('mkdir teste{}'.format(caixa))
                    ssh.exec_command('echo "teste de string " >> teste{}/novo_teste{}.txt'.format(caixa, caixa))
                    print('Caixa {}'.format(caixa))
                except paramiko.ssh_exception.NoValidConnectionsError as e:
                    print('Host inacessível')
                except socket.timeout as e:
                    print('Host inacessível')

        except paramiko.ssh_exception.NoValidConnectionsError as e:
            print('Host inacessível')
        except:
            print('Host inacessível')
ssh.close()
