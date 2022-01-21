
# q0: estados da máquina
# Blank: caracter que representa o espaço vazio
# girininho: regras de transição
# q: fita de dados
# f: estado final

def turing_machine(Q=None, q0=None, blank=None, girininho=[], gama=[], sigma=[], f=None, position=0):

    # Se não houver elementos no fita, adiciona um espaço vazio
    if not gama:
        gama = [blank]

    # Verificar se oq foi digitado é um valor válido
    for i in sigma:
        if not i in gama:
            raise Exception('Invalid input')

    # Se a posição é menor que zero, define a posição como o tamanho da fita
    if position < 0:
        position += len(gama)

    # Garantir que a fita tenha alguma informação
    if position >= len(gama) or position < 0:
        raise Exception('Invalid position')

    """
      Estado	  Valor lido   	Valor  escrito	  Direção 	Estado seguinte.
        (s0)	     (v0)	         (v1)         (dr)	     (s1)
    """

    # Percorre as regras para encontrar a regra que deve ser aplicada
    rules = dict(((s0, v0), (v1, dr, s1))
                 for (s0, v0, v1, dr, s1) in girininho)

    while(True):
        # print(q0, '\t', end=" ")
        # exit(0)

        # Laço de repetição para percorrer toda a fita
        for i, v in enumerate(gama):
          # Se i for igual a posição atual, imprime o valor contido na posição
            if i == position:
                print("[%s]" % v, end=" ")
            else:
                print(v, end=" ")
        print()

        # Se o estado atual for igual o estado final para
        if q0 == f and position > len(gama):
            break

        # Se o estado não estiver na regra para

        if (q0, gama[position]) not in rules:
            break

        # Define as váriaveis de acordo com a regra
        (v1, dr, s1) = rules[(q0, gama[position])]
        gama[position] = v1  # Recebe o valor de entrada da fita

        # Direções

        # Se for para a esquerda e a posição for maior que zero, decrementa a posição
        if dr == 'left':
            print("Entrei na direção left", gama[position])
            if position > 0:
                position -= 1
            # Se não existir indice a esquerda, concatena com o valor do blank
            else:
                gama.insert(0, blank)

        # Se for para a direita incrementa a posição
        elif dr == 'right':
            print("Entrei na direção right", gama[position])
            position += 1
            # Se a posição for maior que o tamanho da fita, adiciona um espaço vazio
            if position >= len(gama):
                gama.append(blank)
        elif s1 == f:
            print("Entrei no estado final", gama[position])
            break
        else:
            position += 0
        q0 = s1


print("Máquina de Turing Ícaro\n")
# turing_machine(q0='q0',  # estado inicial da máquina
#                blank='&',  # Simbolo que representa o vazio
#                q=list("0A"),  # Fita de dados
#                f='q2',  # Estado f da máquina
#                girininho=map(tuple,  # Regras de transição
#                          [
#                              "q0 0 1 right q1".split(),
#                              "q1 A 2 left q2".split(),
#                          ]
#                          )
#                )


print("Máquina de Turing com parada")
# turing_machine(
#     Q="q0,q1,q2,q3,q4",
#     sigma=[0, 1, '&'],
#     q0='q0',  # estado inicial da máquina
#     blank='&',  # Simbolo que representa o vazio
#     gama=list("0"),  # Fita de dados
#     f='q4',  # Estado f da máquina
#     girininho=map(tuple,  # Regras de transição
#                   [
#                       "q0 0 1 left q1".split(),
#                       "q1 & 1 right q2".split(),
#                       "q2 1 0 stop q3".split(),
#                       "q3 0 5 right q4".split(),
#                   ]
#                   )
# )

print("Máquina de Turing soma 1")
# turing_machine(q0='q0',  # estado inicial da máquina
#                blank='&',  # Simbolo que representa o vazio
#                sigma=['1', '+'],
#                gama=list("1+1+1"),  # Fita de dados
#                f='q2',  # Estado f da máquina
#                girininho=map(tuple,  # Regras de transição
#                              [
#                                  "q0 1 1 right q0".split(),
#                                  "q0 + 1 right q1".split(),
#                                  "q1 1 1 right q1".split(),
#                                  "q1 & & left q2".split(),
#                                  "q2 1 & stop q2".split(),
#                              ]
#                              )
#                )


# print("Máquina de Turing soma le 0 e A retorna 1 e 2")
turing_machine(q0='q0',  # estado inicial da máquina
               blank='&',
               sigma=['0', 'A'],  # Simbolo que representa o vazio
               gama=list("0A"),  # Fita de dados
               f='q2',  # Estado f da máquina
               girininho=map(tuple,  # Regras de transição
                             [
                                 "q0 0 1 right q1".split(),
                                 "q1 A 2 right q2".split(),
                             ]
                             )
               )
