
# State: estados da máquina
# Blank: caracter que representa o espaço vazio
# Rules: regras de transição
# Tape: fita de dados
# Final: estado final
# Position: posição seguinte da fita

def turing_machine(state=None, blank=None, rules=[], tape=[], final=None, position=0):

    # Se não houver elementos no fita, adiciona um espaço vazio
    if not tape:
        tape = [blank]

    # Se a posição é menor que zero, define a positição como o tamanho da fita
    if position < 0:
        position += len(tape)

    # Garantir que a fita tenha alguma informação
    if position >= len(tape) or position < 0:
        raise Exception('Invalid position')

    """
      Estado	  Valor lido   	Valor  escrito	  Direção 	Estado seguinte.
        (s0)	     (v0)	         (v1)         (dr)	     (s1)
    """

    # Percorre as regras para encontrar a regra que deve ser aplicada
    rules = dict(((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in rules)

    while(True):
        # print(state, '\t', end=" ")
        # exit(0)

        # Laço de repetição para percorrer toda a fita
        for i, v in enumerate(tape):
          # Se i for igual a posição atual, imprime o valor contido na posição
            if i == position:
                print("[%s]" % v, end=" ")
            else:
                print(v, end=" ")
        print()

        # Se o estado atual for igual o estado final para
        if state == final:
            break

        # Se o estado não estiver na regra para
        if (state, tape[position]) not in rules:
            break

        # Define as váriaveis de acordo com a regra
        (v1, dr, s1) = rules[(state, tape[position])]
        print("%s -> %s Valor escrito:%s Proximo:%s" %
              (state, tape[position], v1, s1))

        tape[position] = v1  # Sobrescreve o valor da fita

        # Direções

        # Se for para a esquerda e a posição for maior que zero, decrementa a posição
        if dr == 'left':
            if position > 0:
                position -= 1

            # Se não existir indice a esquerda, concatena com o valor do blank
            else:
                tape.insert(0, blank)
        # Se para a direita incremenda a posição
        elif dr == 'right':
            position += 1

            # Se a posição for maior que o tamanho da fita, adiciona um espaço vazio
            if position >= len(tape):
                tape.append(blank)
        else:
            position += 0
        state = s1


print("Máquina de Turing Ícaro\n")
# turing_machine(state='q0',  # estado inicial da máquina
#                blank='&',  # Simbolo que representa o vazio
#                tape=list("0A"),  # Fita de dados
#                final='q2',  # Estado final da máquina
#                rules=map(tuple,  # Regras de transição
#                          [
#                              "q0 0 1 right q1".split(),
#                              "q1 A 2 left q2".split(),
#                          ]
#                          )
#                )


print("Máquina de Turing com parada")
turing_machine(state='q0',  # estado inicial da máquina
               blank='&',  # Simbolo que representa o vazio
               tape=list("0"),  # Fita de dados
               final='q4',  # Estado final da máquina
               rules=map(tuple,  # Regras de transição
                         [
                             "q0 0 1 left q1".split(),
                             "q1 & 1 right q2".split(),
                             "q2 1 0 stop q3".split(),
                             "q3 0 5 right q4".split(),
                         ]
                         )
               )

print("Máquina de Turing soma 1")
# turing_machine(state='q0',  # estado inicial da máquina
#                blank='&',  # Simbolo que representa o vazio
#                tape=list("1+1+1"),  # Fita de dados
#                final='q3',  # Estado final da máquina
#                rules=map(tuple,  # Regras de transição
#                          [
#                              "q0 1 1 right q0".split(),
#                              "q0 + 1 right q1".split(),
#                              "q1 1 1 right q1".split(),
#                              "q1 & & left q2".split(),
#                              "q2 1 & stop q3".split(),
#                          ]
#                          )
#                )
