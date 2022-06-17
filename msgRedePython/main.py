#
#PROGRAMA PARA MENSAGENS DO SUPORTE TI FARMÁCIAS PMP


from msgIndividual import  msgInd
from msgRede import  msgTodaRede

ctr = 0
res = 'S'
while ctr < 3 and res == 'S':
    ctr = int(input('Para mensagem individual digite 1:\nPara mensagem de rede digite 2:\n'))
    if ctr == 1:
        msgInd(input('Informe o número da loja:\n'))
    elif ctr == 2:
        msgTodaRede()
    else:
        print('Opção inválida!\n ')

    res = input("Para continuar digite S ").upper()
