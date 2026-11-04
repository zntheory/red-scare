
def few_input_values():
    number_of_vertices, number_of_edges, number_of_red = map(int, input().split())
    start, sink = map(int, input().split())

    name_to_vertex_index = dict()
    red_vertex_set = set()
    for i in number_of_vertices:
        inp = input().split()
        if len(inp) == 2:
            red_vertex_set.add(inp[0])
        name_to_vertex_index[inp[0]] = i

    
    

    return (number_of_vertices, number_of_edges, number_of_red, start, sink)

def dijkstra():


def few():
