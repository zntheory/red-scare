import math
import heapq


def few_input_values(file):
    number_of_vertices, number_of_edges, number_of_red = map(int, file.readline().split())
    start, sink = file.readline().split()

    #Gets all vertexes, add the relevant to red set
    name_to_vertex_index = dict()
    red_vertex_set = set()
    for i in range(number_of_vertices):
        inp = file.readline().split()
        if len(inp) == 2:
            red_vertex_set.add(i)
        name_to_vertex_index[inp[0]] = i

    graph = [[] for _ in range(number_of_vertices)]


    #Creating the adjacency list graph
    for i in range(number_of_edges):
        fro, typ, to = file.readline().split()

        if not_same_type(red_vertex_set,name_to_vertex_index[fro],name_to_vertex_index[to]):
            graph[name_to_vertex_index[fro]].append(name_to_vertex_index[to])
            if typ == "--":
                graph[name_to_vertex_index[to]].append(name_to_vertex_index[fro])

    

    return (number_of_vertices, number_of_edges, number_of_red, name_to_vertex_index[start], name_to_vertex_index[sink], red_vertex_set, graph)

def not_same_type(red_vertex_set, fro, to):
    if fro in red_vertex_set:
        return to not in red_vertex_set
    elif fro not in red_vertex_set:
        return to in red_vertex_set



from collections import defaultdict, deque

 # dict[list], vertex u maps to many vertices v
            # if undirected, vertex v maps to vertices edges u

# Credits for base: https://www.geeksforgeeks.org/dsa/breadth-first-search-or-bfs-for-a-graph/
def bfs(graph, start, sink):


    visited = defaultdict(lambda: False)

    src = start
    trm = sink

    q = deque()
    visited[src] = True
    q.append(src)

    while q:
        u = q.popleft()

        if trm in graph[u]:
            return True

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

    return False

def alternate(f):
    #Gets all the input values
    number_of_vertices, number_of_edges, number_of_red, start, sink, red_vertex_set, graph = few_input_values(f)

    res = bfs(graph,start,sink)
    return res
    