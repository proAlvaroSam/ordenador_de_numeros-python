def ordenar_numero(numero):
    # Converter o número para string para manipulação
    numero_str = str(numero)

    # Verificar se o número é decimal
    if '.' in numero_str:
        # Manipular a parte inteira e decimal separadamente
        parte_inteira, parte_decimal = numero_str.split('.')

        # Ordenar a parte inteira do menor para o maior e do maior para o menor
        parte_inteira_ordenada_menor_maior = ''.join(sorted(parte_inteira))
        parte_inteira_ordenada_maior_menor = ''.join(sorted(parte_inteira, reverse=True))

        # Ordenar a parte decimal do menor para o maior e do maior para o menor
        parte_decimal_ordenada_menor_maior = ''.join(sorted(parte_decimal))
        parte_decimal_ordenada_maior_menor = ''.join(sorted(parte_decimal, reverse=True))

        # Combinar partes ordenadas
        numero_ordenado_menor = parte_inteira_ordenada_menor_maior + '.' + parte_decimal_ordenada_menor_maior
        numero_ordenado_maior = parte_inteira_ordenada_maior_menor + '.' + parte_decimal_ordenada_maior_menor
    else:
        # Ordenar os dígitos do menor para o maior e do maior para o menor (números inteiros)
        numero_ordenado_str_menor_maior = ''.join(sorted(numero_str))
        numero_ordenado_str_maior_menor = ''.join(sorted(numero_str, reverse=True))

        # A string ordenada já representa o número final
        numero_ordenado_menor = numero_ordenado_str_menor_maior
        numero_ordenado_maior = numero_ordenado_str_maior_menor

    return numero_ordenado_menor, numero_ordenado_maior

# Testar a função
numero_escolhido = input('Escolha um número inteiro ou decimal com mais de um dígito: ')
numero_ordenado_menor, numero_ordenado_maior = ordenar_numero(numero_escolhido)

# Exibir os resultados ordenados
print(f'Seu número ordenado do menor para o maior fica assim: {numero_ordenado_menor}')
print(f'Seu número ordenado do maior para o menor fica assim: {numero_ordenado_maior}')

# Com os números quebrados, ele vai refazer a ordem e começar outra depois da vírgula