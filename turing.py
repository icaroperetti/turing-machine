class Turing():
    def __init__(self, q, gama, q0, f) -> None:
        self.q = q
        self.gama = gama
        self.current_state = q0
        self.f = f
        self.sigma = ['a', 'b', 'c']
        self.blank = '&'
        pass

    def execute(self):
        index = 0
        increment = 0
        current_tape = {}
        print('inicial', self.current_state)
        # Verificar se a entrada é válida
        # for i in self.gama:
        #     if not i in self.sigma:
        #         raise Exception('Invalid input')

        # Percorrer a entrada do usuário
        while index < len(self.gama):

            # Percorre as fitas para buscar o valor que precisa ser lido e o estado atual
            for q in self.q:
                if q.get('read') == self.gama[index] and q.get(
                        'current_state') == self.current_state:
                    current_tape = q
            print('current_tap', current_tape)

            # Substituir o valor no indice [i] do tape pelo valor que deve ser escrito
            if index >= 0:
                self.gama = self.gama[:index] + \
                    current_tape.get('write') + self.gama[index + 1:]

            # Caso não exista indice a direita do indice atual, concatena com o valor blank
            if current_tape.get('direction') == 'R':

                if self.check_index(self.gama, index + 1) == False:
                    self.gama += self.blank
                increment = 1

             # Caso não exista indice atrás ele continua onde esta e vai concatenar com o valor do blank
            elif current_tape.get('direction') == 'L':

                if self.check_index(self.gama, index - 1) == False:
                    self.gama = self.blank + self.gama
                    increment = 0

                # Se for necessário mover para a esquerda e existir um indice a esquerda, ele volta um indice para trás
                elif current_tape.get('direction') == 'L':
                    increment = -1

            # Se for para parar (S) o índice apenas continua onde está
            else:
                increment = 0
            index += increment

            #self.current_state = current_tape.get('next_state')

            if self.current_tape.get('next_state') == self.f:
                return self.gama
            # Atualiza o estado atual para o próximo estado da fita capturada

    # Verificar se o indice existe na string ja que o python retorna error caso nao exista

    def check_index(self, string, index):
        try:
            if index < 0:
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
# tape = [{'current_state': 'q0', 'read': '1', 'next_state': 'q0', 'write': '1', 'direction': 'R'},

#         {'current_state': 'q0', 'read': '+',
#             'next_state': 'q1', 'write': '1', 'direction': 'R'},

#         {'current_state': 'q1', 'read': '1',
#         'next_state': 'q1', 'write': '1', 'direction': 'R'},

#         {'current_state': 'q1', 'read': '&',
#         'next_state': 'q2', 'write': '&', 'direction': 'L'},
#         {'current_state': 'q2', 'read': '1',
#         'next_state': 'q3', 'write': '&', 'direction': 'S'},
#         ]


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

tape = [{
    'current_state': 'q0',
    'read': 'a',
    'next_state': 'q0',
    'write': '1',
    'direction': 'R'
},
    {
    'current_state': 'q0',
    'read': 'b',
    'next_state': 'q0',
    'write': '2',
    'direction': 'R'
},
    {
    'current_state': 'q0',
    'read': 'c',
    'next_state': 'q0',
    'write': '3',
    'direction': 'R'

},
    {
    'current_state': 'q0',
    'read': '&',
    'next_state': 'q1',
    'write': '&',
    'direction': 'S'
}

]

turing = Turing(tape, 'abcabc&', 'q0', 'q1')
print("Return:", turing.execute())
