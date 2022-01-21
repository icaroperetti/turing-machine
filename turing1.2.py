from turtle import position


class Turing():
    def __init__(self, q, sigma, q0, f) -> None:
        self.q = q
        self.sigma = sigma
        self.current_state = q0
        self.f = f
        self.gama = ['1', '+']
        self.blank = '&'
        pass

    def execute(self):
        index = 0
        index = 0
        current_tape = {}
        print('inicial', self.current_state)
        # Verificar se a entrada é válida
        # for i in self.sigma:
        #     if not i in self.gama:
        #         raise Exception('Invalid input')

        # Percorrer a entrada do usuário

        while index < len(self.sigma):
            index += len(self.gama)

            # if index >= len(self.gama) or index < 0:
            #     raise Exception('Invalid position')
            # Percorre as fitas para buscar o valor que precisa ser lido e o estado atual
            print('index antes', index)
            for q in self.q:
                if q.get('read') == self.sigma[index] and q.get(
                        'current_state') == self.current_state:
                    current_tape = q
            print('current_tap', current_tape)

            # Substituir o valor no indice [i] do tape pelo valor que deve ser escrito
            print('antes', self.sigma)
            if index >= 0:
                self.sigma = self.sigma[:index] + \
                    current_tape.get('write') + self.sigma[index + 1:]
            print('depois', self.sigma)

            # Caso não exista indice a direita do indice atual, concatena com o valor blank
            if current_tape.get('direction') == 'R':
                index += 1
                if index >= len(self.gama):
                    self.gama += self.blank

                # Caso não exista indice atrás ele continua onde esta e vai concatenar com o valor do blank
            elif current_tape.get('direction') == 'L':
                if index > 0:
                    index -= 1
                else:
                    self.gama = self.blank + self.gama
                # Se for necessário mover para a esquerda e existir um indice a esquerda, ele volta um indice para trás
            else:
                index += 0

            print('index depos\n', index)

            print('state antes do print\n', self.current_state)

            self.current_state = current_tape.get('next_state')

            # Verificar se o estado atual é o estado final
            if self.current_state == self.f:
                print(self.current_state, "DENTRO DO IF")
                return self.sigma

            # Atualiza o estado atual para o próximo estado da fita capturada
            print('state depois\n', self.current_state)

    # Verificar se o indice existe na string ja que o python retorna error caso nao exista
    def check_index(self, string, index):
        try:
            if index < 0 or index > len(string):
                return False
            if string[index]:
                return True
        except:
            return False


# Deve retornar 12
# tape = [{'current_state': 'q0', 'direction': 'R', 'write': '1', 'read': '0', 'next_state': 'q1'},
#         {'current_state': 'q1', 'direction': 'L',
#             'write': '2', 'read': 'A'},
#         ]


# Deve retornar &&1
# tape = [{'current_state': 'q0', 'direction': 'L', 'write': '1', 'read': '0', 'next_state': 'q1'},
#         {'current_state': 'q1', 'direction': 'L',
#             'write': '&', 'read': '&', 'next_state': 'q2'},
#         ]

# Soma de 1
tape = [{'current_state': 'q0', 'read': '1', 'next_state': 'q0', 'write': '1', 'direction': 'R'},

        {'current_state': 'q0', 'read': '+',
            'next_state': 'q1', 'write': '1', 'direction': 'R'},

        {'current_state': 'q1', 'read': '1',
        'next_state': 'q1', 'write': '1', 'direction': 'R'},

        {'current_state': 'q1', 'read': '&',
        'next_state': 'q2', 'write': '&', 'direction': 'L'},
        {'current_state': 'q2', 'read': '1',
        'next_state': 'q3', 'write': '&', 'direction': 'S'},
        ]


# tape = [
#     {'current_state': 'q0', 'read': '0',
#         'next_state': 'q1', 'write': '1', 'direction': 'L'},

#     {'current_state': 'q1', 'read': '&', 'next_state': 'q2',
#         'write': '1', 'direction': 'R'},

#     {'current_state': 'q2', 'read': '1',
#         'next_state': 'q3', 'write': '0', 'direction': 'S'},

#     {'current_state': 'q3', 'read': '0',
#         'next_state': 'q4', 'write': '5', 'direction': 'R'},
# ]

turing = Turing(tape, '11+11', 'q0', 'q3')
print("Return:", turing.execute())
