# 3. Faça um programa que calcule a média de um aluno, a partir de três notas informadas pelo usuário.
print("--- Média do Aluno ---")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("\n--- Resultado ---")
print(f"Média do aluno: {media:.2f}")