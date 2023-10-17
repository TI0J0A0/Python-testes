# Lista de frutas
frutas_lista = ["açaí", "abacate", "abacaxi", "abiu", "abricó", "ameixa", "amora", "ananás", "araçá", "araticum",
               "ata", "bacaba", "bacuri", "banana", "cabeludinha", "cacau", "cagaita", "cajá", "caju", "cajuí",
               "cajuína", "calabaça", "calamansi", "calamondin", "carambola", "cereja", "cereja-do-rio-grande",
               "cereja-europeia", "cereja-japonesa", "cereja-negra", "cereja-ornamental", "cereja-rosa",
               "cereja-silvestre", "cereja-umbu", "cereja-yuzu", "cidra", "cipó-azougue", "coco", "coquinho-azedo",
               "coquinho-babaçu", "coquinho-cabacinha", "coquinho-cumari", "coquinho-jerivá", "coquinho-licuri",
               "coquinho-macajá", "coquinho-pequizeiro", "coquinho-tucumã", "cupuaçu", "damasco", "dovyalis",
               "durião", "embaúba", "figo", "framboesa", "fruta-pão", "frutas do cerrado", "fruta-do-conde",
               "goiaba", "graviola", "groselha", "guabiroba", "guaraná", "ingá", "jabuticaba", "jaca", "jambo",
               "jambolão", "jatobá", "jenipapo", "kiwi", "laranja", "lichia", "limão", "maçã", "mamão", "manga",
               "mangaba", "maracujá"]

# lista vazia 
frutas_digitadas = []

print("Olá, digite o nome de frutas que você conhece aqui ou digite 'sair' para sair do jogo.")

while True:
    fruta = input("Digite o nome de uma fruta: ")
    if fruta == "sair":
        break 
    
    if fruta in frutas_lista:
        if fruta not in frutas_digitadas:
            frutas_digitadas.append(fruta)
            print(f"{fruta} foi adicionada à lista de frutas digitadas.")
        else:
            print(f"{fruta} já foi digitada.")
    else:
        print(f"{fruta} não é uma fruta válida.")

# Verifica se todas as frutas da lista foram digitadas
if set(frutas_lista) == set(frutas_digitadas):
    print("Parabéns! Você digitou todas as frutas da lista.")
else:
    print("Você saiu do jogo ou não digitou todas as frutas da lista.")
