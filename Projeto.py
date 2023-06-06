grafo = {
    'Limeira' : {
        'vizinhos': {
            'Mogi Mirim': {'distancia': 52, 'custoPedagio': 10.90, 'tempo': 0.76, 'qtdPostoPolicial': 0},
            'Paulinia': {'distancia': 51, 'custoPedagio': 0.0, 'tempo': 0.68, 'qtdPostoPolicial': 0},
            'Capivari': {'distancia': 68, 'custoPedagio': 0.0, 'tempo': 0.93, 'qtdPostoPolicial': 0}
        }
    },
    
    'Mogi Mirim' : {
        'vizinhos': {
            'Limeira': {'distancia': 52, 'custoPedagio': 10.90, 'tempo': 0.76, 'qtdPostoPolicial': 0},
            'Jaguariuna': {'distancia': 39, 'custoPedagio': 0.0, 'tempo': 0.5, 'qtdPostoPolicial': 1},
            'Serra Negra': {'distancia': 55, 'custoPedagio': 9.60, 'tempo': 0.81, 'qtdPostoPolicial': 0},
        }
    },
    
    'Paulinia' : {
        'vizinhos': {
            'Limeira': {'distancia': 51, 'custoPedagio': 0.0, 'tempo': 0.68, 'qtdPostoPolicial': 0},
            'Campinas': {'distancia': 21, 'custoPedagio': 0.0, 'tempo': 0.46, 'qtdPostoPolicial': 0}
        }
    },
    
    'Capivari' : {
        'vizinhos': {
            'Limeira': {'distancia': 68, 'custoPedagio': 0.0, 'tempo': 0.93, 'qtdPostoPolicial': 0},
            'Campinas': {'distancia': 53, 'custoPedagio': 8.90, 'tempo': 0.81, 'qtdPostoPolicial': 1},
            'Indaiatuba': {'distancia': 32, 'custoPedagio': 8.90, 'tempo': 0.73, 'qtdPostoPolicial': 1}
        }
    },
    
    'Jaguariuna' : {
        'vizinhos': {
            'Mogi Mirim': {'distancia': 39, 'custoPedagio': 0.0, 'tempo': 0.5, 'qtdPostoPolicial': 1},
            'Campinas': {'distancia': 29, 'custoPedagio': 7.60, 'tempo': 0.6, 'qtdPostoPolicial': 1}
        }
    },
    
    'Campinas' : {
        'vizinhos': {
            'Jaguariuna': {'distancia': 29, 'custoPedagio': 7.60, 'tempo': 0.6, 'qtdPostoPolicial': 1},
            'Paulinia': {'distancia': 21, 'custoPedagio': 0.0, 'tempo': 0.46, 'qtdPostoPolicial': 0},
            'Capivari': {'distancia': 53, 'custoPedagio': 8.90, 'tempo': 0.81, 'qtdPostoPolicial': 1},
            'Jundiai': {'distancia': 40, 'custoPedagio': 11.70, 'tempo': 0.6, 'qtdPostoPolicial': 0},
            'Itatiba': {'distancia': 38, 'custoPedagio': 13.50, 'tempo': 0.6, 'qtdPostoPolicial': 0}
        }
    },
    
    'Indaiatuba' : {
        'vizinhos': {
            'Capivari': {'distancia': 32, 'custoPedagio': 8.90, 'tempo': 0.73, 'qtdPostoPolicial': 1},
            'Jundiai': {'distancia': 50.9, 'custoPedagio': 28.50, 'tempo': 0.76 , 'qtdPostoPolicial': 2}
        }
    },
    
    'Jundiai' : {
        'vizinhos': {
            'Campinas': {'distancia': 40, 'custoPedagio': 11.70, 'tempo': 0.6, 'qtdPostoPolicial': 0},
            'Indaiatuba': {'distancia': 50.9, 'custoPedagio': 28.50, 'tempo': 0.76, 'qtdPostoPolicial': 2},
            'Itatiba': {'distancia': 25.3, 'custoPedagio': 4.50, 'tempo': 0.48 , 'qtdPostoPolicial': 1},
            'Atibaia': {'distancia': 61.9, 'custoPedagio': 9.30, 'tempo': 1.06, 'qtdPostoPolicial': 2},
            'São Paulo': {'distancia': 58.8 , 'custoPedagio': 11.80, 'tempo': 0.95, 'qtdPostoPolicial': 3}
        }
    },
    
    'Itatiba' : {
        'vizinhos': {
            'Campinas': {'distancia': 38, 'custoPedagio': 13.50, 'tempo': 0.6, 'qtdPostoPolicial': 0},
            'Jundiai': {'distancia': 25.3, 'custoPedagio': 4.50, 'tempo': 0.48, 'qtdPostoPolicial': 1},
            'Serra Negra': {'distancia': 64.2, 'custoPedagio': 0.0, 'tempo': 1.28, 'qtdPostoPolicial': 1},
            'Atibaia': {'distancia': 37.3, 'custoPedagio': 9.30, 'tempo': 0.6, 'qtdPostoPolicial': 1}
        }
    },
    
    'Serra Negra' : {
        'vizinhos': {
            'Mogi Mirim': {'distancia': 55, 'custoPedagio': 9.60, 'tempo': 0.81, 'qtdPostoPolicial': 0},
            'Itatiba': {'distancia': 64.2, 'custoPedagio': 0.0, 'tempo': 1.28, 'qtdPostoPolicial': 1},
            'Bragança Paulista': {'distancia': 63.6, 'custoPedagio': 0.0, 'tempo': 1.22, 'qtdPostoPolicial': 1}
        }
    },
    
    'Bragança Paulista' : {
        'vizinhos': {
            'Serra Negra': {'distancia': 63.6, 'custoPedagio': 0.0, 'tempo': 1.22, 'qtdPostoPolicial': 1},
            'Atibaia': {'distancia': 25.3, 'custoPedagio': 0.0, 'tempo': 0.53, 'qtdPostoPolicial': 0},
            'Camanducaia': {'distancia': 57.4, 'custoPedagio': 2.80, 'tempo': 0.9, 'qtdPostoPolicial': 2}
        }
    },
    
    'Atibaia' : {
        'vizinhos': {
            'Itatiba': {'distancia': 37.3, 'custoPedagio': 9.30, 'tempo': 0.6, 'qtdPostoPolicial': 1},
            'Bragança Paulista': {'distancia': 25.3, 'custoPedagio': 0.0, 'tempo': 0.53, 'qtdPostoPolicial': 0},
            'Jundiai': {'distancia': 61.9, 'custoPedagio': 9.30, 'tempo': 0.6, 'qtdPostoPolicial': 2},
            'Guarulhos': {'distancia': 52.9, 'custoPedagio': 0.0, 'tempo': 1.02, 'qtdPostoPolicial': 2},
            'São José dos Campos': {'distancia': 90.3, 'custoPedagio': 17.59, 'tempo': 1.15, 'qtdPostoPolicial': 3}
        }
    },
    
    'São Paulo' : {
        'vizinhos': {
            'Jundiai': {'distancia': 58.8, 'custoPedagio': 11.80, 'tempo': 0.95, 'qualidadeVia': 3},
            'Guarulhos': {'distancia': 22.0, 'custoPedagio': 0.0, 'tempo': 0.66, 'qualidadeVia': 0}
        }
    },
    
    'Guarulhos' : {
        'vizinhos': {
            'São Paulo': {'distancia': 22.0, 'custoPedagio': 0.0, 'tempo': 0.66, 'qtdPostoPolicial': 0},
            'Atibaia': {'distancia': 52.9, 'custoPedagio': 0.0, 'tempo': 1.02, 'qtdPostoPolicial': 2},
            'São José dos Campos': {'distancia': 75.2, 'custoPedagio': 12.35, 'tempo': 1.08, 'qtdPostoPolicial': 6}
        }
    },
    
    'São José dos Campos' : {
        'vizinhos': {
            'Guarulhos': {'distancia': 75.2, 'custoPedagio': 12.35, 'tempo': 1.08, 'qtdPostoPolicial': 6},
            'Atibaia': {'distancia': 90.3, 'custoPedagio': 17.59, 'tempo': 1.15, 'qtdPostoPolicial': 3},
            'Taubaté': {'distancia': 42.2, 'custoPedagio': 0.0, 'tempo': 0.65, 'qtdPostoPolicial': 0},
            'Paraisópolis': {'distancia': 119.2, 'custoPedagio': 0.0, 'tempo': 1.96, 'qtdPostoPolicial': 0}
        }
    },
    
    'Taubaté' : {
        'vizinhos': {
            'São José dos Campos': {'distancia': 42.2, 'custoPedagio': 0.0, 'tempo': 0.65, 'qtdPostoPolicial': 0},
            'Santo Antônio do Pinhal': {'distancia': 35.4, 'custoPedagio': 0.0, 'tempo': 0.8, 'qtdPostoPolicial': 2}
        }
    },
    
    'Santo Antônio do Pinhal' : {
        'vizinhos': {
            'Taubaté': {'distancia': 35.4, 'custoPedagio': 0.0, 'tempo': 0.8, 'qtdPostoPolicial': 2},
            'Campos do Jordão': {'distancia': 22.2, 'custoPedagio': 0.0, 'tempo': 0.41, 'qtdPostoPolicial': 0}
        }
    },
    
    'Campos do Jordão' : {
        'vizinhos': {
            'Santo Antônio do Pinhal': {'distancia': 16.6, 'custoPedagio': 0.0, 'tempo': 0.43, 'qtdPostoPolicial': 0},
            'Paraisópolis': {'distancia': 49.5, 'custoPedagio': 0.0, 'tempo': 1.06, 'qtdPostoPolicial': 0}
        }
    },
    
    'Paraisópolis' : {
        'vizinhos': {
            'Campos do Jordão': {'distancia': 49.5, 'custoPedagio': 0.0, 'tempo': 1.06, 'qtdPostoPolicial': 0},
            'Camanducaia': {'distancia': 60.7, 'custoPedagio': 2.90, 'tempo': 1.25, 'qtdPostoPolicial': 0},
            'São José dos Campos': {'distancia': 119.2, 'custoPedagio': 0.0, 'tempo': 1.96, 'qtdPostoPolicial': 0}
        }
    },

    'Camanducaia' : {
        'vizinhos': {
            'Paraisópolis': {'distancia': 60.7, 'custoPedagio': 2.90, 'tempo': 1.25, 'qtdPostoPolicial': 0},
            'Bragança Paulista': {'distancia': 57.4, 'custoPedagio': 2.80, 'tempo': 0.9, 'qtdPostoPolicial': 2}
        }
    },
}

def menorDistancia(grafo, origem, destino):
    distancias = {cidade: float('inf') for cidade in grafo}
    distancias[origem] = 0
    antecessores = {cidade: None for cidade in grafo}
    visitados = []

    while len(visitados) < len(grafo):
        cidadeAtual = None
        menorDistancia = float('inf')

        for cidade, distancia in distancias.items():
            if cidade not in visitados and distancia < menorDistancia:
                cidadeAtual = cidade
                menorDistancia = distancia

        if cidadeAtual == destino:
            break

        visitados.append(cidadeAtual)

        vizinhos = grafo[cidadeAtual]['vizinhos']
        for vizinho, dados in vizinhos.items():
            novaDistancia = distancias[cidadeAtual] + dados['distancia']

            if novaDistancia < distancias[vizinho]:
                distancias[vizinho] = novaDistancia
                antecessores[vizinho] = cidadeAtual
    
    caminho = []
    cidade = destino
    while cidade is not None:
        caminho.insert(0, cidade)
        cidade = antecessores[cidade]

    print(f"\nO caminho mais curto entre {origem} e {destino} é:")
    print("\n\t[  ", end="")
    for cidade in caminho:
        print(cidade, "  ", end="")
    
    print("] ", distancias[destino], "Km")



def menorTempo(grafo, origem, destino):
    tempos = {cidade: float('inf') for cidade in grafo}
    tempos[origem] = 0
    antecessores = {cidade: None for cidade in grafo}
    visitados = []

    while len(visitados) < len(grafo):
        cidadeAtual = None
        menorTempo = float('inf')

        for cidade, tempo in tempos.items():
            if cidade not in visitados and tempo < menorTempo:
                cidadeAtual = cidade
                menorTempo = tempo

        if cidadeAtual == destino:
            break

        visitados.append(cidadeAtual)

        vizinhos = grafo[cidadeAtual]['vizinhos']
        for vizinho, dados in vizinhos.items():
            novoTempo = tempos[cidadeAtual] + dados['tempo']

            if novoTempo < tempos[vizinho]:
                tempos[vizinho] = novoTempo
                antecessores[vizinho] = cidadeAtual
    
    caminho = []
    cidade = destino
    while cidade is not None:
        caminho.insert(0, cidade)
        cidade = antecessores[cidade]
    
    minutos = tempos[destino] * 60

    contadorHoras = 0

    while minutos >= 60:
        contadorHoras += 1
        minutos -= 60
        minutosArred = int(minutos)

    print(f"\nO caminho com menor tempo de percurso entre {origem} e {destino} é:")
    print("\n\t[  ", end="")
    for cidade in caminho:
        print(cidade, "  ", end="")
    
    if(minutos >= 60):
        print("] ",contadorHoras, "h", minutosArred, "min")
    else:
        minutoss = int(minutos)
        print("] ",contadorHoras, "h", minutoss, "min")

def menorCusto(grafo, origem, destino):
    precos = {cidade: float('inf') for cidade in grafo}
    precos[origem] = 0
    antecessores = {cidade: None for cidade in grafo}
    visitados = []

    while len(visitados) < len(grafo):
        cidadeAtual = None
        menorPreco = float('inf')

        for cidade, preco in precos.items():
            if cidade not in visitados and preco < menorPreco:
                cidadeAtual = cidade
                menorPreco = preco

        if cidadeAtual == destino:
            break

        visitados.append(cidadeAtual)

        vizinhos = grafo[cidadeAtual]['vizinhos']
        for vizinho, dados in vizinhos.items():
            novoPreco = precos[cidadeAtual] + dados['custoPedagio']

            if novoPreco < precos[vizinho]:
                precos[vizinho] = novoPreco
                antecessores[vizinho] = cidadeAtual
    
    caminho = []
    cidade = destino
    while cidade is not None:
        caminho.insert(0, cidade)
        cidade = antecessores[cidade]

    if precos[destino] == 0:
        print("\nO percurso [", end='')
        for cidade in caminho:
            print(cidade, "  ", end="")
        print("] não possui pedágios!")
    
    else:
        print(f"\nO caminho com menor custo entre {origem} e {destino} é:")
        print("\n\t[  ", end="")
        for cidade in caminho:
            print(cidade, "  ", end="")
        
        print("] R$ %.2f" % precos[destino])

def qtdPostoPolicial(grafo, origem, destino):
    quantidades = {cidade: float('inf') for cidade in grafo}
    quantidades[origem] = 0
    antecessores = {cidade: None for cidade in grafo}
    visitados = []

    while len(visitados) < len(grafo):
        cidadeAtual = None
        menorQtd = float('inf')

        for cidade, quantidade in quantidades.items():
            if cidade not in visitados and quantidade < menorQtd:
                cidadeAtual = cidade
                menorQtd = quantidade

        if cidadeAtual == destino:
            break

        visitados.append(cidadeAtual)

        vizinhos = grafo[cidadeAtual]['vizinhos']
        for vizinho, dados in vizinhos.items():
            novaQtd = quantidades[cidadeAtual] + dados['qtdPostoPolicial']

            if novaQtd < quantidades[vizinho]:
                quantidades[vizinho] = novaQtd
                antecessores[vizinho] = cidadeAtual
    
    caminho = []
    cidade = destino
    while cidade is not None:
        caminho.insert(0, cidade)
        cidade = antecessores[cidade]
        
    if quantidades[destino] == 0:
        print("\nO percurso [", end='')
        for cidade in caminho:
            print(cidade, "  ", end="")
        print("] não possui posto policial!")
        
    else:

        print(f"\nO caminho com menor quantidade de posto policial entre {origem} e {destino} é:")
        print("\n\t[  ", end="")
        for cidade in caminho:
            print(cidade, "  ", end="")
        
        print("] ", quantidades[destino], end='')
        if quantidades[destino] == 1:
            print(" posto")
        elif quantidades[destino] > 1:
            print(" postos")




print ("\n\n\t_______________________________")
print ("\n\tPROGRAMA DE DEFINIÇÃO DE ROTAS")
print ("\t_______________________________")
print ("\n\t\tGrupo: Brenda Carmo, Isabella Mendes, Julia Medeiros")

print("\n\n| Seja bem vindo ao Programa de Definição de Rotas! \n| O programa define a melhor rota para entrega de produtos baseada na regra que você escolher.")

rotaNaoConfirmada = True
while rotaNaoConfirmada:
    cidadeInexistente = True
    while cidadeInexistente:
        print("\n\nQual a cidade de saída do produto?")
        print("\n\t1) Limeira \n\t2) Mogi Mirim \n\t3) Paulinia \n\t4) Capivari \n\t5) Jaguariúna \n\t6) Campinas \n\t7) Indaiatuba \n\t8) Jundiai \n\t9) Itatiba \n\t10) Serra Negra \n\t11) Bragança Paulista \n\t12) Atibaia \n\t13) São Paulo \n\t14) Guarulhos \n\t15) São José dos Campos \n\t16) Taubaté \n\t17) Santo Antônio do Pinhal \n\t18) Campos do Jordão \n\t19) Paraisópolis \n\t20) Camanducaia \n\t21) Sair do programa")
        
        try:
            saida = int(input("\nCidade de saída: "))
            
        

            if (saida <= 0 or saida > 21):
                print("\t\t __________________________________________")
                print("\n\t\t| ATENÇÃO: Opção inválida. Tente novamente |")
                print("\t\t __________________________________________")
                cidadeInexistente = True
            else:
                cidadeInexistente = False
        
        except ValueError:
            print("\t\t ________________________________________")
            print("\n\t\t| ATENÇÃO: Digite apenas números inteiros |")
            print("\t\t ________________________________________")

    if (saida == 1):
        saida = "Limeira"
    elif (saida == 2):
        saida = "Mogi Mirim"
    elif (saida == 3):
        saida = "Paulinia"
    elif (saida == 4):
        saida = "Capivari"
    elif (saida == 5):
        saida = "Jaguariuna"
    elif (saida == 6):
        saida = "Campinas"
    elif (saida == 7):
        saida = "Indaiatuba"
    elif (saida == 8):
        saida = "Jundiai"
    elif (saida == 9):
        saida = "Itatiba"
    elif (saida == 10):
        saida = "Serra Negra"
    elif (saida == 11):
        saida = "Bragança Paulista"
    elif (saida == 12):
        saida = "Atibaia"
    elif (saida == 13):
        saida = "São Paulo"
    elif (saida == 14):
        saida = "Guarulhos"
    elif (saida == 15):
        saida = "São José dos Campos"
    elif (saida == 16):
        saida = "Taubaté"
    elif (saida == 17):
        saida = "Santo Antônio do Pinhal"
    elif (saida == 18):
        saida = "Campos do Jordão"
    elif (saida == 19):
        saida = "Paraisópolis"
    elif (saida == 20):
        saida = "Camanducaia"
    elif (saida == 21):
        print("\n\n\tObrigada por utilizar o programa! Volte sempre :)\n\n")
        exit()

    cidadeInexistente = True
    while cidadeInexistente: 
        print("\n\nQual a cidade de entrega do produto?")
        print("\n\t1) Limeira \n\t2) Mogi Mirim \n\t3) Paulinia \n\t4) Capivari \n\t5) Jaguariúna \n\t6) Campinas \n\t7) Indaiatuba \n\t8) Jundiai \n\t9) Itatiba \n\t10) Serra Negra \n\t11) Bragança Paulista \n\t12) Atibaia \n\t13) São Paulo \n\t14) Guarulhos \n\t15) São José dos Campos \n\t16) Taubaté \n\t17) Santo Antônio do Pinhal \n\t18) Campos do Jordão \n\t19) Paraisópolis \n\t20) Camanducaia \n\t21) Sair do Programa")

        try:
            entrega = int(input("\nCidade de entrega: "))

            if (entrega <= 0 or entrega > 21):
                print("\t\t __________________________________________")
                print("\n\t\t| ATENÇÃO: Opção inválida. Tente novamente |")
                print("\t\t __________________________________________")
                cidadeInexistente = True
            else:
                cidadeInexistente = False

        except ValueError:
            print("\t\t ________________________________________")
            print("\n\t\t| ATENÇÃO: Digite apenas números inteiros |")
            print("\t\t ________________________________________")

    if (entrega == 1):
        entrega = "Limeira"
    elif (entrega == 2):
        entrega = "Mogi Mirim"
    elif (entrega == 3):
        entrega = "Paulinia"
    elif (entrega == 4):
        entrega = "Capivari"
    elif (entrega == 5):
        entrega = "Jaguariuna"
    elif (entrega == 6):
        entrega = "Campinas"
    elif (entrega == 7):
        entrega = "Indaiatuba"
    elif (entrega == 8):
        entrega = "Jundiai"
    elif (entrega == 9):
        entrega = "Itatiba"
    elif (entrega== 10):
        entrega = "Serra Negra"
    elif (entrega == 11):
        entrega = "Bragança Paulista"
    elif (entrega == 12):
        entrega = "Atibaia"
    elif (entrega == 13):
        entrega = "São Paulo"
    elif (entrega == 14):
        entrega = "Guarulhos"
    elif (entrega == 15):
        entrega = "São José dos Campos"
    elif (entrega == 16):
        entrega = "Taubaté"
    elif (entrega == 17):
        entrega = "Santo Antônio do Pinhal"
    elif (entrega == 18):
        entrega = "Campos do Jordão"
    elif (entrega == 19):
        entrega = "Paraisópolis"
    elif (entrega== 20):
        entrega = "Camanducaia"
    elif (entrega == 21):
        print("\n\n\tObrigada por utilizar o programa! Volte sempre :)\n\n")
        exit()

    if (saida == entrega):
        print("\t\t __________________________________________________________")
        print("\n\t\t| ATENÇÃO: A cidade de saída não pode ser a mesma da entrega |")
        print("\t\t __________________________________________________________")
        rotaNaoConfirmada = True
    else:
        print("\n\tRota selecionada: ", saida, " ------> ", entrega)

        digitouErrado = True
        while digitouErrado:
            confirmado = input("\n\nConfirmar (S / N)? ").upper()

            if (confirmado == "S" or confirmado == "N"):
                digitouErrado = False
            else:
                print("\t\t ___________________________________________________")
                print("\n\t\t| ATENÇÃO: Digite apenas 'S' ou 'N'. Tente novamente |")
                print("\t\t ___________________________________________________")
                digitouErrado = True

        if (confirmado == "N"):
            rotaNaoConfirmada = True
        elif (confirmado == "S"):
            rotaNaoConfirmada = False
            

opcaoInvalida = True
while opcaoInvalida:
    print("\n\nQual regra você deseja utilizar para defirnir a melhor rota? ")
    print("\n\t1) Menor distância \n\t2) Menor custo \n\t3) Menor tempo \n\t4) Menor quantidade de Posto Policial \n\t5) Sair do programa")

    try:
        regra = int(input("\nRegra:  "))

        if (regra <= 0 or regra > 5 ):
            print("\t\t __________________________________________")
            print("\n\t\t| ATENÇÃO: Opção inválida. Tente novamente |")
            print("\t\t __________________________________________")
            opcaoInvalida = True
        elif (regra == 5):
            print("\n\n\tObrigada por utilizar o programa! Volte sempre :)\n\n")
            exit()
        else:
            opcaoInvalida = False

    except ValueError:
        print("\t\t ________________________________________")
        print("\n\t\t| ATENÇÃO: Digite apenas números inteiros |")
        print("\t\t ________________________________________")

if (regra == 1):
    menorDistancia(grafo, saida, entrega)

elif (regra == 2):
    menorCusto(grafo, saida, entrega)
elif (regra == 3):
    menorTempo(grafo, saida, entrega)
elif (regra == 4):
    qtdPostoPolicial(grafo, saida, entrega)

print("\n\n\n\t\t| BOA VIAGEM !! |\n\n")
