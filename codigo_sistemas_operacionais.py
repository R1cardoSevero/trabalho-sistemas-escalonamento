import datetime
import random

"""
    Owner: Ricardo Severo
    Version: 1.1
    Implemented: FCFS e SJF(Preemptivo e Não Preemptivo)
"""

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
        print("5 - Rodar SJF (Não Preemptivo)")
        print("6 - Rodar SJF (Preemptivo)")
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
            case "5":
                rodar_sjf("NAO-PREEMPTIVO")
            case "6":
                rodar_sjf("PREEMPTIVO")
            case "0":
                break
            case _:
                print("Opção Inválida")
        input("Clique enter para continuar...")

def gerar_aleatorio():
    return random.randint(1, 10)

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

def rodar_sjf(tipo):
    if tipo == "NAO-PREEMPTIVO":
        if not lista_processos:
            print("\nNenhum processo na lista.\n")
            return

        print("---//--- RODAR SJF (Não Preemptivo) ---//---")

        pendentes = list(lista_processos)
        tempo_atual = 0
        tempos_espera = []
        ordem_execucao = []

        while pendentes:
            disponiveis = [p for p in pendentes if p.tempo_chegada <= tempo_atual]

            if not disponiveis:
                print(f"tempo[{tempo_atual}]: nenhum processo está pronto")
                tempo_atual += 1
                continue

            processo = min(disponiveis, key=lambda p: p.tempo_execucao)
            pendentes.remove(processo)

            espera = tempo_atual - processo.tempo_chegada
            tempos_espera.append((processo, espera))
            ordem_execucao.append(processo)

            for i in range(processo.tempo_execucao, 0, -1):
                tempo_atual += 1
                print(f"tempo[{tempo_atual}] processo:[{processo.id_processo}] restante: {i}")

        print("\n")
        for processo, espera in tempos_espera:
            print(f'Processo[{processo.id_processo}]: tempo_espera={espera}')
        media = sum(e for _, e in tempos_espera) / len(tempos_espera)
        print(f'Tempo médio de espera: {media:.2f}\n')
    else:
        if not lista_processos:
            print("\nNenhum processo na lista.\n")
            return

        print("---//--- RODAR SJF (Preemptivo) ---//---")

        tempos_restantes = {p.id_processo: p.tempo_execucao for p in lista_processos}
        tempo_conclusao = {}
        tempo_atual = 0
        concluidos = 0
        total = len(lista_processos)

        while concluidos < total:
            disponiveis = [p for p in lista_processos if p.tempo_chegada <= tempo_atual and tempos_restantes[p.id_processo] > 0]

            if not disponiveis:
                print(f"tempo[{tempo_atual}]: nenhum processo está pronto")
                tempo_atual += 1
                continue

            processo = min(disponiveis, key=lambda p: tempos_restantes[p.id_processo])
            tempos_restantes[processo.id_processo] -= 1
            tempo_atual += 1
            print(f"tempo[{tempo_atual}] processo:[{processo.id_processo}] restante: {tempos_restantes[processo.id_processo]}")

            if tempos_restantes[processo.id_processo] == 0:
                tempo_conclusao[processo.id_processo] = tempo_atual
                concluidos += 1

        print("\n")
        tempos_espera = []
        for processo in lista_processos:
            espera = tempo_conclusao[processo.id_processo] - processo.tempo_chegada - processo.tempo_execucao
            tempos_espera.append(espera)
            print(f'Processo[{processo.id_processo}]: tempo_espera={espera}')
        print(f'Tempo médio de espera: {(sum(tempos_espera) / len(tempos_espera)):.2f}\n')

def limpar_tela():
    print("\n" * 50)

if __name__ == "__main__":
    lista_processos.append(Processo(10, 0, 1))
    lista_processos.append(Processo(2, 1, 2))
    lista_processos.append(Processo(1, 2, 3))
    lista_processos.append(Processo(4, 3, 1))
    lista_processos.append(Processo(3, 15, 2))
    menu()
