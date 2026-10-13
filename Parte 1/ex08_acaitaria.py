# 8. Faça um programa para calcular o total de uma venda de açaí a partir das quantidades compradas para cada tamanho: pequeno, médio e grande,
# sabendo que o valor do açaí é R$ 13,50, R$ 15,00 e R$ 17,50 respectivamente. O programa também deve receber o valor do cupom de desconto em porcentagem.
print("--- Venda de Açaí ---")
pequeno = int(input("Digite a quantidade de açaí pequeno: "))
medio = int(input("Digite a quantidade de açaí médio: "))
grande = int(input("Digite a quantidade de açaí grande: "))
desconto = float(input("Digite a porcentagem de desconto: "))

valor_total = (pequeno * 13.50) + (medio * 15.00) + (grande * 17.50)
valor_desconto = valor_total * desconto / 100
valor_final = valor_total - valor_desconto

print("\n--- Resultado ---")
print(f"Açaí pequeno: {pequeno}")
print(f"Açaí médio: {medio}")
print(f"Açaí grande: {grande}")
print(f"Valor total: R${valor_total:.2f}")
print(f"Desconto: {desconto:.2f}%")
print(f"Valor final: R${valor_final:.2f}")