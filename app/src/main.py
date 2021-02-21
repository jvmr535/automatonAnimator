import pydot

graph = open("app/assets/graphs/graph_notation.txt", "r").read()


initial_and_final_states: list = [item.strip()
                                  for item in graph.splitlines()[0].split(";")]
initial_states: list = [
    item for item in initial_and_final_states[0].split(" ")]
final_states: list = [item for item in initial_and_final_states[1].split(" ")]

transitions: list = [item for item in graph.splitlines()[1:]]
del transitions[-1]

word: list = [item for item in graph.splitlines()[-1].split(":")[1].strip()]


def who_is_initial_state(initial_states: list, transitions: list):
    initial_state_on_states_array: str = ''
    for initial in initial_states:
        for transition in transitions:
            if initial == transition.split(" ")[0] and word[0] == transition.split(" ")[1]:
                initial_state_on_states_array = transition
                break
        break
    if initial_state_on_states_array:
        return initial_state_on_states_array.split(" ")[0]
    else:
        exit(1)


def next_state(current_state: str, transitions: list):
    for transition in transitions:
        if current_state == transition.split(" ")[0] and word[0] == transition.split(" ")[1]:
            word.pop(0)
            return transition.split(" ")[3]
    print('Automato não conseguiu ler a palavra')
    return exit(1)


current_state = who_is_initial_state(initial_states, transitions)
states_to_consume_the_word: list = []

while True:
    if len(word) != 0:
        current_state = next_state(current_state, transitions)
        states_to_consume_the_word.append(current_state)
    elif len(word) == 0 and current_state in final_states:
        break

print(states_to_consume_the_word)


def build_graph():
    graph = pydot.Dot('my_graph', graph_type='digraph')

    for transition in transitions:
        graph.add_node(pydot.Node(str(transition.split(
            " ")[0]), shape='circle', label=str(transition.split(" ")[0])))
        graph.add_node(pydot.Node(str(transition.split(
            " ")[3]), shape='circle', label=str(transition.split(" ")[3])))
        graph.add_edge(pydot.Edge(transition.split(" ")[0], transition.split(" ")[
                       3], label=transition.split(" ")[1]))

    for initial in initial_states:
        graph.add_node(pydot.Node(str(initial)))
    for final in final_states:
        graph.add_node(pydot.Node(str(final), shape='doublecircle'))

    graph.write_png('output.jpg')


build_graph()

# for initial in initial_states:
#     graph.add_node(pydot.Node(initial, shape='circle', label=initial,
#                               color='lightgrey', style='filled'))

# Add nodes
# my_node = pydot.Node('a', shape='circle', label='Foo',
#                      color='red', style='filled')
# graph.add_node(my_node)
# # Or, without using an intermediate variable:
# graph.add_node(pydot.Node('b', shape='circle'))

# # Add edges
# my_edge = pydot.Edge('a', 'b', color='blue')
# graph.add_edge(my_edge)
# # Or, without using an intermediate variable:
# graph.add_edge(pydot.Edge('b', 'c', color='blue'))

#
