import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    tentativa = int(input("Adivinhe o número entre 1 e 100: "))
    tentativas += 1

    if tentativa < numero_secreto:
        print("Tente um número maior.")
    elif tentativa > numero_secreto:
        print("Tente um número menor.")
    else:
        print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
        break

jogar_novamente = input("Deseja jogar novamente? (s/n): ")

if jogar_novamente.lower() != "s":
    print("Obrigado por jogar. Até a próxima!")
