print("--- Performance do Piloto ---")
tamanho_pista = float(input("Digite o tamanho da pista em metros: "))
quantidade_voltas = int(input("Digite a quantidade de voltas: "))
tempo_primeira_volta = float(input("Digite o tempo da primeira volta em segundos: "))

distancia_total = (tamanho_pista * quantidade_voltas) / 1000
tempo_total = (tempo_primeira_volta * quantidade_voltas) / 60

print("\n--- Resultado ---")
print(f"Distância total da corrida: {distancia_total:.2f} km")
print(f"Previsão de tempo: {tempo_total:.2f} minutos")