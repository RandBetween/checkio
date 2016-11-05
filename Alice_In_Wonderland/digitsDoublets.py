def create_graph(numbers):
    graph = {}
    for node in numbers:
        if node not in graph:
            keys = []
            for key in numbers:
                temp_set = filter(lambda x: str(node)[x] != str(key)[x], [0,1,2])
                if len(temp_set) == 1:
                    keys.append(key)
            graph[node] = keys
    return graph

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def checkio(numbers):
    return find_shortest_path(create_graph(numbers), numbers[0], numbers[-1])
