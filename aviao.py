from threading import Thread
from time import sleep

import simulacao as sim
from aeroporto import *

class Aviao(Thread):
    '''
        Aviões devem ser criados periodicamente e realizar as seguintes ações:
        - Se aproximar do aeroporto e esperar a sua vez de pousar.
          Verifique no enunciado a ordem de pouso.
        - O avião deve pousar (por um determinado tempo) na pista reservada
          para ele.
        - O avião que acabou de pousar deve tentar ir para um portão livre.
        - O avião deve alocar uma esteira para descarregar as bagagens dos
          passageiros.
        - O avião deve carregar as bagagens do próximo vôo.
        - O avião deve desacoplar do portão e tentar decolar.
        - O avião deve sair do portão para uma pista livre e decolar.

        A sua responsabilidade é desenvolver os comportamentos dentro das
        funções do avião e proteger os contadores globais.
    '''

    def __init__(self, id, combustivel):
        # Atributos default
        self.id          = id
        self.combustivel = combustivel

        # Atributos nulos, não altere essas variáveis. Elas devem ser alteradas
        # apenas durante alocação e liberação de recursos. Ou seja, ao liberar
        # um recurso, sobreescreva o valor antigo com um recurso nulo
        # (construtor vázio).
        self.pista   = Pista()
        self.portao  = Portao()
        self.esteira = Esteira()
        super().__init__(name=("Avião " + str(id)))

    def overview(self):
        descricao = self.name + " ("
        descricao += "Combustível " + str(self.combustivel) + "%, "
        descricao += self.pista.overview()                  + ", "
        descricao += self.portao.overview()                 + ", "
        descricao += self.esteira.overview()                + ")"
        return descricao

    def log(self, frase, espacos = 0):
        print('[', self.overview(), '] ', frase,
            " " * espacos, ' | ', aeroporto.overview(), sep = ''
        )

    def run(self):
        '''
            NÃO ALTERE A ORDEM DAS CHAMADAS A BAIXO.

            Você deve implementar os comportamentos dentro das funções aqui
            invocadas. Lembre-se de usar a variável global "aeroporto" para ter
            acesso a funções e recursos.
            Observação: Comente no código qual o objetivo de uma dada
            operação, ou conjunto de operações, para facilitar a correção do
            trabalho.
        '''
        sim.contadores["entrando"] += 1

        self.log("Entrou no espaço aéreo", 17)

        self.aproximar()
        self.pousar()
        self.acoplar()
        self.descarregar_bagagens()
        self.carregar_bagagens()
        self.desacoplar()
        self.decolar()

        sim.contadores["saindo"] += 1

        self.log("Saindo do espaço aéreo", 17)

    def atualiza_contador(contador):
        def decorador(operacao):
            def envelope(self):
                sim.contadores[contador] += 1
                operacao(self)
                sim.contadores[contador] -= 1
            return envelope
        return decorador

    @atualiza_contador("aproximando")
    def aproximar(self):
        self.log("Aproxima-se", 28)
        '''
            IMPLEMENTE ABAIXO:
            O avião deve tentar reservar uma pista, respeitando a ordem de
            prioridade definida no enunciado. Se não houver pistas livres,
            o avião deve aguardar até que seja a sua vez de alocar a próxima
            pista liberada.
        '''

        # IMPLEMENTE AQUI A RESERVA DE UMA PISTA.

    @atualiza_contador("pousando")
    def pousar(self):
        '''
            Avião só chega aqui quando tiver reservado uma pista.
        '''
        self.log("Pousa na " + self.pista.overview(), 22)
        '''
            IMPLEMENTE ABAIXO:
            O avião deve "pousar" por um período de tempo e taxiar até um
            portão livre. Após o pouso, a pista pode ser liberada para outro
            avião enquanto o avião atual aguarda um portão liberar.
        '''

        # IMPLEMENTE AQUI O POUSO E SAÍDA DO AVIÃO DA PISTA.

    @atualiza_contador("acoplando")
    def acoplar(self):
        '''
            IMPLEMENTE ABAIXO:
            O avião que acabou de sair da pista após sua aterrisagem deve
            aguardar um portão liberar. A ordem de reserva dos portões deve
            respeitar a ordem de requisição.
        '''

        # IMPLEMENTE AQUI A RESERVA DO PORTÃO.

        '''
            Avião só chega aqui quando tiver reservado um portão.
        '''
        self.log("Acopla no " + self.portao.overview(), 20)

    @atualiza_contador("descarregando")
    def descarregar_bagagens(self):
        '''
            IMPLEMENTE ABAIXO:
            O avião deve buscar uma esteira que possua espaço livre para
            descarregar as bagagens dos passageiros. Lembre que uma esteira
            suporta uma quantidade definida de aviões ao mesmo tempo.
        '''

        # IMPLEMENTE AQUI A RESERVA DA ESTEIRA.

        '''
            Avião só chega aqui quando tiver reservado uma esteira.
        '''
        self.log("Descarrega bagagens pela " + self.esteira.overview(), 0)
        '''
            IMPLEMENTE ABAIXO:
            O avião deve descarregar as bagagens dos passageiros.
        '''

        # IMPLEMENTE AQUI O DESCARREGAMENTO DAS BAGAGENS.

    @atualiza_contador("carregando")
    def carregar_bagagens(self):
        '''
            Avião só chega aqui quando tiver descarregado as bagagens.
        '''
        self.log("Carrega bagagens pela " + self.esteira.overview(), 3)
        '''
            IMPLEMENTE ABAIXO:
            O avião deve carregar as bagagens dos novos passageiros. Após
            o embarque das bagagens e dos passageiros, o avião pode liberar
            a esteira e desacoplar.
        '''

        # IMPLEMENTE AQUI O CARREGAMENTOS DAS BAGAGENS.

    @atualiza_contador("desacoplando")
    def desacoplar(self):
        '''
            Avião só chega aqui quando tiver carregado as bagagens.
        '''
        self.log("Desacoplando do " + self.portao.overview(), 14)
        '''
            IMPLEMENTE ABAIXO:
            O avião deve liberar o portão e taxiar até a pista. Caso não haja
            uma pista disponível, o avião deve aguardar seguindo a ordem de
            prioridade definida no enunciado do trabalho.
        '''

        # IMPLEMENTE A LIBERAÇÃO DO PORTÃO E RESERVA DA PISTA.

    @atualiza_contador("decolando")
    def decolar(self):
        '''
            Avião só chega aqui quando tiver reservado uma pista.
        '''
        self.log("Decolando pela " + self.pista.overview(), 16)
        '''
            IMPLEMENTE ABAIXO:
            O avião deve decolar e liberar a pista.
        '''

        # IMPLEMENTE A DECOLAGEM E LIBERAÇÃO DA PISTA.

