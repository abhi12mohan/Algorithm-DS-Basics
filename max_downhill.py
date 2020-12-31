def most_awesome(C, R):
    '''
    Input: C | list of checkpoint pairs (c, h) with name c and height h
           R | list of route triples (c1, c2, a) for route {c1, c2}, awesome a
    Output:  | list representing a course having maximum awesomeness
    '''
    def dfs(Adj, s, parent = None, order = []):
        if parent is None:
            parent = {}
            for point in Adj:
                parent[point] = None
            parent[s] = s

        for v in Adj[s]:
            if parent[v] is None:
                parent[v] = s
                dfs(Adj, v, parent, order)

        order.append(s)

    def full_dfs(Adj):
        parent = {}
        for point in Adj:
            parent[point] = None

        order = []
        for v in Adj:
            if parent[v] is None:
                parent[v] = v
                dfs(Adj, v, parent, order)

        return order

    def relax(Adj, d, parent, u, v):
        if d[v] > d[u] + Adj[u][v]:
            d[v] = d[u] + Adj[u][v]
            parent[v] = u

    def DAG_Shortest_Paths(Adj, w, s):
        topological_sort = []
        dfs(Adj, w, None, topological_sort)
        topological_sort.reverse()
        s.update(topological_sort)

        d = {}
        for point in topological_sort:
            d[point] = float('inf')

        parent = {point:None for point in topological_sort}
        d[w], parent[w] = 0, w

        for u in topological_sort:
            for v in Adj[u]:
                relax(Adj, d, parent, u, v)

        minimum = min(d.values())
        for v in d:
            if d[v] == minimum and v != s:
                return d[v], v, parent

    checkpoints = {points[0]:points[1] for points in C}
    adjacency = {point:{} for point in checkpoints}

    for route in R:
        c1, c2, a = route

        if checkpoints[c1] > checkpoints[c2]:
            adjacency[c1][c2] = -a
        else:
            adjacency[c2][c1] = -a

    topological_sort = full_dfs(adjacency)
    topological_sort.reverse()

    visited = set()
    awesome_list = {}

    for point in topological_sort:
        if point not in visited:
            visited.add(point)
            if len(adjacency[point]) > 0:
                distance, value, parent  = DAG_Shortest_Paths(adjacency, point, visited)
                awesome_list[-distance] = (value, parent)

    node, parent = awesome_list[max(awesome_list)]

    list_result = [node]
    while parent[node] != node:
        node = parent[node]
        list_result.append(node)

    list_result.reverse()
    return list_result

# if __name__ == "__main__":
#     C = [('alpine_ridge', 7), ('rocky_canteen', 5), ('sunrise_ridge', 10), ('east_bluff', 10)]
#     R = [('rocky_canteen', 'alpine_ridge', 21), ('sunrise_ridge', 'rocky_canteen', 43), ('east_bluff', 'rocky_canteen', 18), ('east_bluff', 'alpine_ridge', 44), ('sunrise_ridge', 'alpine_ridge', 23)]
#
#     print(most_awesome(C, R))
