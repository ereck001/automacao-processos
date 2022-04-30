#!/usr/bin/python3

import paramiko

ssh = paramiko.SSHClient()

#ssh.load_host_keys('~/.ssh/known_hosts')
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for loja in range(167,185,+1):
        print('Loja ', loja)
        try:
            for balcao in range(1,8,+1):
                try:
                    ssh.connect(hostname='192.168.{}.{}'.format(loja, balcao), username='caixa', password='*****', timeout=8)
                    ssh.exec_command('cd')
                    ssh.exec_command('mkdir teste{}'.format(balcao))
                    print(balcao)
                except paramiko.ssh_exception.NoValidConnectionsError as e:
                    print('Host inacessível')
        except paramiko.ssh_exception.NoValidConnectionsError as e:
            print('Host inacessível')
ssh.close()
