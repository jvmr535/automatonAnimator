file = open("graphs/graph_notation.txt", "r")
graph = file.read()
initial_states: list = [item.strip() for item in graph.splitlines()[0].split(";")]
word: list = [item for item in graph.splitlines()[-1].split(":")[1].strip()]
