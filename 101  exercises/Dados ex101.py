import random

def rolar_dado():
    return random.randint(1,6)

resultado  = rolar_dado()
print(f"Voce tirou {resultado}")


#`---------------------------`
#import random

#lados_do_dado = [1, 2, 3, 4, 5, 6]
#def rolar_dado():
#return random.choice(lados_do_dado)
#resultado = rolar_dado()
#print(f"O dado rolou e o resultado foi: {resultado}")

#`---------------------------`
#import random

#def rolar_dado(lados=6):
    #return random.randint(1, lados)

#lados_personalizados = 8  # Pode ser qualquer número de lados desejado
#resultado = rolar_dado(lados_personalizados)
#print(f"O dado rolou e o resultado foi: {resultado}")

#`---------------------------`

#import numpy as np

#ef rolar_dado():
#   return np.random.choice([1, 2, 3, 4, 5, 6])
#
#resultado = rolar_dado()
#print(f"O dado rolou e o resultado foi: {resultado}")