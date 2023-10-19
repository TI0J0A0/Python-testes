import math

def valor_final(produto, porcentagem):
    return produto - (produto * porcentagem /100)

def main():
    produto = float(input('Qual o valor do produto: ').replace(',', '.'))
    porcentagem = float(input('Qual o valor do desconto: ').replace(',', '.'))
    resultado = valor_final(produto, porcentagem)
    print(f"Valor final: {resultado}")

if __name__ == "__main__":          
    main()
#-------------> A linha if __name__ == "__main__": é usada para determinar se um módulo Python está sendo executado como um programa principal ou se está sendo importado como um módulo em outro script. 
# O código dentro deste bloco será executado apenas se o módulo estiver sendo executado diretamente como um programa, 
# permitindo que você crie módulos reutilizáveis que também podem ser executados independentemente.