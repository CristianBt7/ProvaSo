#Cristian Brandao Tavares
#Enzo Damasceno Falcao
#Francisco Osmar Santos Silva

#Simulador Desempenho Escalonamento

class Processo:
    def __init__(self, nome,ordem,tempo_de_execucao):
        self.nome = nome
        self.ordem = ordem
        self.tempo_de_execucao = tempo_de_execucao
        self.tempo_de_espera = 0
        self.turnaround = 0
    
    def __str__(self):
        return f'{self.nome:<10} {self.ordem:^6} {self.tempo_de_execucao:^16} {self.tempo_de_espera:^14} {self.turnaround:^10}'
        
def fifo(processos):
    tempo_ocorrido = 0
    processos.sort(key= lambda processo: processo.ordem)
    
    for processo in processos:
        if processo.ordem == 1:
            processo.tempo_de_espera = 0
            processo.turnaround = processo.tempo_de_execucao
            tempo_ocorrido += processo.tempo_de_execucao
        else:
            processo.tempo_de_espera = tempo_ocorrido
            processo.turnaround = processo.tempo_de_execucao + processo.tempo_de_espera
            tempo_ocorrido += processo.tempo_de_execucao

def sjf(processos):
    processos.sort(key=lambda processo: processo.tempo_de_execucao)
    
    tempo_ocorrido = 0
    for processo in processos:
        processo.tempo_de_espera = tempo_ocorrido
        processo.turnaround = processo.tempo_de_execucao + processo.tempo_de_espera
        tempo_ocorrido += processo.tempo_de_execucao


def tabela(processos):
    print("\nResultado:")
    print("-" * 70)
    print(f"{'Nome':<10} {'Ordem':^6} {'Tempo Execução':^16} {'Tempo Espera':^14} {'Turnaround':^10}")
    print("-" * 70)
    for processo in lista_de_processos:
        print(processo)
    print("-" * 70)
    tempo_total_do_turnaround = 0
    tempo_total_de_espera = 0
    for tempo_processos in processos:
        tempo_total_do_turnaround += tempo_processos.turnaround
        tempo_total_de_espera += tempo_processos.tempo_de_espera
    print(f'O tempo medio de turnaround: {tempo_total_do_turnaround/len(processos):0.2f}')
    print(f'O tempo medio de espera: {tempo_total_de_espera/len(processos): 0.2f}')


lista_de_processos = []

print('Simulador Desempenho Escalonamento')

quantidade_de_processos = int(input('Digite a quantidade de processos: '))

while quantidade_de_processos > 0:
    quantidade_de_processos -= 1
    
    nome = input('Digite o nome do processo: ')
    ordem = int(input('Digite a ordem do processo: '))
    tempo_de_execucao = int(input('Digite o tempo de execuçao: '))
    print()
    
    processo = Processo(nome,ordem,tempo_de_execucao)
    lista_de_processos.append(processo)

print('Algoritmo FIFO')
fifo(lista_de_processos)
tabela(lista_de_processos)

print()

print('Algoritmo SJF')
sjf(lista_de_processos)
tabela(lista_de_processos)

