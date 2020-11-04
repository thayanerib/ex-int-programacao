#agenda = {}
#agenda ["maria"] = 82873
#agenda ["carlos"] = 64820
#print (agenda)

#cadastro = dict()
#cadastro[ 'matrcula' ] = str(input('matricula: '))
#cadastro [aluno] = input ('nome do aluno: ')
#cdastro [nota] = input ('nota do aluno: ')
#print (cadastro)

dados_lista = []
for i in range(1, 5):
  dados = dict()
  dados['aluno'] = input('aluno: ')
  dados['matricula'] =input('matricula: ')
  dados['nota'] = input('nota: ')
  dados_lista.append(dados)
print (dados_lista)

tam = len(dados_lista)

maior_elemento = dados_lista[0]['nota']
posicao_aluno = 0
for i in range(0, tam):
  if maior_elemento < dados_lista[i]['nota']:
    maior_elemento = dados_lista[i]['nota']
    posicao_aluno = i
print(dados_lista[posicao_aluno])
