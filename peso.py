# Exercício Python 29: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

peso1 = []

print('Descubra o maior e o menor peso de uma lista')
for i in range(0,5):
    peso2 = float(input(f'Digite o {i+1}° peso: '))
    peso1.append(peso2)
maior = max(peso1)
menor = min(peso1)

print(f'O maior peso da lista é {maior}\nO menor peso da lista é {menor}')