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

        inp1 = (name_to_vertex_index[to],0)
        if name_to_vertex_index[to] in red_vertex_set:
            inp1 = (name_to_vertex_index[to],1)

        graph[name_to_vertex_index[fro]].append(inp1)
        if typ == "--":
            inp2 = (name_to_vertex_index[fro],0)
            if name_to_vertex_index[fro] in red_vertex_set:
                inp2 = (name_to_vertex_index[fro],1)
            graph[name_to_vertex_index[to]].append(inp2)

    

    return (number_of_vertices, number_of_edges, number_of_red, name_to_vertex_index[start], name_to_vertex_index[sink], red_vertex_set, graph)

def dijkstra(graph, source):
    #Define dist and prev
    dist = [math.inf for _ in range(len(graph))]
    prev = [None for _ in range(len(graph))]

    Q = []
    dist[source] = 0

    heapq.heappush(Q, (dist[source],source))
    
    ''' Choosing not to add everything into priority queue
    for i in range(len(graph)):
        heapq.heappush(Q, (dist[i],i))
    '''
    while Q:
        u = heapq.heappop(Q)

        for e in graph[u[1]]:
            v = e[0]
            distance = e[1]
            alt = dist[u[1]] + distance
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(Q,(dist[v],v))

    return dist, prev

def few(f):
    #Gets all the input values
    number_of_vertices, number_of_edges, number_of_red, start, sink, red_vertex_set, graph = few_input_values(f)

    dist, _ = dijkstra(graph, start)
    if dist[sink] == math.inf:
        return -1
    else: return dist[sink]