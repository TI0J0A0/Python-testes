n1 = input('Digite algo: ')

print(f'Qual o tipo primitivo desse valor?? {type(n1)}.')

print(f'É composto de valores imprimiveis? {n1.isprintable()}')
print(f'contem apenas letras ? {n1.isalpha()}')
print(f'Está com apenas letras minusculas? {n1.islower()}')
print(f'É Décimal? {n1.isdecimal()}')
print(f'Está com letras maiusculas? {n1.isupper()}')
print(f'alfanuméricos ? {n1.isalnum()}')
print(f'todos os caracteres sao dígitos numéricos? {n1.isdigit()}')

