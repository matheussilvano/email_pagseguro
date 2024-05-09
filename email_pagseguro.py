import os
from time import sleep
print('==== GERADOR DE RESPOSTAS PAGSEGURO ====')
sleep(1)
razao_social = input('Insira a razão social: ')
cnpj = input('Insira o CNPJ: ')
id = input('Insira o DsName do cliente: ')
caixa_postal = input('Insira o id caixa postal do cliente: ')
os.system('cls')
print(f'''
Prezados, bom dia!

Referente aos DSNames desse cliente, segue abaixo:

Razão Social: {razao_social}
CNPJ: {cnpj}
ID: {id}

RET.ANT.{id}XXX.680.{caixa_postal}  
RET.FIN.{id}XXX.680.{caixa_postal}   
RET.TRA.{id}XXX.680.{caixa_postal}  ''')
terminar = input('Digite enter para sair: ')
