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
        increment = 1
        current_tape = {}
        # Verificar se a entrada é válida
        for i in self.sigma:
            if not i in self.gama:
                raise Exception('Invalid input')

        # Percorrer a entrada do usuário
        while index < len(self.sigma):

            # Percorre as fitas para buscar o valor que precisa ser lido e o estado atual
            for q in self.q:
                if q.get('read') == self.sigma[index] and q.get(
                        'current_state') == self.current_state:
                    current_tape = q

            # Substituir o valor no indice [i] do tape pelo valor que deve ser escrito
            if index >= 0:
                self.sigma = self.sigma[:index] + \
                    current_tape.get('write') + self.sigma[index + 1:]

            # Caso não exista indice a direita do indice atual, concatena com o valor blank
            if current_tape.get('direction') == 'R':
                if not self.check_index(self.sigma, index + 1):
                    self.sigma += self.blank
                    increment = 1

             # Caso não exista indice atrás ele continua onde esta e vai concatenar com o valor do blank
            elif current_tape.get('direction') == 'L':
                if not self.check_index(self.sigma, index - 1):
                    increment = 0
                    self.sigma += self.blank

                # Se for necessário mover para a esquerda e existir um indice a esquerda, ele volta um indice para trás
                else:
                    increment = -1

            # Se for para parar (S) o índice apenas continua onde está
            else:
                increment = 0
            index += increment

            # Atualiza o estado atual para o próximo estado da fita capturada
            self.current_state = current_tape.get('next_state')

            if self.current_state == self.f:
                print(self.current_state)
                return self.sigma

    # Verificar se o indice existe na string ja que o python retorna error caso nao exista
    def check_index(self, str, index):
        try:
            if str[index]:
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


turing = Turing(tape, '1+1', 'q0', 'q3')
print("Return:", turing.execute())
