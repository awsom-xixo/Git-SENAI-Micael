import os
os.system ('clear')

frase = str(input('Escreva uma frase para contar suas vogais:')).lower()

vogais = ['a', 'e', 'i', 'o', 'u']

for vogal in vogais:
    print(f'{vogal}: {frase.count(vogal)}')