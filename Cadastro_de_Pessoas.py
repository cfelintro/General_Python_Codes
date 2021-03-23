
#Listas de Dados:
index = [0,]
nomes = ['NOME']
sobrenomes = ['SOBRENOME']
telefones = [000]
cpfs = [00000000000]

#Dicionario de dados:
database = {
    'index':index,
    'nome':nomes,
    'sobrenome':sobrenomes,
    'telefone':telefones,
    'cpf':cpfs
}

#MENU INICIAL - Chama as demais funções ou termina o programa:

def main_menu():
  print()
  selection = str(input('O que deseja fazer? :')).capitalize()
  if selection == 'C' or selection == 'Cadastrar':
    cadastrar()
  elif selection == 'L' or selection == 'Listar':
    listar()
  elif selection == 'R' or selection == 'Remover':
    remover()
  elif selection == 'E' or selection == 'Editar':
    editar()
  elif selection == 'T':
    terminate()
  else:
    print()
    print('Selecao invalida')
    print()
    main_menu()

#FIM DE PROGRAMA
def terminate():
  print('FIM DA EXECUÇÃO')

#FUNÇÃO BUSCA - Utilizada para procurar valores para as funções remover e editar
def busca(nome_busca, sobrenome_busca):
  index_busca = -1

  for numero in index:
    nome = database["nome"][numero-1]
    sobrenome = database["sobrenome"][numero-1]

    if nome == nome_busca and sobrenome == sobrenome_busca:
      index_busca = numero

  return(index_busca)


#FUNÇÃO CADASTRO - Adiciona novos cadastros na base de dados
def cadastrar():

  print('***CADASTRO***')
  print()

  nome = str(input('Nome: ')).upper()
  if nome == 'CANCELAR':
    main_menu()
  else:
    sobrenome = str(input('Sobrenome: ')).upper()
    if sobrenome == 'CANCELAR':
      main_menu()
    else:
      telefone = str(input('Telefone: ')).upper()
      if telefone == 'CANCELAR':
        main_menu()
      else:
        cpf = str(input('CPF: ')).upper()
        if cpf == 'CANCELAR':
          main_menu()
        else:
          index.append(len(index))
          sobrenomes.append(sobrenome)
          telefones.append(telefone)    
          nomes.append(nome)
          cpfs.append(cpf)

          print()
          print('CADASTRO CONCLUÍDO COM SUCESSO!')

          main_menu()


#FUNÇÃO LISTA - Lista todos os nomes e sobrenomes na base de dados
#Pode ser atualizada para exibir mais dados

def listar():
  print('***LISTAR***')
  print('Aspessoas cadastradas no sistema são:')
  print()

  for num in index: 
    print(f'{database["index"][num]} - {database["nome"][num]} {database["sobrenome"][num]}')

  print()
  print('LISTA CONCLUÍDA COM SUCESSO!')

  main_menu()


#FUNÇÃO REMOVER - Utiliza a função busca e caso retorne um valor existente
#remove o mesmo da base de dados
def remover():
  print('***REMOVER***')
  print()

  nome = str(input('Nome do cadastro a remover: ')).upper()
  if nome == 'CANCELAR':
    main_menu()
  else:
    sobrenome = str(input('Sobrenome do cadastro a remover: ')).upper()
    if sobrenome == 'CANCELAR':
      main_menu()
    else:
      num_index = busca(nome, sobrenome)
      if num_index == -1:
        print('Cadastro não encontrado')
        print()
        remover()
      else:
        for numero in index:
          nome = database["nome"][numero-1]
          sobrenome = database["sobrenome"][numero-1]
          telefone = database["telefone"][numero-1]
          cpf =  database["cpf"][numero-1]

          if numero == num_index:
            index.remove(len(index)-1)
            nomes.remove(nome)
            sobrenomes.remove(sobrenome)
            telefones.remove(telefone)
            cpfs.remove(cpf)

  print('CADASTRO REMOVIDO COM SUCESSO')

  main_menu()
 

#FUNÇÃO EDITAR - Utiliza a função busca e caso retorne um valor existente
#permite alterar cadaum dos valores da base de dados

def editar():
  print('***EDITAR***')
  print()

  nome = str(input('Nome do cadastro a ser editado: ')).upper()
  if nome == 'CANCELAR':
    main_menu()
  else:
    sobrenome = str(input('Sobrenome do cadastro a ser editado: ')).upper()
    if sobrenome == 'CANCELAR':
      main_menu()
    else:
      num_index = busca(nome, sobrenome)
      if num_index == -1:
        print('Cadastro não encontrado')
        print()
        editar()
      else:
        for numero in index:
          nome = database["nome"][numero-1]
          sobrenome = database["sobrenome"][numero-1]
          telefone = database["telefone"][numero-1]
          cpf =  database["cpf"][numero-1]

          if numero == num_index:
            novo_nome = str(input('Nome: ')).upper()
            novo_sobrenome = str(input('Sobrenome: ')).upper()
            novo_telefone = str(input('Telefone: ')).upper()
            novo_cpf = str(input('CPF: ')).upper()
            
            if novo_nome != '':
              nomes[numero-1] = novo_nome
            if novo_sobrenome != '':
              sobrenomes[numero-1] = novo_sobrenome
            if novo_telefone != '':
              telefones[numero-1] = novo_telefone
            if novo_cpf != '':
              cpfs[numero-1] = novo_cpf

  print('CADASTRO EDITADO COM SUCESSO')

  main_menu()

#Execução da função MENU INICIAL para inicio do programa

main_menu()
