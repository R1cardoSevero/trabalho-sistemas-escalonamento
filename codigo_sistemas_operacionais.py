import datetime
import random

lista_processos = []

class Processo:
    def __init__(self, tempo_execucao, tempo_chegada, prioridade):
        self.id_processo = str(len(lista_processos) + 1)
        self.tempo_execucao = tempo_execucao
        self.tempo_chegada = tempo_chegada
        self.prioridade = prioridade

    def info(self):
        print("\n---//--- PROCESSO ID {} ---//---".format(self.id_processo))
        print("Tempo de execucao: {}".format(self.tempo_execucao))
        print("Tempo de chegada: {}".format(self.tempo_chegada))
        print("Prioridade: {}\n".format(self.prioridade))



def menu():
    while True:
        limpar_tela()
        print("---//--- MENU ---//---")
        print("1 - Adicionar um novo processo")
        print("2 - Remover um processo")
        print("3 - Listar processos")
        print("4 - Rodar FCFS")
        print("0 - Sair do Programa")
        resposta = input("Digite a opção: ")
        limpar_tela()
        match resposta:
            case "1":
                adicionar_processo()
            case "2":
                remover_processo()
            case "3":
                listar_processos()
            case "4":
                rodar_fcfs()
            case "0":
                break
            case _:
                print("Opção Inválida")
        input("Clique enter para continuar...")


def gerar_aleatorio():
    return random.randint(1, 100)

def entrada_usuario(texto1, texto2):
    while True:
        print(texto1)
        print(f"1 - Inserir {texto2}")
        print("2 - Gerar Aleatoriamente")
        resposta = input("Digite a opção: ")
        match resposta:
            case "1":
                while True:
                    try:
                        return int(input("Digite um número: "))
                    except:
                        print("Digite um número válido e inteiro")
            case "2":
                return gerar_aleatorio()
            case _:
                print("Opção Inválida")


def adicionar_processo():
    print("---//--- ADICIONAR PROCESSO ---//---")
    tempo_execucao = entrada_usuario("---//--- TEMPO EXECUÇÃO ---//---", "Tempo")
    tempo_chegada = entrada_usuario("---//--- TEMPO CHEGADA ---//---", "Tempo")
    prioridade = entrada_usuario("---//--- PRIORIDADE ---//---", "Prioridade")

    lista_processos.append(Processo(tempo_execucao, tempo_chegada, prioridade))
    print("---//--- PROCESSO CRIADO COM SUCESSO ---//---")

def listar_processos():
    print("---//--- LISTA DE PROCESSOS ---//---")
    if lista_processos:
        for processo in lista_processos:
            processo.info()
    else:
        print("\nNenhum processo foi encontrado")

def remover_processo():
    print("---//--- REMOVER PROCESSO ---//---")
    resposta = input("Insira o ID do Processo:")
    for processo in lista_processos:
        if processo.id_processo == resposta:
            print("\nProcesso removido com sucesso\n")
            lista_processos.remove(processo)
            return
    print("\nNenhum processo foi encontrado")

def rodar_fcfs():
    tempo_espera = 0
    tempo_atual = 0
    tempos_espera = []
    processos_ordenados = sorted(lista_processos, key=lambda p: p.tempo_chegada)

    if not lista_processos:
        print("\nNenhum processo na lista.\n")
        return

    print("---//--- RODAR FCFS ---//---")
    for processo in processos_ordenados:

        for i in range(processo.tempo_execucao, 0, -1):
            tempo_atual += 1
            print(f"tempo[{tempo_atual}] processo:[{processo.id_processo}] restante: {i}")
        tempos_espera.append(tempo_espera)
        tempo_espera += processo.tempo_execucao
    print("\n")
    for i, processo in enumerate(processos_ordenados):
        print(f'Processo[{processo.id_processo}]: tempo_espera={tempos_espera[i]}')
    print(f'Tempo médio de espera: {(sum(tempos_espera) / len(tempos_espera)):.2f}\n')

def limpar_tela():
    print("\n" * 50)

if __name__ == "__main__":
    lista_processos.append(Processo(5, 0, 3))
    lista_processos.append(Processo(3, 2, 1))
    lista_processos.append(Processo(8, 4, 2))
    lista_processos.append(Processo(6, 6, 4))
    lista_processos.append(Processo(2, 8, 5))
    lista_processos.append(Processo(4, 10, 2))
    lista_processos.append(Processo(7, 12, 3))
    lista_processos.append(Processo(3, 14, 1))
    lista_processos.append(Processo(5, 16, 4))
    lista_processos.append(Processo(4, 18, 2))
    menu()