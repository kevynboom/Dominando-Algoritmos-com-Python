# 4. Faça um programa para simular a conversão de um valor em real para dólar. Considere a cotação do dólar em R$ 5,42.
cotacao = 5.42

print("--- Conversor de Real para Dólar ---")
valor_reais = float(input("Digite o valor em reais: R$"))

valor_dolar = valor_reais / cotacao

print("\n--- Resultado ---")
print(f"Valor em reais: R${valor_reais:.2f}")
print(f"Valor em dólares: US${valor_dolar:.2f}")