print("-----seja bem vindx ao Willfinder-----")
acesso=str(input("você ja possui cadastro?"))
if acesso=="sim":
    email=str(input("Por favor, digite seu e-mail cadastrado"))
    login=int(input("Por favor, digite sua senha de 6 dígitos"))
    print("bem vindo")
else:
    print("vamos criar seu cadastro ")
    nome=str(input("Digite seu nome: "))
    sobrenome=str(input("Qual o seu sobrenome? "))
    print("Seja bem-vindo ao willfinder", nome, sobrenome)
    idade=int(input(" Qual sua idade? "))
    if idade>=18:
        print("Parabéns, você é maior de idade")
    else   :
        print("Essa não:(")
        print("parece que você é menor de idade")
        print("tente novamente no futuro")
    endereco=str(input("Qual é o seu endereço? "))
    print(endereco)
    email=str(input("Por favor, digite seu e-mail: "))
    login=int(input("Por favor, crie uma senha com 6 dígitos numericos: "))
print("Seu cadastro foi criado com sucesso,", nome)
listadeservicos=str(input('você deseja ver quais estabelecimentos estão disponiveis na sua região'))
if listadeservicos=='sim':
    regiao=str(input('digite a zona em que você reside. ex.:zona sul'))
    if (regiao=='zs') or (regiao=='zona sul'):
        print('estabelecimentos disponiveis na sua região: ')
        print('academias, supermercados, lavanderias, shopping center')
    if(regiao=="zona leste")or(regiao=='zl'):
        print('estabelecimentos disponiveis na sua região: ')
        print('academias, supermercados, , shopping centers')
    if(regiao=='zo')or(regiao=='zona oeste'):
        print('estabelecimentos disponiveis na sua região: ')
        print('academias, supermercados, cinemas ')
    if(regiao=='centro'):
        print('estabelecimentos disponiveis na sua região: ')
        print('academias, supermercados, lavanderias, shopping center, cinemas')
    if(regiao=='zona norte')or (regiao=='zn'):
        print('estabelecimentos disponiveis na sua região: ')
        print('academias, supermercados, hospitais')
servico=str(input("Qual o tipo de estabelecimento você gostaria de contratar?"))
#eixo de servicos zona sul
if(servico=='academia')and(regiao=='zs', 'zona sul'):
    print('academias disponiveis: smart fit, selfit, bluefit')
    if(servico=='supermercado')and(regiao=='zs', 'zona sul'):
        print('supermercados disponiveis: extra, carrefour, clube sams')
    if(servico=='lavanderia')and(regiao=='zs', 'zona sul'):
        print('lavanderias disponiveis: omo lavanderia, lavanderia 60 minutos ')
    if(servico=='shopping center ')and(regiao=='zs', 'zona sul'):
        print(' shoppings centers disponiveis: shopping market place, shopping campo limpo, shopping plaza sul')
#eixo de servicos da zona leste
elif(servico=='academia')and(regiao=='zona leste', 'zl'):
    print('academias disponiveis: selfit, bluefit')
    if(servico=='supermercados')and(regiao=='zona leste', 'zl'):
         print('supermercados disponiveis: extra, carrefour')
    if(servico=='shoppings center')and(regiao=='zona leste', 'zl'):
         print(' shoppings centers disponiveis: shopping analia franco, shopping fashion brás, shopping metrô itaquera ' )
#adicionar as outras regioes
#resolver o choque dos ifs