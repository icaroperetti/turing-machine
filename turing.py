class Turing():
    def __init__(self, tape, user_input, initial_state, final_state) -> None:
        self.tape = tape
        self.user_input = user_input
        self.current_state = initial_state
        self.final_state = final_state
        self.blank = '&'
        pass

    def execute(self):
        index = 0
        increment = 1
        current_tape = {}
        # Percorrer a entrada do usuário
        while index < len(self.user_input):
            print('index:', index)
            # Percorre as fitas para buscar o valor que precisa ser lido e o estado atual
            for tape in self.tape:
                if tape.get('read') == self.user_input[index] and tape.get(
                        'current_state') == self.current_state:
                    current_tape = tape

            # Atualiza o estado atual para o próximo estado da fita capturada
            self.current_state = current_tape.get('next_state')

            # Substituir o valor no indice [i] do tape pelo valor que deve ser escrito
            print("Antes:", self.user_input)
            print("Direction", current_tape.get('direction'))
            self.user_input = self.user_input[:index] + \
                current_tape.get('write') + self.user_input[index + 1:]

            print("Depois:", self.user_input)

            # Caso exista mais um indice a diante continua para a direita
            if current_tape.get('direction') == 'R':
                if not self.check_index(self.user_input, index + 1):
                    self.user_input += self.blank
                    increment = 1

             # Caso exista não exista indice atrás ele continua onde esta e vai concatenar com o valor do blank
            elif current_tape.get('direction') == 'L':
                if not self.check_index(self.user_input, index - 1):
                    increment = 0
                    self.user_input = self.blank + self.user_input
                # Se for necessário mover para a esquerda e existir um indice a esquerda, ele volta um indice para trás
                else:
                    increment = -1
            # Se for para parar o índice apenas continua onde está
            else:
                increment = 0
            index += increment
            print("Input final", self.user_input)
            if self.current_state == self.final_state:

                return self.user_input

    # Gambirarra para verificar se o indice existe na string ja que o python retorna error caso nao exista
    def check_index(self, str, index):
        try:
            if str[index]:
                return True
        except:
            return False


tape = [{'current_state': 'q0', 'direction': 'S',
         'next_state': 'q0', 'read': 'a', 'write': 'a'},
        {'current_state': 'q0', 'direction': 'S', 'next_state': 'q1', 'read': 'b', 'write': 'b'}, {
            'current_state': 'q1', 'direction': 'R', 'next_state': 'q1', 'read': 'b', 'write': 'b'},
        ]


turing = Turing(tape, 'aabb', 'q0', 'q1')
print(turing.execute())
