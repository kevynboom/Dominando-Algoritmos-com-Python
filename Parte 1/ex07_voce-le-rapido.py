# 7. Faça um programa que calcule o tempo que um livro será lido por uma pessoa a partir do nome do livro, do total de páginas e do tempo em segundos de leitura por página.
print("--- Tempo de Leitura ---")
nome_livro = input("Digite o nome do livro: ")
paginas = int(input("Digite o total de páginas: "))
segundos_por_pagina = int(input("Digite o tempo em segundos para ler cada página: "))

tempo_total = paginas * segundos_por_pagina

print("\n--- Resultado ---")
print(f"Livro: {nome_livro}")
print(f"Total de páginas: {paginas}")
print(f"Tempo por página: {segundos_por_pagina} segundos")
print(f"Tempo total de leitura: {tempo_total} segundos")