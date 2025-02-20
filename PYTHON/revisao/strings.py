def manipulacao_strings():
    texto = "  Python é incrível!  "

    # Remover espaços extras no início e no fim
    texto_limpo = texto.strip()
    print(f"Texto limpo: '{texto_limpo}'")

    # Deixar tudo maiúsculo
    maiusculo = texto_limpo.upper()
    print(f"Maiúsculo: {maiusculo}")

    # Deixar tudo minúsculo
    minusculo = texto_limpo.lower()
    print(f"Minúsculo: {minusculo}")

    # Capitalizar a primeira letra
    capitalizado = texto_limpo.capitalize()
    print(f"Capitalizado: {capitalizado}")

    # Trocar palavras
    substituido = texto_limpo.replace("Python", "Programar")
    print(f"Substituído: {substituido}")

    # Contar quantas vezes uma palavra aparece
    contagem = texto_limpo.count("é")
    print(f"Quantidade de 'é': {contagem}")

    # Quebrar a string em uma lista de palavras
    palavras = texto_limpo.split()
    print(f"Lista de palavras: {palavras}")

    # Juntar palavras com um separador
    texto_junto = "-".join(palavras)
    print(f"Texto com '-': {texto_junto}")

    # Verificar se começa com determinada palavra
    comeca_com = texto_limpo.startswith("Python")
    print(f"Começa com 'Python'? {comeca_com}")

    # Verificar se termina com determinada palavra
    termina_com = texto_limpo.endswith("incrível!")
    print(f"Termina com 'incrível!'? {termina_com}")

    # Encontrar a posição de uma palavra
    posicao = texto_limpo.find("é")
    print(f"Posição de 'é': {posicao}")

manipulacao_strings()
