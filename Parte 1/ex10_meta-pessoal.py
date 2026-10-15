print("--- Meta Pessoal ---")
descricao_meta = input("Digite a descrição da meta: ")
valor_meta = float(input("Digite o valor necessário para atingir a meta: R$"))
salario = float(input("Digite o seu salário mensal: R$"))
despesas = float(input("Digite o total das despesas mensais: R$"))

valor_restante = salario - despesas
economia_fixa = valor_restante * 30 / 100
valor_mensal = valor_restante - economia_fixa
tempo = valor_meta / valor_mensal

print("\n--- Resultado ---")
print(f"Meta: {descricao_meta}")
print(f"Valor da meta: R${valor_meta:.2f}")
print(f"Valor reservado para economia: R${economia_fixa:.2f}")
print(f"Valor destinado à meta por mês: R${valor_mensal:.2f}")
print(f"Tempo para alcançar a meta: {tempo:.2f} meses")