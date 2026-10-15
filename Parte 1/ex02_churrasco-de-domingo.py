print("--- Churrasco de Domingo ---")
pessoas = int(input("Digite a quantidade de pessoas: "))

carne_por_pessoa = 0.300
linguica_por_pessoa = 0.200
frango_por_pessoa = 0.150

preco_carne = 50.00
preco_linguica = 28.00
preco_frango = 22.00

carne_total = carne_por_pessoa * pessoas
linguica_total = linguica_por_pessoa * pessoas
frango_total = frango_por_pessoa * pessoas

custo_carne = carne_total * preco_carne
custo_linguica = linguica_total * preco_linguica
custo_frango = frango_total * preco_frango

custo_total = custo_carne + custo_linguica + custo_frango
valor_por_pessoa = custo_total / pessoas

print("\n--- Resultado ---")
print(f"Carne: {carne_total:.2f} kg - R${custo_carne:.2f}")
print(f"Linguiça: {linguica_total:.2f} kg - R${custo_linguica:.2f}")
print(f"Frango: {frango_total:.2f} kg - R${custo_frango:.2f}")
print(f"\nCusto total: R${custo_total:.2f}")
print(f"Cada pessoa deve pagar: R${valor_por_pessoa:.2f}")