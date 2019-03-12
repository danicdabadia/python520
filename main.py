# Tipos primitivos de variáveis

inteiro = 1
ponto_flutuante = 1.5
text = 'Lucas Ricciardi de Salles'

lista = []
tupla = ()
dicionario = {}

usuarios = [
  
  {
  'id': 1,
  'nome': 'Lucas',
  'idade': 25,
  },

  {
    'id': 2,
    'nome': 'Claudia',
    'idade': 20
  },

  {
    'id': 3,
    'nome': 'Siclano',
    'idade': 10
  },

  {
    'id': 4,
    'nome': 'Matusalem',
    'idade': 3129863981263981263981263
  },
  
]

lucas = usuarios[0]
print(lucas)
# print(usuarios)

exit()

# Exercício 2 (Não pode colocar as operações na mesma linha !!!)
# Peça para que o usuário digite um número
# Se o número for maior do que 50:
#   1.1 - Multiplique o número por 2
#   1.2 - Eleve o número ao quadrado
#   1.3 - Some 45 ao número
# Se não:
#   2.1 - Multiplique o número por 5
#   2.2 - Some 423789 ao número
# Depois disso tudo, imprima o resultado

numero = int(input('Digite um número: '))

if numero > 50:
  numero = numero * 2
  numero = numero ** 2  # numero * numero
  numero += 45          # numero = numero + 45
  if numero < 100:
    numero += 12381263
else:
  numero *= 5
  numero += 423789

print(numero)

exit()

# exercício
# Escrever um programa que:
# - 1: Pede que o usuário digite um número
# - 2: Vê se o número é maior do que a sua idade
#    - 2.1: Se sim, imprima: "Você é mais velho do que eu!"
#    - 2.2: Se não, imprima: "Sou mais velho do que você"
#    - 2.3 (desafio): Se for igual, imprima "Temos a mesma idade"


# daqui para baixo, ignorem !

# DICA: Converter string para número

string = '153267153672153671'
numero = int(string)
print(numero) # isso aqui é um número, pode usar >, < e etc.

numero = input('Digite um número, por favor: ')

minha_idade = 25

if numero > minha_idade:
  print('Você é mais velho do que eu!')
elif numero < minha_idade:
  print('Eu sou mais velho do que você !')
elif numero == minha_idade:
  print('Você tem a minha idade')
