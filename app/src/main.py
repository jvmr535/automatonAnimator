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
