#CADASTRO V02 - CODIGO RE-ESCRITO DE FORMA MAIS LEGIVEL

database = []
lista_parametros = ['nome','sobrenome','telefone','cpf']



#MENU INICIAL - Chama as demais funções ou termina o programa:
def main_menu():
  print()
  selection = str(input('O que deseja fazer? :')).capitalize()

  if selection == 'C' or selection == 'Cadastrar':
    cadastro()

  elif selection == 'L' or selection == 'Listar':
    listar()

  elif selection == 'R' or selection == 'Remover':
    remover()

  elif selection == 'E' or selection == 'Editar':
    editar()

  elif selection == 'T':
    terminate()

  else:
    print('Selecao invalida')
    print()
    main_menu()



#FUNÇÃO CADASTRO
def cadastro():
  print('***CADASTRAR***')
  nome = input('NOME: ').upper()
  if nome == 'CANCELAR':
    main_menu()

  sobrenome = input('SOBRENOME: ').upper()
  if sobrenome == 'CANCELAR':
    main_menu()

  telefone =  input('TELEFONE: ').upper()
  if telefone == 'CANCELAR':
    main_menu()
  
  cpf =   input('CPF: ').upper()
  if cpf == 'CANCELAR':
    main_menu()

  cadastro = {
      "nome":nome, 
      "sobrenome":sobrenome, 
      "telefone":telefone, 
      "cpf":cpf
      }

  database.append(cadastro)
  print('CADASTRO CONCLUÍDO COM SUCESSO!')
  main_menu()



#FUNÇÃO LISTAR NOMES E SOBRENOMES NO SISTEMA
def listar():
  print('***LISTAR***')
  print('Aspessoas cadastradas no sistema são:')
  print()

  for item_cadastrado in database: 
    print(item_cadastrado["nome"], item_cadastrado["sobrenome"])

  print()
  print('LISTA CONCLUÍDA COM SUCESSO!')

  main_menu()



#FUNÇÃO REMOVER - Busca o nome e sobrenome na lista cadastrada e caso existe
#remove o mesmo
def remover():
  print('***REMOVER***')
  print()

  nome_remover = str(input('Nome completo do cadastro a remover: ')).upper()
  if nome_remover == 'CANCELAR':
    main_menu()
  
  nome_remover = nome_remover.split(' ')
  nome_encontrado = False

  for item_cadastrado in database:

    if item_cadastrado["nome"] == nome_remover[0] and item_cadastrado["sobrenome"] == nome_remover[1]:
      database.remove(item_cadastrado)
      nome_encontrado = True

  if nome_encontrado == True:
    print('CADASTRO REMOVIDO COM SUCESSO')
  else:
    print('CADASTRO NÃO ENCONTRADO')
    remover()

  main_menu()



#FUNÇÃO EDITAR - Busca nome e sobrenome na lista e caso exista permite editar
def editar():
  print('***EDITAR***')
  print()

  nome_editar = str(input('Nome completo do cadastro a editar: ')).upper()
  if nome_editar == 'CANCELAR':
    main_menu()
  
  nome_editar = nome_editar.split(' ')
  nome_encontrado = False

  for item_cadastrado in database:

    if item_cadastrado["nome"] == nome_editar[0] and item_cadastrado["sobrenome"] == nome_editar[1]:
      for parametro in lista_parametros:
        print(parametro.upper(), 'ATUAL: ',item_cadastrado[parametro])
        novo_valor = input(f'NOVO {parametro.upper()}: ').upper()

        if novo_valor != '':
          item_cadastrado[parametro] = novo_valor

      nome_encontrado = True

  if nome_encontrado == True:
    print('CADASTRO EDITADO COM SUCESSO')
  else:
    print('CADASTRO NÃO ENCONTRADO')
    editar()
  main_menu()



#FIM DE PROGRAMA
def terminate():
  print('FIM DA EXECUÇÃO')
  exit()



main_menu()
