grafo = {
    'limeira' : {
        'vizinhos': {
            'mogi mirim': {'distancia': 52, 'velocidadeMax': 68.42, 'tempo': 0.76, 'qualidadeVia': 6},
            'paulinia': {'distancia': 51, 'velocidadeMax': 75, 'tempo': 0.68, 'qualidadeVia': 4},
            'capivari': {'distancia': 68, 'velocidadeMax': 73.11, 'tempo': 0.93, 'qualidadeVia': 10}
        }
    },
    
    'mogi mirim' : {
        'vizinhos': {
            'limeira': {'distancia': 52, 'velocidadeMax': 68.42, 'tempo': 0.76, 'qualidadeVia': 6},
            'jaguariuna': {'distancia': 39, 'velocidadeMax': 78, 'tempo': 0.5, 'qualidadeVia': 8},
            'serra Negra': {'distancia': 55, 'velocidadeMax': 67.90, 'tempo': 0.81, 'qualidadeVia': 6},
        }
    },
    
    'paulinia' : {
        'vizinhos': {
            'limeira': {'distancia': 51, 'velocidadeMax': 75, 'tempo': 0.68, 'qualidadeVia': 4},
            'campinas': {'distancia': 21, 'velocidadeMax': 45.65, 'tempo': 0.46, 'qualidadeVia': 8}
        }
    },
    
    'capivari' : {
        'vizinhos': {
            'limeira': {'distancia': 68, 'velocidadeMax': 73.11, 'tempo': 0.93, 'qualidadeVia': 10},
            'campinas': {'distancia': 53, 'velocidadeMax': 65.43, 'tempo': 0.81, 'qualidadeVia': 7},
            'indaiatuba': {'distancia': 32, 'velocidadeMax': 43.83, 'tempo': 0.73, 'qualidadeVia': 7}
        }
    },
    
    'jaguariuna' : {
        'vizinhos': {
            'mogi mirim': {'distancia': 39, 'velocidadeMax': 78, 'tempo': 0.5, 'qualidadeVia': 8},
            'campinas': {'distancia': 29, 'velocidadeMax': 81.66, 'tempo': 0.6, 'qualidadeVia': 8}
        }
    },
    
    'campinas' : {
        'vizinhos': {
            'jaguariuna': {'distancia': 29, 'velocidadeMax': 48.33, 'tempo': 0.6, 'qualidadeVia': 8},
            'paulinia': {'distancia': 21, 'velocidadeMax': 45.65, 'tempo': 0.46, 'qualidadeVia': 8},
            'capivari': {'distancia': 53, 'velocidadeMax': 65.43, 'tempo': 0.81, 'qualidadeVia': 7},
            'jundiai': {'distancia': 40, 'velocidadeMax': 66.66, 'tempo': 0.6, 'qualidadeVia': 10},
            'itatiba': {'distancia': 38, 'velocidadeMax': 63.33, 'tempo': 0.6, 'qualidadeVia': 9}
        }
    },
    
    'indaiatuba' : {
        'vizinhos': {
            'capivari': {'distancia': 32, 'velocidadeMax': 43.83, 'tempo': 0.73, 'qualidadeVia': 7},
            'jundiai': {'distancia': 50.9, 'velocidadeMax': 66.9, 'tempo': 0.76 , 'qualidadeVia': 10}
        }
    },
    
    'jundiai' : {
        'vizinhos': {
            'campinas': {'distancia': 40, 'velocidadeMax': 66.66, 'tempo': 0.6, 'qualidadeVia': 10},
            'indaiatuba': {'distancia': 50.9, 'velocidadeMax': 66.97, 'tempo': 0.76, 'qualidadeVia': 10},
            'itatiba': {'distancia': 25.3, 'velocidadeMax': 52.70, 'tempo': 0.48 , 'qualidadeVia': 9},
            'atibaia': {'distancia': 61.9, 'velocidadeMax': 58.39, 'tempo': 1.06, 'qualidadeVia': 8},
            'sao paulo': {'distancia': 58.8 , 'velocidadeMax': 61.89, 'tempo': 0.95, 'qualidadeVia': 10}
        }
    },
    
    'itatiba' : {
        'vizinhos': {
            'campinas': {'distancia': 38, 'velocidadeMax': 63.33, 'tempo': 0.6, 'qualidadeVia': 9},
            'jundiai': {'distancia': 25.3, 'velocidadeMax': 52.70, 'tempo': 0.48, 'qualidadeVia': 9},
            'serra negra': {'distancia': 64.2, 'velocidadeMax': 50.15, 'tempo': 1.28, 'qualidadeVia': 7},
            'atibaia': {'distancia': 37.3, 'velocidadeMax': 62.16, 'tempo': 0.6, 'qualidadeVia': 8}
        }
    },
    
    'serra negra' : {
        'vizinhos': {
            'mogi mirim': {'distancia': 55, 'velocidadeMax': 67.90, 'tempo': 0.81, 'qualidadeVia': 6},
            'itatiba': {'distancia': 64.2, 'velocidadeMax': 50.15, 'tempo': 1.28, 'qualidadeVia': 7},
            'braganca paulista': {'distancia': 63.6, 'velocidadeMax': 52.13, 'tempo': 1.22, 'qualidadeVia': 7}
        }
    },
    
    'braganca paulista' : {
        'vizinhos': {
            'serra negra': {'distancia': 63.6, 'velocidadeMax': 52.13, 'tempo': 1.22, 'qualidadeVia': 7},
            'atibaia': {'distancia': 25.3, 'velocidadeMax': 47.73, 'tempo': 0.53, 'qualidadeVia': 8},
            'camanducaia': {'distancia': 57.4, 'velocidadeMax': 63.77, 'tempo': 0.9, 'qualidadeVia': 8}
        }
    },
    
    'atibaia' : {
        'vizinhos': {
            'itatiba': {'distancia': 37.3, 'velocidadeMax': 62.16, 'tempo': 0.6, 'qualidadeVia': 8},
            'braganca paulista': {'distancia': 25.3, 'velocidadeMax': 47.73, 'tempo': 0.53, 'qualidadeVia': 8},
            'jundiai': {'distancia': 61.9, 'velocidadeMax': 103.16, 'tempo': 0.6, 'qualidadeVia': 8},
            'guarulhos': {'distancia': 52.9, 'velocidadeMax': 51.86, 'tempo': 1.02, 'qualidadeVia': 8},
            'sao jose dos campos': {'distancia': 90.3, 'velocidadeMax': 78.52, 'tempo': 1.15, 'qualidadeVia': 8}
        }
    },
    
    'sao paulo' : {
        'vizinhos': {
            'jundiai': {'distancia': 58.8, 'velocidadeMax': 61.89, 'tempo': 0.95, 'qualidadeVia': 10},
            'guarulhos': {'distancia': 22.0, 'velocidadeMax': 33.33, 'tempo': 0.66, 'qualidadeVia': 10}
        }
    },
    
    'guarulhos' : {
        'vizinhos': {
            'sao paulo': {'distancia': 22.0, 'velocidadeMax': 33.33, 'tempo': 0.66, 'qualidadeVia': 10},
            'atibaia': {'distancia': 52.9, 'velocidadeMax': 51.86, 'tempo': 1.02, 'qualidadeVia': 8},
            'sao jose dos campos': {'distancia': 75.2, 'velocidadeMax': 69.62, 'tempo': 1.08, 'qualidadeVia': 9}
        }
    },
    
    'sao jose dos campos' : {
        'vizinhos': {
            'guarulhos': {'distancia': 75.2, 'velocidadeMax': 69.62, 'tempo': 1.08, 'qualidadeVia': 9},
            'atibaia': {'distancia': 90.3, 'velocidadeMax': 78.54, 'tempo': 1.15, 'qualidadeVia': 8},
            'taubate': {'distancia': 42.2, 'velocidadeMax': 64.92, 'tempo': 0.65, 'qualidadeVia': 10},
            'paraisopolis': {'distancia': 119.2, 'velocidadeMax': 60.81, 'tempo': 1.96, 'qualidadeVia': 7}
        }
    },
    
    'taubate' : {
        'vizinhos': {
            'sao jose dos campos': {'distancia': 42.2, 'velocidadeMax': 64.92, 'tempo': 0.65, 'qualidadeVia': 10},
            'santo antonio do pinhal': {'distancia': 35.4, 'velocidadeMax': 44.25, 'tempo': 0.8, 'qualidadeVia': 7}
        }
    },
    
    'santo antonio do pinhal' : {
        'vizinhos': {
            'taubate': {'distancia': 35.4, 'velocidadeMax': 44.25, 'tempo': 0.8, 'qualidadeVia': 7},
            'campos do jordao': {'distancia': 22.2, 'velocidadeMax': 54.14, 'tempo': 0.41, 'qualidadeVia': 7}
        }
    },
    
    'campos do jordao' : {
        'vizinhos': {
            'santo antonio do pinhal': {'distancia': 16.6, 'velocidadeMax': 38.60, 'tempo': 0.43, 'qualidadeVia': 7},
            'paraisopolis': {'distancia': 49.5, 'velocidadeMax': 46.69, 'tempo': 1.06, 'qualidadeVia': 6}
        }
    },
    
    'paraisopolis' : {
        'vizinhos': {
            'campos do jordao': {'distancia': 49.5, 'velocidadeMax': 46.69, 'tempo': 1.06, 'qualidadeVia': 6},
            'camanducaia': {'distancia': 60.7, 'velocidadeMax': 48.58, 'tempo': 1.25, 'qualidadeVia': 6},
            'sao jose dos campos': {'distancia': 119.2, 'velocidadeMax': 60.81, 'tempo': 1.96, 'qualidadeVia': 7}
        }
    },

    'camanducaia' : {
        'vizinhos': {
            'paraisopolis': {'distancia': 60.7, 'velocidadeMax': 48.56, 'tempo': 1.25, 'qualidadeVia': 6},
            'braganca paulista': {'distancia': 57.4, 'velocidadeMax': 63.77, 'tempo': 0.9, 'qualidadeVia': 8}
        }
    },
}

def menorDistancia():
    print("\nFunção para calcular rota com menor distância")

def maiorVelocidade():
    print("\nFunção para calcular rota com maior velocidade média")

def menorTempo():
    print("\nFunção para calcular rota com menor tempo")

def qualidadeVia():
    print("\nFunção para calcular rota com melhor qualidade de via")



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
        print("\n\t1) Limeira \n\t2) Mogi Mirim \n\t3) Paulinia \n\t4) Capivari \n\t5) Jaguariúna \n\t6) Campinas \n\t7) Indaiatuba \n\t8) Jundiai \n\t9) Itatiba \n\t9) Serra Negra \n\t10) Bragança Paulista \n\t11) Atibaia \n\t12) São Paulo \n\t13) Guarulhos \n\t14) São José dos Campos \n\t15) Taubaté \n\t16) Santo Antônio do Pinhal \n\t17) Campos do Jordão \n\t18) Paraisópolis \n\t19) Camanducaia")
        
        try:
            saida = int(input("\nCidade de saída: "))
            
        

            if (saida <= 0 or saida > 19):
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

    cidadeInexistente = True
    while cidadeInexistente: 
        print("\n\nQual a cidade de entrega do produto?")
        print("\n\t1) Limeira \n\t2) Mogi Mirim \n\t3) Paulinia \n\t4) Capivari \n\t5) Jaguariúna \n\t6) Campinas \n\t7) Indaiatuba \n\t8) Jundiai \n\t9) Itatiba \n\t10) Serra Negra \n\t11) Bragança Paulista \n\t12) Atibaia \n\t13) São Paulo \n\t14) Guarulhos \n\t15) São José dos Campos \n\t16) Taubaté \n\t17) Santo Antônio do Pinhal \n\t18) Campos do Jordão \n\t19) Paraisópolis \n\t20) Camanducaia")

        try:
            entrega = int(input("\nCidade de entrega: "))

            if (entrega <= 0 or entrega > 20):
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
    print("\n\t1) Menor distância \n\t2) Maior velocidade média \n\t3) Menor tempo \n\t4) Qualidade da via")

    try:
        regra = int(input("\nRegra:  "))

        if (regra <= 0 or regra > 4 ):
            print("\t\t __________________________________________")
            print("\n\t\t| ATENÇÃO: Opção inválida. Tente novamente |")
            print("\t\t __________________________________________")
            opcaoInvalida = True
        else:
            opcaoInvalida = False

    except ValueError:
            print("\t\t ________________________________________")
            print("\n\t\t| ATENÇÃO: Digite apenas números inteiros |")
            print("\t\t ________________________________________")

if (regra == 1):
    menorDistancia()
elif (regra == 2):
    maiorVelocidade()
elif (regra == 3):
    menorTempo()
elif (regra == 4):
    qualidadeVia()
