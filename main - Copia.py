nome = 'gabriel vendiciano barbosa'
fatiamento = nome[:]
nome = 'luis siqueira'
print(fatiamento)
print()
print(nome)
print(fatiamento[10:2:-1])
ao_contrario = fatiamento[::-1]
print(ao_contrario)


frase ="""
 pista pis fez pisto pis
 pusta posta que gosta de torta
"""

texto = "Aprender Python é incrível"

ex01 = texto[9:15]

numeros = [10, 20, 30, 40, 50, 60]

ex02 = numeros[0:3]

arquivo = "imagem_ferias.png"

ex03 = arquivo[-4:]

alfabeto = "abcdefghijklmnopqrstuvwxyz"

ex04 = alfabeto[1:1:2]

lista = [1, 2, 3, 4, 5]

ex05 = lista[::-1]

semana = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"]

ex06 = semana[1:6]

data = "2025-10-25"
separado = data.split('-')
ano = separado[0]
mes = separado[1]
dia = separado[2]

print(dia,mes,ano)