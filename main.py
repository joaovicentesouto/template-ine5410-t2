from time import sleep

# Argumentos
import sys

# Parâmetros da simulação
import simulacao as sim

# Argumentos
from aeroporto import *
from aviao import *

def main(argv):
    # Tenta ler os argumentos
    sim.ler_argumentos(argv)

    '''
        Implemente a criação periódica de aviões usando valores aleatórios entre
        "novo_aviao_min" e "novo_aviao_max". Aviões deverão ser criados enquanto o
        tempo de simulação não tiver sido esgotado ("tempo_total").

        IMPORTANTE: Utilize tempos em milissegundos.
    '''

    # Tempo de simulação
    tempo = 0

    # Enquanto o tempo total de simuação não for atingido
    while tempo < sim.tempo_total:
        # Crie um avião
        
        # Aguarde um tempo aleatório entre "novo_aviao_min" e "novo_aviao_max"
        # antes de criar o próximo avião
        
        # Atualize o tempo total de simulação considerando o intervalo de espera
        # para a criação do avião
        
    # Aguarde a finalização (término) de todos os aviões antes de finalizar
    # a execução do programa

if __name__ == "__main__":
    # Verifica a versão do python
    if sys.version_info < (3, 0):
        sys.stdout.write('Utilize python3 para desenvolver este trabalho\n')
        sys.exit(1)

    # Main
    main(sys.argv[1:])

