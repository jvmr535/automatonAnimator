import glob

import pydot
from PIL import Image

from Node import Node
from Transition import Transition

graph = open("app/assets/graphs/graph_notation.txt", "r").read()


initial_and_final_states: list = [item.strip()
                                  for item in graph.splitlines()[0].split(";")]
initial_states: list = [Node(item)
                        for item in initial_and_final_states[0].split(" ")]
final_states: list = [Node(item)
                      for item in initial_and_final_states[1].split(" ")]
transitions: list = [item for item in graph.splitlines()[1:]]
del transitions[-1]

transitions = [Transition(
    item.split(" ")[0],
    item.split(" ")[3],
    item.split(" ")[1])
    for item in transitions]


word: list = [item for item in graph.splitlines()[-1].split(":")[1].strip()]

# Which of the initial states will be the first according to the word


def first_state(initial_states: list, transitions: list):
    for initial in initial_states:
        for transition in transitions:
            if initial.name == transition.origin and word[0] == transition.symbol:
                return transition


def next_state(current_state: Node, transitions: list):
    for transition in transitions:
        if current_state == transition.origin and word[0] == transition.symbol
        word.pop()
        return

# def next_state(current_state: str, transitions: list):
#     for transition in transitions:
#         if current_state == transition.split(" ")[0] and word[0] == transition.split(" ")[1]:
#             word.pop(0)
#             return transition
#     print('Automato não conseguiu ler a palavra')
#     return exit(1)

# current_state = who_is_initial_state(initial_states, transitions)
# states_to_consume_the_word: list = []

# while True:
#     if len(word) != 0:
#         current_state = next_state(current_state, transitions)
#         states_to_consume_the_word.append(current_state)
#     elif len(word) == 0 and current_state in final_states:
#         break

# word: list = [item for item in graph.splitlines()[-1].split(":")
#               [1].strip()]

# def build_animation():
#     graph = pydot.Dot('my_graph', graph_type='digraph')

#     graph.add_node(pydot.Node(f'Passo', shape='square',
#                               label=f'Passo - \n Le: -'))
#     graph.write_dot('output_graphviz.dot')

#     for transition in transitions:
#         graph.add_node(pydot.Node(str(transition.split(
#             " ")[0]), style='bold', shape='circle', label=str(transition.split(" ")[0])))
#         graph.add_node(pydot.Node(str(transition.split(
#             " ")[3]), style='bold', shape='circle', label=str(transition.split(" ")[3])))
#         graph.add_edge(pydot.Edge(transition.split(" ")[0], transition.split(" ")[
#                        3], label=transition.split(" ")[1]))

#     for initial in initial_states:
#         graph.add_node(pydot.Node(str(initial)))
#     for final in final_states:
#         graph.add_node(pydot.Node(str(final), shape='doublecircle'))

#     graph.write_png('app/assets/graph_imgs/output.jpg')

#     for i in range(len(states_to_consume_the_word)):
#         if i == 0:
#             graph.add_node(pydot.Node(
#                 str(states_to_consume_the_word[i]), style='filled', color="lightblue"))

#             graph.add_node(pydot.Node(f'Passo', shape='square',
#                                       label=f'Passo {i+1} \n Le: {word[i]}'))

#             graph.write_png(f'app/assets/graph_imgs/output{i}.jpg')
#             graph.write_dot(f'app/assets/graph_imgs/output_graphviz{i}.dot')
#         else:
#             graph.add_node(pydot.Node(
#                 str(states_to_consume_the_word[i-1]), style="bold", color="black"))
#             graph.add_node(pydot.Node(
#                 str(states_to_consume_the_word[i]), style='filled', color="lightblue"))

#             graph.add_node(pydot.Node(f'Passo', shape='square',
#                                       label=f'Passo {i+1} \n Le: {word[i]}'))

#             graph.write_png(f'app/assets/graph_imgs/output{i}.jpg')
#             graph.write_dot(f'app/assets/graph_imgs/output_graphviz{i}.dot')

#     frames = []

#     imgs = glob.glob("app/assets/graph_imgs/*.jpg")
#     for i in imgs:
#         new_frame = Image.open(i)
#         frames.append(new_frame)

#     frames[0].save('app/assets/graph_imgs/automaton.gif', format='GIF',
#                    append_images=frames[1:],
#                    save_all=True,
#                    duration=1500, loop=0)

# build_animation()
