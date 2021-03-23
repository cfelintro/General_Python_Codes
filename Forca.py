import random


lista_palavras = ((open('D:\Arquivos\Caio\Arquivos diversos\Trilha da Programacao Python Ocean\Forca\lista_forca.csv','r')).read()).split(', ')
"""

lista_palavras = ['ARARA', 'TARANTULA']     # ---> LISTA PARA TESTES
"""

def novo_jogo():

  palavra_jogo = random.choice(lista_palavras)
  num_caracteres = len(palavra_jogo)
  blank = '_ '
  cont_derrota = 0
  print(f'A palavra é: {num_caracteres * blank}')
  listas = letras_da_palavra(palavra_jogo)  #Popula lista 'lista_letras'
  lista_letra = listas[0]
  lista_resultado = listas[1]
  lista_utilizadas = []
  selecao_letra(cont_derrota, palavra_jogo, lista_letra, lista_resultado, lista_utilizadas)



def selecao_letra(contador,palavra_jogo, lista_letras, lista_resultado, lista_utilizadas):
  cont_derrota = contador
  lista_letra = lista_letras
  lista_resultado = lista_resultado
  lista_index = []
  lista_utilizadas = lista_utilizadas
  print()
  letra = str(input('Escolha uma letra: ')).upper()
  busca = True

  for value in lista_utilizadas:

    if value == letra:
      busca = False

  if busca == False:
    print(f'A letra "{letra.upper()}" já foi utilizada.')
    print('Escolha outra letra.')
    selecao_letra(cont_derrota, palavra_jogo, lista_letra, lista_resultado, lista_utilizadas)

  lista_utilizadas.append(letra)

  if len(letra) > 1 or letra == '':
    print('Este valor não é valido. Digite novamente')
    selecao_letra(cont_derrota, palavra_jogo, lista_letra, lista_resultado, lista_utilizadas)

  else:
    for index in range(len(palavra_jogo)):

      if letra == palavra_jogo[index]:
        lista_index.append(index)
 
    if lista_index == []:
      contador = contador + 1
      cont_derrota = contador
      print(f'Você errou a {contador}ª vez')

      if contador < 6:
        selecao_letra(cont_derrota, palavra_jogo, lista_letra, lista_resultado, lista_utilizadas)

      else:
        print()
        print('O jogo acabou: VOCÊ FOI PARA A FORCA!')
        print(f'A palavra era: {palavra_jogo.upper()}')
        
        nova_execucao()

    else:
      for num in enumerate(lista_index):
        value = num[1]
        lista_resultado[value] = lista_letras[value]

      nome_completo = ''

      for letra in lista_resultado:
        nome_completo = nome_completo +' '+ letra

      if lista_resultado == lista_letras:
        print()
        print(f'A palavra é: {nome_completo}')
        print()
        print(f'PARABÉNS! Você ganhou o jogo!')
        print(f'Você precisou de {contador+1} chances para vencer.')
        print()
        nova_execucao()

      else:  
        print()
        print(f'A palavra é: {nome_completo}')
        selecao_letra(cont_derrota, palavra_jogo, lista_letra, lista_resultado, lista_utilizadas)  



#Adiciona letras da palavra na Lista 'lista_letras'
def letras_da_palavra(palavra_jogo):
  lista_letras = []
  lista_resultado = []

  for index in range(len(palavra_jogo)):
    letra = palavra_jogo[index]
    lista_letras.append(letra)
    lista_resultado.append('_')

  return(lista_letras, lista_resultado)



def nova_execucao():
  print()
  executar_novamente = input('Deseja jogar novamente? (Y/N): ').upper()
  if executar_novamente == 'Y':
    print()
    novo_jogo() #a função principal deve ser substituída nessa linha
  elif executar_novamente == 'N':
    print()
    print('FIM DE JOGO')
    exit()
  else:
    print()
    print('Seleção não é valida')
    nova_execucao()

novo_jogo()
