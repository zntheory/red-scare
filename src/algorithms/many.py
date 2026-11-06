class NegativeCycleException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class vertex:
    def __init__(self, id, isRed):
        self.id = id
        self.isRed = isRed

class edge:
    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight

    def toString(self):
        return f"{self.src} --({self.weight})--> {self.dst}"


def many(f):
    nameToInt : dict[str, int] = dict()
    red : set[int] = set()    
    
    edges: list[edge] = []


    n, m, r = map(int, f.readline().split())
    s, t = f.readline().split()

    nextNodeId = 0

    for v in range(n):
        tokens = f.readline().split()

        id = nextNodeId
        nextNodeId = nextNodeId+1
        name = tokens[0]
        nameToInt[name] = id

        isRed = len(tokens) == 2 and tokens[1] == '*'
        if isRed:
            red.add(id)

        # print(f"id: {id}, name: {name}, red: {isRed}")

    for e in range(m):
        tokens = f.readline().split()

        if tokens[1] == '--': # undirected graph
            v1 = nameToInt[tokens[0]]
            v2 = nameToInt[tokens[2]]

            weight_v1v2 = -1 if v2 in red else 0
            weight_v2v1 = -1 if v1 in red else 0

            edges.append(edge(v1, v2, weight_v1v2))
            edges.append(edge(v2, v1, weight_v2v1))

        elif tokens[1] == '->': # directed graph
            src = nameToInt[tokens[0]]
            dst = nameToInt[tokens[2]]
            weight = -1 if dst in red else 0

            edges.append(edge(src, dst, weight))

        else:
            print(f"Error: expected '--' or '->', but received '{tokens[1]}'")
            raise Exception("Wrong input")

    # print(f"edges:")
    # for e in edges:
    #     print(e.toString())

    srcId = nameToInt[s]
    dstId = nameToInt[t]

    dist = [1] * n
    dist[srcId] = -1 if srcId in red else 0 

    for v in range(n): # vertexes
        for e in edges: 
            # print(f"check {e.toString()}")
            if dist[e.src] != 1 and dist[e.src] + e.weight < dist[e.dst]:

                if v == n-1:
                    raise NegativeCycleException("Negative cycle detected")

                # print(f"relax {e.toString()} to {e.src} --({dist[e.src] + e.weight})--> {e.dst}")
                dist[e.dst] = dist[e.src] + e.weight

    # print(f"{str(-dist[dstId])}")
    # print(f"{dist}")

    return - dist[dstId]