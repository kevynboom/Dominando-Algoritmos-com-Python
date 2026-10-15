print("--- Calculadora de IMC ---")
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura * altura)

print("\n--- Resultado ---")
print(f"Peso: {peso:.2f} kg")
print(f"Altura: {altura:.2f} m")
print(f"IMC: {imc:.2f}")