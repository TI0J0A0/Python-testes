#### meu codigo######
l = float(input('Qual a largura da parede(mestros)\n'))
h = float(input('Qual a altura da parede(metros)\n'))
r = float(input('Qual o rendimento da Tinta(m²/L)\n'))
area = l*h
tinta = area*r 
print ('Sua parede tem uma dimensao de {} por {} e sua área é de {}m'.format(l,h,area))
print ('Para pintar a parede voce precisará de {}L de tinta.'.format(tinta))






################################ codigo melhorado pelo GPT ########################################

#def calcular_area(largura, altura):
    #return largura * altura

#def calcular_tinta(area, rendimento_tinta):
    #return area / rendimento_tinta

#def main():
    #largura = float(input('Qual a largura da parede (metros): '))
    #altura = float(input('Qual a altura da parede (metros): '))
    #rendimento_tinta = float(input('Qual o rendimento da tinta (m²/L): '))

    #area = calcular_area(largura, altura)
    #tinta_necessaria = calcular_tinta(area, rendimento_tinta)

    #print(f'Sua parede tem uma dimensão de {largura}m x {altura}m e sua área é de {area}m².')
    #print(f'Para pintar a parede você precisará de {tinta_necessaria:.2f} litros de tinta.')

#if __name__ == '__main__':
    #main()
    
    #Em resumo, a construção if __name__ == '__main__': permite que você tenha um ponto de entrada para o seu programa. 
    # O código dentro desse bloco será executado apenas quando o arquivo Python for executado diretamente, 
    # e não quando ele for importado como um módulo em outro programa. Isso ajuda a modularizar e organizar o código, tornando-o mais reutilizável e legível.
    
    ########################################                 ########################################