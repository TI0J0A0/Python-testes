X = int(input('Digite um número para ver sua tabuada: '))

print('------------------')
for Y in range(1, 11):
    resultado = X * Y
    print(f'{X} x {Y} = {resultado}')
print('------------------')
