# valida o número do cpf com pontos e hífens
import re
cpf1 = str(input('Entre com o número do CPF, com pontos e hífens: \n'))
if re.search('\d{3}.\d{3}.\d{3}-\d{2}', cpf1):
    print('Número CPF validado')
else:
    print('Número CPF fora do padrão')
cpf2 = str(input('Entre com o número do CPF, com pontos e hífen: (\d{3}\d{3}\d{3}-\d{2}) \n'))
if re.search('\d{3}\d{3}\d{3}-\d{2}', cpf2):
    print('Número CPF validado')
else:
    print('Número CPF fora do padrão')
cpf3 = str(input('Entre com o número do CPF, com pontos e hífen: (\d{11})\n'))
if re.search('\d{11}', cpf3):
    print('Número CPF validado')
else:
    print('Número CPF fora do padrão')
input('Pressione ENTER para sair...')
          
