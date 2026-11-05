"""
None: Return the length of a shortest s,t-path internally avoiding R.
    To be precise, let P be the set of s,t-paths v_1,..., v_l such that v_i R if 1<i<l.
    Let l(p) denote the length of a path p.
    Return min,l(p): p in P.
    If no such path exists, return `-1'.
    Note that the edge st, if it exists, is an s,t-path with l=2.
    Thus, if s,t in E(G) then the answer is 1, no matter the colour of s or t.
    In G_ex, the answer is 3 (because of the path 0, 1, 2, 3.)
"""


from collections import defaultdict, deque

st = dict() # keys: src, trm
V = set()
E = dict()  # dict[list], vertex u maps to many vertices v
            # if undirected, vertex v maps to vertices edges u

# Credits for base: https://www.geeksforgeeks.org/dsa/breadth-first-search-or-bfs-for-a-graph/
def bfs():
    visited = defaultdict(lambda: False)

    src = st["src"]
    trm = st["trm"]

    q = deque()
    visited[src] = True
    q.append(src)
    breadth = 1

    while q:
        u = q.popleft()
        breadth += 1

        if trm in E[u]:
            return breadth

        for v in E[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

    return -1


# TODO: Optimisation idea
# Get s, t then f.readlines() NO SPLIT
# This returns a list of the vertices and edges
# Search for s

def parse(f):
    n, m, r = [int(x) for x in f.readline().split()]
    if n > 0 and m == 0:
        return False

    s, t = f.readline().split()

    for _ in range(n):
        v = f.readline().split()
        if len(v) == 2:
            if v[0] == s or v[0] == t:
                return False
            continue
        else:
            V.add(v[0])
            if v[0] == s: st["src"] = v[0]
            if v[0] == t: st["trm"] = v[0]

    for _ in range(m):
        u, x, v = f.readline().split()

        if u not in E: E[u] = []
        E[u].append(v)

        if ">" != x:  # handle undirected
            if v not in E: E[v] = []
            E[v].append(u)

    return True

def none(f):
    # Removes R from graph
    if not parse(f):
        return -1

    return bfs()