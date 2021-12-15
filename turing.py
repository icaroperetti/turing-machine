class Turing():
    def __init__(self, tape, user_input, initial_state, final_state) -> None:
        self.tape = tape
        self.user_input = user_input
        self.current_state = initial_state
        self.final_state = final_state
        self.blank = '&'
        pass

    def execute(self):
        i = 0
        increment = 1
        current_tape = {}
        while i < len(self.user_input):

            for tape in self.tape:
                if tape.get('read') == self.user_input[i] and tape.get(
                        'current_state') == self.current_state:
                    current_tape = tape

            self.current_state = current_tape.get('next_state')

            # Substituir o valor no indice [i] do tape pelo valor que deve ser escrito
            self.user_input = self.user_input[:i] + \
                current_tape.get('write') + self.user_input[i + 1:]

            print('\n\n', self.current_state)
            print('\n\n', self.user_input)


            # Caso exista mais um indice a diante continua para a direita
            if current_tape.get('direction') == 'R':
                if not self.check_index(self.user_input, i + 1):
                    self.user_input += self.blank
                    increment = 1

             # Caso exista não exista indice atrás ele continua onde esta e vai concatenar com o valor do blank
             
            elif current_tape.get('direction') == 'L':
                if not self.check_index(self.user_input, i - 1):
                    increment = 0
                    self.user_input = self.blank + self.user_input
                else:
                    increment = -1
            else:
                increment = 0
            i += increment

            if self.current_state == self.final_state:
                print("entrei")
                return self.user_input

    # Gambirarra para verificar se o indice existe na string ja que o python retorna error caso nao exista
    def check_index(self, str, index):
        try:
            if str[index]:
                return True
        except:
            return False


tape = [{'current_state': 'q0', 'direction': 'R',
         'next_state': 'q1', 'read': '1', 'write': '0'},
        {'current_state': 'q1', 'direction': 'R', 'next_state': 'q2', 'read': '&', 'write': '1'}]


turing = Turing(tape, '1', 'q0', 'q2')
print(turing.execute())
