
import requests 
import json
import time

print("CONSULTA DE CEP")
print("===============")
cep = input('Digite o CEP para consulta: ')
requests = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
requests = requests.json()
cep1 = requests['cep']
logradouro = requests['logradouro']
complemento = requests['complemento']
bairro = requests['bairro']
localidade = requests['localidade']
uf = requests['uf']
ibge = requests['ibge']
gia = requests['gia']
ddd = requests['ddd']
siafi = requests['siafi']
print()
print('CEP:',cep1)
print('Lougradouro:',logradouro)
print('Complemento',complemento)
print('Bairro:',bairro)
print('Localidade:',localidade)
print('UF:',uf)
print('IBGE:',ibge)
print('GIA:',gia)
print('DDD:',ddd)
print('SIAFI:',siafi)
print()
print('Consulta realizada com sucesso!')
print('===============================')
print('BY: GALAXY and RICK')
print('GitHub: RickMzy')
exit()      



