print("-----seja bem vindx ao Willfinder-----")
#cadastro ou login
acesso=str.lower(input("você ja possui cadastro?"))
if acesso=="sim":
    email=str(input("Por favor, digite seu e-mail cadastrado"))
    login=int(input("Por favor, digite sua senha de 6 dígitos"))
    print("bem vindo")
else:
    print("vamos criar seu cadastro ")
    nome=str(input("Digite seu nome: "))
    sobrenome=str(input("Qual o seu sobrenome? "))
    print("Seja bem-vindo ao willfinder", nome, sobrenome)
   
while True: 
    idade=int(input(" Qual sua idade? "))
    if (idade>=18):
        print("Parabéns, você é maior de idade")
        break
    elif(idade<18):
        print("Essa não:(")
        print("parece que você é menor de idade")
        print("tente novamente no futuro")
endereco=str(input("Qual é o seu endereço? "))
print(endereco)
email=str(input("Por favor, digite seu e-mail: "))
login=int(input("Por favor, crie uma senha com 6 dígitos numericos: "))
print("Seu cadastro foi criado com sucesso,", nome)
#lista de sericos
#regiao e servicos
#erro
listadeservicos=str.lower(input('você deseja ver quais estabelecimentos estão disponiveis na sua região? '))
if (listadeservicos=='não'):
    print("entendido ")
elif(listadeservicos=='sim'):
    regiao=str.lower(input('digite a zona em que você reside. ex.:zona sul'))
elif(regiao=='zs') or (regiao=='zona sul'):
    print('estabelecimentos disponiveis na sua região: ')
    print('academias, supermercados, lavanderias, shopping center')
elif(regiao=="zona leste")or(regiao=='zl'):
    print('estabelecimentos disponiveis na sua região: ')
    print('academias, supermercados, , shopping centers')
elif(regiao=='zo')or(regiao=='zona oeste'):
    print('estabelecimentos disponiveis na sua região: ')
    print('academias, supermercados, cinemas ')
elif(regiao=='centro'):
    print('estabelecimentos disponiveis na sua região: ')
    print('academias, supermercados, lavanderias, shopping center, cinemas')
elif(regiao=='zona norte')or (regiao=='zn'):
    print('estabelecimentos disponiveis na sua região: ')
    print('academias, supermercados, hospitais')
else:
    print("serviço  ou regiao nao encontrado")

servico=str(input("Qual o tipo de estabelecimento você gostaria de contratar?"))
#eixo de servicos zona sul
if(servico=='academia')and(regiao=='zs', regiao=='zona sul'):
    print('academias disponiveis: smart fit, selfit, bluefit')
elif(servico=='supermercado')and(regiao=='zs', 'zona sul'):
    print('supermercados disponiveis: extra, carrefour, clube sams')
elif(servico=='lavanderia')and(regiao=='zs', 'zona sul'):
    print('lavanderias disponiveis: omo lavanderia, lavanderia 60 minutos ')
elif(servico=='shopping center ')and(regiao=='zs', 'zona sul'):
    print(' shoppings centers disponiveis: shopping market place, shopping campo limpo, shopping plaza sul')
#eixo de servicos da zona leste

if(servico=='academia')and(regiao=='zona leste', 'zl'):
    print('academias disponiveis: selfit, bluefit')
elif(servico=='supermercados')and(regiao=='zona leste', 'zl'):
    print('supermercados disponiveis: extra, carrefour')
elif(servico=='shoppings center')and(regiao=='zona leste', 'zl'):
    print(' shoppings centers disponiveis: shopping analia franco, shopping fashion brás, shopping metrô itaquera ' )
#adicionar as outras regioes
#resolver o choque dos ifs