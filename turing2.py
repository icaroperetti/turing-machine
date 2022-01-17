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
        while i < len(self.user_input):
            [tape] = [x for x in self.tape if x.get('read') == self.user_input[i] and x.get(
                'current_state') == self.current_state]
            print(tape)
            self.current_state = tape.get('next_state')
            self.user_input = self.user_input[:i] + \
                tape.get('write') + self.user_input[i + 1:]
            if tape.get('direction') == 'R':
                if not self.check_index(self.user_input, i + 1):
                    self.user_input += self.blank
                    increment = 1
            elif tape.get('direction') == 'L':
                if not self.check_index(self.user_input, i - 1):
                    increment = 0
                    self.user_input = self.blank + self.user_input
                else:
                    increment = -1
            else:
                increment = 0
            i += increment
            print(self.user_input)
            print(tape.get('current_state'))
            if self.current_state == self.final_state:
                return self.user_input

    def check_index(self, str, index):
        try:
            if str[index]:
                return True
        except:
            return False


tape = [{'current_state': 'q0', 'direction': 'R',
         'next_state': 'q1', 'write': '0', 'read': '1'}]

turing = Turing(tape, '1', 'q0', 'q1')
turing.execute()
