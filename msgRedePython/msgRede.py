from socket import socket
import paramiko

backGround = "https://pmpfarmacias.com.br/wp-content/uploads/2021/03/empty-save-texture-room-light.jpg"
idPagina = 'corpo'
logo = "http://links.precomaispopular.com.br/logo_pmp.png"
funcao = "telaFechar()"

def msgTodaRede():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    user = 'operador'
    password = '9658213'
    mensagem = input('Informe a mensagem:\n')

    for loja in range(70,202,+1):
            print('Loja ', loja)
            try:
                for balcao in range(1,3,+1):
                    try:
                        ssh.connect(hostname='192.168.{}.{}'.format(loja, balcao), username=user, password=password, timeout=4)
                        #Comandos a serem executados
                        ssh.exec_command('mkdir msg')

                        ssh.exec_command('echo "<!DOCTYPE html> <style>    body{   padding: 0;   margin:0;   font-family: sans-serif;   height: 1000px;   width: 100%;    background-image: url(' + backGround + ');   } " > msg/msg.html ')
                        ssh.exec_command('echo "   main{  width: 100%;  height: 70%;    display:flex;  flex-direction: column; align-items: center;   justify-content: space-around;  } " >> msg/msg.html ')
                        ssh.exec_command('echo "p{  font-weight: bold;   font-size: 80px;  }  button{  border: NONE;   height: 60px;   width: 220px;   font-size: 40px;   border-radius: 0.2em;    box-shadow: 0 0 1px #000; }   button:hover{    background-color: rgb(121, 121, 121);   color: white;    }  </style>" >> msg/msg.html ')
                        ssh.exec_command('echo " <title>Mensagem TI</title> </head> <body> <main id = ' + idPagina + '> <figure>  <img src=' + logo + '>  </figure> <p>   ' + mensagem + '    </p>  <button onclick=' + funcao + '> FECHAR </button>  </main>  </body> <script>  function telaFechar(){  window.close()} </script> </html>" >> msg/msg.html ')

                        ssh.exec_command('export DISPLAY=:0.0 ; firefox ~/msg/msg.html')
                        print(balcao)
                    except paramiko.ssh_exception.NoValidConnectionsError as e:
                        print('Host inacessível')
                    except socket.timeout as e:
                        print('Host inacessível')
            except paramiko.ssh_exception.NoValidConnectionsError as e:
                print('Host inacessível')
            
    ssh.close()
