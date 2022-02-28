import os.path

#função para registrar um novo jogador no sistema, com pontuação igual a 0 e derrotas = 0
def criarNovoJogador():
    nome = input("Digite o nome do novo jogador: ")
    #verifica se um arquivo para esse jogador já existe
    if os.path.isfile("{}.txt".format(nome)):
        print("Jogador já registrado\n")
    else:
        print("Registrando o jogador {}\n".format(nome))
        f = open("{}.txt".format(nome), "w")
        f.write("0\n")#pontuação/vitórias
        f.write("0\n")#derrotas
        f.close()

#função para excluir um jogador
def excluirJogador():
    nome = input("Digite o nome do jogador a ser excluído: ")
    #verifica se o jogador a ser excluído existe
    if os.path.isfile("{}.txt".format(nome)):
        print("Excluindo o jogador {}\n".format(nome))
        os.remove("{}.txt".format(nome))
    else:
        print("Jogador {} não existe!\n".format(nome))

#função para ler a pontuação do jogador
def lePontuacao():
    nome = input("Digite o nome do jogador: ")
    #se o jogador existe, leia sua pontuação
    if os.path.isfile("{}.txt".format(nome)):
        f = open("{}.txt".format(nome), "r")
        print("Pontuação de {}:".format(nome))
        historico = f.readlines()#pego as linhas do arquivo para leitura
        vitorias = historico[0]
        derrotas = historico[1]
        print("Vitórias: {}\nDerrotas: {}".format(vitorias, derrotas))
    else:
        print("Jogador {} não existe".format(nome))

#matriz do jogo
matriz = [
    [" "," "," "," "," "],
    [" "," "," "," "," "],
    [" "," "," "," "," "],
    [" "," "," "," "," "],
    [" "," "," "," "," "]
]

#função do tabuleiro
def tabuleiro():
    #desenho do tabuleiro
    print("   0:   1:  2:  3:  4:")
    print("0:  " + matriz[0][0] + " | " + matriz[0][1] + " | " + matriz[0][2] + " | " + matriz[0][3] + " | " + matriz[0][4])
    print("  --------------------")
    print("1:  " + matriz[1][0] + " | " + matriz[1][1] + " | " + matriz[1][2] + " | " + matriz[1][3] + " | " + matriz[1][4])
    print("  --------------------")
    print("2:  " + matriz[2][0] + " | " + matriz[2][1] + " | " + matriz[2][2] + " | " + matriz[2][3] + " | " + matriz[2][4])
    print("  --------------------")
    print("3:  " + matriz[3][0] + " | " + matriz[3][1] + " | " + matriz[3][2] + " | " + matriz[3][3] + " | " + matriz[3][4])
    print("  --------------------")
    print("4:  " + matriz[4][0] + " | " + matriz[4][1] + " | " + matriz[4][2] + " | " + matriz[4][3] + " | " + matriz[4][4])

#função para resetar a matriz
def matriz_reset():
    for i in range(5):
        for j in range(5):
            matriz[i][j] = " "

#criando o jogo
def jogo():
    jogadas = 0
    #verificação dos jogadores, caso esteja tudo certo o jogo se inicia
    jog1 = input("Digite o nome do jogador: ")
    jog2 = input("Digite o nome do jogador: ")
    if os.path.isfile("{}.txt".format(jog1)) and os.path.isfile("{}.txt".format(jog2)):
        if jog1 == jog2:
            print("Um jogador não pode jogar contra ele mesmo!")
        else:
            while True:
                tabuleiro()
                #input de linha e coluna
                l = int(input("Digite a linha desejada: "))
                c = int(input("Digite a coluna desejada: "))
                
                #quem joga
                if jogadas % 2 == 0:
                    jogador = 'X'
                else:
                    jogador = 'O'
                
                #local já preenchido?
                if matriz[l][c] != " ":
                    print("Local já preenchido")
                    jogadas -= 1
                else:
                    matriz[l][c] = jogador
                
                #condições de vitória
                #linhas
                if matriz[0][0] + matriz[0][1] + matriz[0][2] + matriz[0][3] == 'XXXX' or matriz[0][1] + matriz[0][2] + matriz[0][3] + matriz[0][4] == 'XXXX' or matriz[1][0] + matriz[1][1] + matriz[1][2] + matriz[1][3] == 'XXXX' or matriz[1][1] + matriz[1][2] + matriz[1][3] + matriz[1][4] == 'XXXX' or matriz[2][0] + matriz[2][1] + matriz[2][2] + matriz[2][3] == 'XXXX' or matriz[2][1] + matriz[2][2] + matriz[2][3] + matriz[2][4] == 'XXXX' or matriz[3][0] + matriz[3][1] + matriz[3][2] + matriz[3][3] == 'XXXX' or matriz[3][1] + matriz[3][2] + matriz[3][3] + matriz[3][4] == 'XXXX' or matriz[4][0] + matriz[4][1] + matriz[4][2] + matriz[4][3] == 'XXXX' or matriz[4][1] + matriz[4][2] + matriz[4][3] + matriz[4][4] == 'XXXX':
                    ganhador = jog1
                    perdedor = jog2
                    print("O jogador:", ganhador, "venceu, os pontos foram contabilizados")

                    #pontuação - ganhador
                    f = open("{}.txt".format(ganhador), "r")
                    historico = f.readlines()  #leio o arquivo
                    f.close()
                    vitorias = int(historico[0]) + 1
                    derrotas = int(historico[1])
                    f = open("{}.txt".format(ganhador), "w")
                    f.write("{}\n{}".format(vitorias, derrotas))  #pontuação / vitorias
                    f.close()

                    #pontuação - perdedor
                    f = open("{}.txt".format(perdedor), "r")
                    historico = f.readlines()  #leio o arquivo
                    f.close()
                    vitorias = int(historico[0]) 
                    derrotas = int(historico[1]) + 1
                    f = open("{}.txt".format(perdedor), "w")
                    f.write("{}\n{}".format(vitorias, derrotas))  #pontuação / derrotas
                    f.close()

                    matriz_reset()
                    main()
                elif matriz[0][0] + matriz[0][1] + matriz[0][2] + matriz[0][3] == 'OOOO' or matriz[0][1] + matriz[0][2] + matriz[0][3] + matriz[0][4] == 'OOOO' or matriz[1][0] + matriz[1][1] + matriz[1][2] + matriz[1][3] == 'OOOO' or matriz[1][1] + matriz[1][2] + matriz[1][3] + matriz[1][4] == 'OOOO' or matriz[2][0] + matriz[2][1] + matriz[2][2] + matriz[2][3] == 'OOOO' or matriz[2][1] + matriz[2][2] + matriz[2][3] + matriz[2][4] == 'OOOO' or matriz[3][0] + matriz[3][1] + matriz[3][2] + matriz[3][3] == 'OOOO' or matriz[3][1] + matriz[3][2] + matriz[3][3] + matriz[3][4] == 'OOOO' or matriz[4][0] + matriz[4][1] + matriz[4][2] + matriz[4][3] == 'OOOO' or matriz[4][1] + matriz[4][2] + matriz[4][3] + matriz[4][4] == 'OOOO':
                    ganhador = jog2
                    perdedor = jog1
                    print("O jogador:", ganhador, "venceu, os pontos foram contabilizados")

                    #pontuação - ganhador
                    f = open("{}.txt".format(ganhador), "r")
                    historico = f.readlines()  #leio o arquivo
                    f.close()
                    vitorias = int(historico[0]) + 1
                    derrotas = int(historico[1])
                    f = open("{}.txt".format(ganhador), "w")
                    f.write("{}\n{}".format(vitorias, derrotas))  #pontuação / vitorias
                    f.close()

                    #pontuação - perdedor
                    f = open("{}.txt".format(perdedor), "r")
                    historico = f.readlines()  #leio o arquivo
                    f.close()
                    vitorias = int(historico[0]) 
                    derrotas = int(historico[1]) + 1
                    f = open("{}.txt".format(perdedor), "w")
                    f.write("{}\n{}".format(vitorias, derrotas))  #pontuação / derrotas
                    f.close()

                    matriz_reset()
                    main()
                else:
                    pass
                
                #colunas
                if matriz[0][0] + matriz[1][0] + matriz[2][0] + matriz[3][0] == 'XXXX' or matriz[1][0] + matriz[2][0] + matriz[3][0] + matriz[4][0] == 'XXXX' or matriz[0][1] + matriz[1][1] + matriz[2][1] + matriz[3][1] == 'XXXX' or matriz[1][1] + matriz[2][1] + matriz[3][1] + matriz[4][1] == 'XXXX' or matriz[0][2] + matriz[1][2] + matriz[2][2] + matriz[3][2] == 'XXXX' or matriz[1][2] + matriz[2][2] + matriz[3][2] + matriz[4][2] == 'XXXX' or matriz[0][3] + matriz[1][3] + matriz[2][3] + matriz[3][3] == 'XXXX' or matriz[1][3] + matriz[2][3] + matriz[3][3] + matriz[4][3] == 'XXXX' or matriz[0][4] + matriz[1][4] + matriz[2][4] + matriz[3][4] == 'XXXX' or matriz[1][4] + matriz[2][4] + matriz[3][4] + matriz[4][4] == 'XXXX':
                    ganhador = jog1
                    perdedor = jog2
                    print("O jogador:", ganhador, "venceu, os pontos foram contabilizados")

                    #pontuação - ganhador
                    f = open("{}.txt".format(ganhador), "r")
                    historico = f.readlines()  #leio o arquivo
                    f.close()
                    vitorias = int(historico[0]) + 1
                    derrotas = int(historico[1])
                    f = open("{}.txt".format(ganhador), "w")
                    f.write("{}\n{}".format(vitorias, derrotas))  #pontuação / vitorias
                    f.close()

                    #pontuação - perdedor
                    f = open("{}.txt".format(perdedor), "r")
                    historico = f.readlines()  #leio o arquivo
                    f.close()
                    vitorias = int(historico[0]) 
                    derrotas = int(historico[1]) + 1
                    f = open("{}.txt".format(perdedor), "w")
                    f.write("{}\n{}".format(vitorias, derrotas))  #pontuação / derrotas
                    f.close()

                    matriz_reset()
                    main()
                elif matriz[0][0] + matriz[1][0] + matriz[2][0] + matriz[3][0] == 'OOOO' or matriz[1][0] + matriz[2][0] + matriz[3][0] + matriz[4][0] == 'OOOO' or matriz[0][1] + matriz[1][1] + matriz[2][1] + matriz[3][1] == 'OOOO' or matriz[1][1] + matriz[2][1] + matriz[3][1] + matriz[4][1] == 'OOOO' or matriz[0][2] + matriz[1][2] + matriz[2][2] + matriz[3][2] == 'OOOO' or matriz[1][2] + matriz[2][2] + matriz[3][2] + matriz[4][2] == 'OOOO' or matriz[0][3] + matriz[1][3] + matriz[2][3] + matriz[3][3] == 'OOOO' or matriz[1][3] + matriz[2][3] + matriz[3][3] + matriz[4][3] == 'OOOO' or matriz[0][4] + matriz[1][4] + matriz[2][4] + matriz[3][4] == 'OOOO' or matriz[1][4] + matriz[2][4] + matriz[3][4] + matriz[4][4] == 'OOOO':
                    ganhador = jog2
                    perdedor = jog1
                    print("O jogador:", ganhador, "venceu, os pontos foram contabilizados")

                    #pontuação - ganhador
                    f = open("{}.txt".format(ganhador), "r")
                    historico = f.readlines()  #leio o arquivo
                    f.close()
                    vitorias = int(historico[0]) + 1
                    derrotas = int(historico[1])
                    f = open("{}.txt".format(ganhador), "w")
                    f.write("{}\n{}".format(vitorias, derrotas))  #pontuação / vitorias
                    f.close()

                    #pontuação - perdedor
                    f = open("{}.txt".format(perdedor), "r")
                    historico = f.readlines()  #leio o arquivo
                    f.close()
                    vitorias = int(historico[0]) 
                    derrotas = int(historico[1]) + 1
                    f = open("{}.txt".format(perdedor), "w")
                    f.write("{}\n{}".format(vitorias, derrotas))  #pontuação / derrotas
                    f.close()

                    matriz_reset()
                    main()
                else:
                    pass   

                #diagonais
                if matriz[1][0] + matriz[2][1] + matriz[3][2] + matriz[4][3] == 'XXXX' or matriz[0][0] + matriz[1][1] + matriz[2][2] + matriz[3][3] == 'XXXX' or matriz[1][1] + matriz[2][2] + matriz[3][3] + matriz[4][4] == 'XXXX' or matriz[0][1] + matriz[1][2] + matriz[2][3] + matriz[3][4] == 'XXXX' or matriz[0][3] + matriz[1][2] + matriz[2][1] + matriz[3][0] == 'XXXX' or matriz[0][4] + matriz[1][3] + matriz[2][2] + matriz[3][1] == 'XXXX' or matriz[1][3] + matriz[2][2] + matriz[3][1] + matriz[4][0] == 'XXXX' or matriz[1][4] + matriz[2][3] + matriz[3][2] + matriz[4][1] == 'XXXX':
                    ganhador = jog1
                    perdedor = jog2
                    print("O jogador:", ganhador, "venceu, os pontos foram contabilizados")

                    #pontuação - ganhador
                    f = open("{}.txt".format(ganhador), "r")
                    historico = f.readlines()  #leio o arquivo
                    f.close()
                    vitorias = int(historico[0]) + 1
                    derrotas = int(historico[1])
                    f = open("{}.txt".format(ganhador), "w")
                    f.write("{}\n{}".format(vitorias, derrotas))  #pontuação / vitorias
                    f.close()

                    #pontuação - perdedor
                    f = open("{}.txt".format(perdedor), "r")
                    historico = f.readlines()  #leio o arquivo
                    f.close()
                    vitorias = int(historico[0]) 
                    derrotas = int(historico[1]) + 1
                    f = open("{}.txt".format(perdedor), "w")
                    f.write("{}\n{}".format(vitorias, derrotas))  #pontuação / derrotas
                    f.close()

                    matriz_reset()
                    main()
                elif matriz[1][0] + matriz[2][1] + matriz[3][2] + matriz[4][3] == 'OOOO' or matriz[0][0] + matriz[1][1] + matriz[2][2] + matriz[3][3] == 'OOOO' or matriz[1][1] + matriz[2][2] + matriz[3][3] + matriz[4][4] == 'OOOO' or matriz[0][1] + matriz[1][2] + matriz[2][3] + matriz[3][4] == 'OOOO' or matriz[0][3] + matriz[1][2] + matriz[2][1] + matriz[3][0] == 'OOOO' or matriz[0][4] + matriz[1][3] + matriz[2][2] + matriz[3][1] == 'OOOO' or matriz[1][3] + matriz[2][2] + matriz[3][1] + matriz[4][0] == 'OOOO' or matriz[1][4] + matriz[2][3] + matriz[3][2] + matriz[4][1] == 'OOOO':
                    ganhador = jog2
                    perdedor = jog1
                    print("O jogador:", ganhador, "venceu, os pontos foram contabilizados")

                    #pontuação do ganhador
                    f = open("{}.txt".format(ganhador), "r")
                    historico = f.readlines()  #leio o arquivo
                    f.close()
                    vitorias = int(historico[0]) + 1
                    derrotas = int(historico[1])
                    f = open("{}.txt".format(ganhador), "w")
                    f.write("{}\n{}".format(vitorias, derrotas))  #pontuação / vitorias
                    f.close()

                    #pontuação do perdedor
                    f = open("{}.txt".format(perdedor), "r")
                    historico = f.readlines()  #leio o arquivo
                    f.close()
                    vitorias = int(historico[0]) 
                    derrotas = int(historico[1]) + 1
                    f = open("{}.txt".format(perdedor), "w")
                    f.write("{}\n{}".format(vitorias, derrotas))  #pontuação / derrotas
                    f.close()

                    matriz_reset()
                    main()
                else:
                    pass
                
                #empate
                if jogadas == 25:
                    print("Empate!")
                    matriz_reset()
                    main()
                else:
                    pass 
                  
                jogadas += 1
                
    else:
        print("Pelo menos um dos jogadores não foi encontrado, registre-se no menu")
              
#cria o programa principal
def main():
    while True:
        print("---------Menu---------")
        print("1- Criar novo jogador")
        print("2- Exibir pontuação")
        print("3- Excluir jogador")
        print("4- Inicie uma partida")

        #crio uma variável para guardar a escolha do menu
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            criarNovoJogador()
        elif opcao == '2':
            lePontuacao()
        elif opcao == '3':
            excluirJogador()
        elif opcao == '4':
            jogo()
        else:
            print("Opção inválida")

#execute o programa
main()