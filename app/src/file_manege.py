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
