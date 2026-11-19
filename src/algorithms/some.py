from algorithms.many import many, createGraph

def some(f):
    graph = createGraph(f)

    m = many(f, graph=graph)

    if m > 0: # if many found one or more red nodes
        return True

    if m == -1: # if many found no st path
        return False

    if graph.start in graph.red or graph.sink in graph.red: # if start or sink itself is red
        return True


    # if there is a path from start to sink, and all edges going out from start point to a red vertex
    allStartNeighboursAreRed = True
    for e in graph.E:
        if e.src == graph.start and e.weight == 0: # if e is an edge to a black neighbour of start
            allStartNeighboursAreRed = False
            break
    if allStartNeighboursAreRed:
        return True

    # if there is a path from start to sink, and all edges going to sink come from a red vertex
    allSinkNeighboursAreRed = True
    for e in graph.E:
        if e.dst == graph.sink and not e.src in graph.red: # if e is an edge from a black vertex to sink
            allSinkNeighboursAreRed = False
            break
    if allSinkNeighboursAreRed:
        return True

    return False