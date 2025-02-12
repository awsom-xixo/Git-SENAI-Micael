frase = str(input('Escreva alguma frase, palavra... : '))
split = frase.split()
join = "".join(split)

polindromo = join[::-1]

if join == polindromo:
    print(f'"{frase}" é um palíndromo')
else:
    print(f'"{frase}" não é um palíndromo')