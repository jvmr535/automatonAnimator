import glob

import pydot
from PIL import Image

from State import State
from Transition import Transition
from Node import Node


graph_model = open("app/assets/graphs/exemplo_afd.txt", "r").read()


initial_and_final_states: list = [item.strip()
                                  for item in graph_model.splitlines()[0].split(";")]
initial_states: list = [
    item for item in initial_and_final_states[0].split(" ")]

final_states: list = [item for item in initial_and_final_states[1].split(" ")]

transitions: list = [item for item in graph_model.splitlines()[1:]]
del transitions[-1]

word: list = [item for item in graph_model.splitlines()[-1].split(":")
              [1].strip()]

current_state = initial_states[0]


def available_transitions(symbol: str, transitions: list, current_state: str) -> list:
    aux = []
    for item in transitions:
        if item.split(" ")[1] and item.split(" ")[0] == current_state:
            aux.append(item)
    return aux


def is_able_to_consume():
    transitions_symbols = [item.split(" ")[1] for item in transitions]
    for w in word:
        if w not in transitions_symbols:
            return False
    return True


def run_FA():
    if is_able_to_consume():
        id_k = 0
        decision_tree = []
        height = 0

        # Lendo o primeiro estado do automato
        decision_tree.append(Node(id_k, current_state, height, None))
        while word:
            current_symbol = word.pop(0)
            aux = []
            for dt_item in decision_tree:
                if dt_item.height == height:
                    children = [item.split(" ")[3] for item in available_transitions(
                        current_symbol, transitions, dt_item.value)]
                    for c in children:
                        id_k = id_k + 1
                        node = Node(id_k, c, height+1, dt_item.id)
                        aux.append(node)
            for a in aux:
                decision_tree.append(a)

            height = height + 1
        return decision_tree
    else:
        print('O automato não pode ser consumido')


decision_tree = run_FA()


def tree_height():
    tree_height = 0
    for item in decision_tree:
        if tree_height < item.height:
            tree_height = item.height
    return tree_height


def leafts_final_state():
    th = tree_height()
    aux = []
    for item in decision_tree:
        if item.height == th and item.value in final_states:
            aux.append(item)
    return aux


lfs = leafts_final_state()


def find_in_tree(id):
    for item in decision_tree:
        if item.id == id:
            return item

# Construir os caminhos


def build_path(node: Node):
    aux = []
    current_node = node
    aux.append(current_node)
    while current_node.parent_id != None:
        current_node = find_in_tree(current_node.parent_id)
        aux.append(current_node)
    return aux


def list_paths():
    paths = []
    for item in lfs:
        paths.append(build_path(item))
    return paths


paths = list_paths()


def states_to_consume_word(path):
    states = []
    transitions = []
    word: list = [item for item in graph_model.splitlines()[-1].split(":")
                  [1].strip()]
    for state in path:
        aux = State(state.value)
        states.append(aux)
    while states:
        try:
            aux = Transition(states[-1], states[-2], word.pop(0))
            states.pop()
            transitions.append(aux)
        except:
            break
    return transitions


def possible_transitions():
    aux = []
    for item in paths:
        aux.append(states_to_consume_word(item))
    return aux


possibilities = possible_transitions()


def build_animation(possibility: list, prefix_number: str):
    graph = pydot.Dot('my_graph', graph_type='digraph')
    for transition in transitions:
        graph.add_node(pydot.Node(str(transition.split(
            " ")[0]), shape='circle', label=str(transition.split(" ")[0])))
        graph.add_node(pydot.Node(str(transition.split(
            " ")[3]), shape='circle', label=str(transition.split(" ")[3])))
        graph.add_edge(pydot.Edge(transition.split(" ")[0], transition.split(" ")[
                       3], label=transition.split(" ")[1]))

    for initial in initial_states:
        graph.add_node(pydot.Node(str(initial), shape='circle'))
    for final in final_states:
        graph.add_node(pydot.Node(str(final), shape='doublecircle'))

    image_index = 0
    graph.write_png(f'app/assets/graph_imgs/output_{image_index}.jpg')

    i = 0
    for index, t in enumerate(possibility):
        if index == 0:
            graph.add_node(pydot.Node(
                possibility[index].origin.name, color='blue', style='circle'))
            image_index = image_index + 1
            graph.write_png(f'app/assets/graph_imgs/output_{image_index}.jpg')
            graph.del_edge(possibility[index].origin.name,
                           possibility[index].destiny.name)

            graph.add_node(pydot.Node(
                possibility[index].origin.name, color='black', style='circle'))
            graph.add_edge(pydot.Edge(str(possibility[index].origin.name),
                                      str(possibility[index].destiny.name), label=str(t.symbol), color='blue'))
            image_index = image_index + 1
            graph.write_png(
                f'app/assets/graph_imgs/output_{image_index}.jpg')

            index = index + 1
        else:
            graph.add_node(pydot.Node(
                possibility[index-1].origin.name, color='black', style='circle'))

            graph.add_node(pydot.Node(
                possibility[index].origin.name, color='blue', style='circle'))
            image_index = image_index + 1
            graph.write_png(f'app/assets/graph_imgs/output_{image_index}.jpg')

            graph.del_edge(
                str(possibility[index].origin.name), str(possibility[index].destiny.name))

            graph.add_edge(pydot.Edge(str(possibility[index].origin.name),
                                      str(possibility[index].destiny.name), label=str(t.symbol), color='blue'))
            image_index = image_index + 1
            graph.write_png(
                f'app/assets/graph_imgs/output_{image_index}.jpg')
            index = index + 1

    graph.add_node(pydot.Node(
        possibility[-1].origin.name, color='black', style='circle'))

    graph.add_node(pydot.Node(
        possibility[-1].destiny.name, color='blue', style='circle'))
    image_index = image_index + 1
    graph.write_png(f'app/assets/graph_imgs/output_{image_index}.jpg')

    image_index = image_index + 1
    graph.write_png(
        f'app/assets/graph_imgs/output_{image_index}.jpg')


build_animation(possibilities[0], "1")
