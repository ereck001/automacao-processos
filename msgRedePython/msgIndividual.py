
import paramiko

def msgInd(loja):
    ssh = paramiko.SSHClient()
    maq = input('Informe o último campo do IP:\n')
    host = '192.168.{}.{}'.format(loja, maq)
    if(maq < 10 ):
        user = 'operador'
        password = '68594'
    else:
        user = 'vendedor'
        password = '68594'
    backGround = "https://pmpfarmacias.com.br/wp-content/uploads/2021/03/empty-save-texture-room-light.jpg"
    idPagina = 'corpo'
    logo = "http://links.precomaispopular.com.br/logo_pmp.png"
    funcao = "telaFechar()"
    #mensagem = 'FAVOR LIGAR PARA O TI'

    mensagem = input("Digite a mensagem:\n")

    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname=host, username=user, password=password, timeout=3)

    ssh.exec_command('mkdir msg')

    ssh.exec_command('echo "<!DOCTYPE html> <style>    body{   padding: 0;   margin:0;   font-family: sans-serif;   height: 1000px;   width: 100%;    background-image: url('+ backGround +');   } " > msg/msg.html ')
    ssh.exec_command('echo "   main{  width: 100%;  height: 70%;    display:flex;  flex-direction: column; align-items: center;   justify-content: space-around;  } " >> msg/msg.html ')
    ssh.exec_command('echo "p{  font-weight: bold;   font-size: 80px;  }  button{  border: NONE;   height: 60px;   width: 220px;   font-size: 40px;   border-radius: 0.2em;    box-shadow: 0 0 1px #000; }   button:hover{    background-color: rgb(121, 121, 121);   color: white;    }  </style>" >> msg/msg.html ')
    ssh.exec_command('echo " <title>Mensagem TI</title> </head> <body> <main id = '+ idPagina +'> <figure>  <img src=' + logo +'>  </figure> <p>   '+ mensagem +'    </p>  <button onclick='+ funcao +'> FECHAR </button>  </main>  </body> <script>  function telaFechar(){  window.close()} </script> </html>" >> msg/msg.html ')


    ssh.exec_command('export DISPLAY=:0.0 ; firefox ~/msg/msg.html')
    ssh.close()
