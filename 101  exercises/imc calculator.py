print("Olá, tudo bem?\nSeja bem-vindo à calculadora de IMC:\n")
nome = input("Por favor, nos informe seu nome:\n")
print(f"Obrigado, {nome}. Agora, por favor, nos informe sua idade:")
idade = int(input())
print(f"Obrigado, {nome}. Agora, precisaremos do seu peso (em kg) para ajudar\na encontrar o IMC ideal para você:")
peso = float(input()) 
altura_str = input("Agora, nos informe sua altura\n ")
altura_str = altura_str.replace(',', '.')  # Substitui ',' por '.' se houver
altura = float(altura_str)  # Converte a altura em float

# Calcula o IMC
imc = peso / (altura ** 2)

# Classifica o IMC
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Peso ideal")
elif 25 <= imc <= 29.9:
    print("Levemente acima do peso")
elif 30 <= imc <= 34.9:
    print("Obesidade grau I")
elif 35 <= imc <= 39.9:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")

# Exibe o valor do IMC
print(f"Seu IMC é: {imc:.2f}")


