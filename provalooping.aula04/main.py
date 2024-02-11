senha_cadastrada = "2024"
tentativas = 3

for tentativa in range(tentativas):
    senha = input("Digite a senha: ")

    if senha == senha_cadastrada:
        print("Bem-vindo.")
        break
    else:
        tentativas_restantes = tentativas - (tentativa + 1)
        print(f"Senha incorreta. Tentativas restantes: {tentativas_restantes}")

        if tentativas_restantes == 0:
            print("Telefone bloqueado.")
            break