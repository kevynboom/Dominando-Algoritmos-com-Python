# 5. Faça um programa para calcular o valor final de uma compra, a partir do valor da compra e do cupom de desconto. O cupom diz a porcentagem do desconto.
print("--- Calculadora de Desconto ---")
valor_compra = float(input("Digite o valor da compra: R$"))
desconto = float(input("Digite a porcentagem de desconto: "))

valor_desconto = valor_compra * desconto / 100
valor_final = valor_compra - valor_desconto

print("\n--- Resultado ---")
print(f"Valor da compra: R${valor_compra:.2f}")
print(f"Desconto: {desconto:.2f}%")
print(f"Valor do desconto: R${valor_desconto:.2f}")
print(f"Valor final: R${valor_final:.2f}")