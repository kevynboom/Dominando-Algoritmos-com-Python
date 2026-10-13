# 1. Faça um programa que apresente um estudante universitário considerando seu nome, curso que estuda, semestre atual e seu hobby favorito.
nome = input("Digite o seu nome: ")
curso = input("Digite qual o curso que você está fazendo: ")
semestre = int(input("Digite apenas o número correspondente ao semestre em que você está no momento: "))
hobby = input("Digite o seu hobby favorito: ")

print("\n--- Dados do Aluno ---")
print(f"Nome: {nome}")
print(f"Curso: {curso}")
print(f"Semestre atual: {semestre}° Semestre")
print(f"Hobby: {hobby}")