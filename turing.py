from re import S


class Turing():
    def __init__(self, delta, gama, q0, f) -> None:
        self.delta = delta
        self.gama = gama
        self.current_state = q0
        self.f = f
        self.sigma = ['1', '+']
        self.blank = '&'
        pass

    def execute(self):
        index = 0
        increment = 0
        current_tape = {}

        # Verificar se a entrada é válida
        for i in self.gama:
            if not i in self.sigma:
                raise Exception('Invalid input')

        while True:
            # Percorre as fitas para buscar o valor que precisa ser lido e o estado atual
            if index < 0:
                index += len(self.gama)

            for q in self.delta:
                if q.get('read') == self.gama[index] and q.get(
                        'current_state') == self.current_state:
                    current_tape = q

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

            # Atualiza o estado atual para o próximo estado da fita capturada
            self.current_state = current_tape.get('next_state')

            if self.current_state == self.f:
                return self.gama

    # Verificar se o indice existe na string ja que o python retorna error caso nao exista
    def check_index(self, string, index):
        try:
            if index < 0 or index >= len(string):
                return False
        except:
            return False


# Soma de 1
delta = [{'current_state': 'q0', 'read': '1', 'next_state': 'q0', 'write': '1', 'direction': 'R'},

         {'current_state': 'q0', 'read': '+',
         'next_state': 'q1', 'write': '1', 'direction': 'R'},

         {'current_state': 'q1', 'read': '1',
         'next_state': 'q1', 'write': '1', 'direction': 'R'},

         {'current_state': 'q1', 'read': '&',
          'next_state': 'q2', 'write': '&', 'direction': 'L'},
         {'current_state': 'q2', 'read': '1',
          'next_state': 'q3', 'write': '&', 'direction': 'S'},
         ]


turing = Turing(delta, '111+11', 'q0', 'q3')
print("Return:", turing.execute())
