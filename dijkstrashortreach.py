input_arr = [
        "1",
        "4 4",
        "1 2 24",
        "1 4 20",
        "3 1 3",
        "4 3 12",
        "1"]
def input():
    return input_arr.pop(0)

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    graph = dict()
    for j in range(m):
        graph[j+1] = []
    for j in range(m):
        x, y, r = map(int, input().split())
        graph[x].append((y, r))
        graph[y].append((x, r))
    print(graph)
    start = int(input())

    distances = dict()
    inf = float("inf")
    for j in range(n):
        distances[j+1] = inf
    distances[start] = 0

    print(distances)

    unvisited = [x for x in range(1,n+1)]
    unvisited.remove(start)
    print(unvisited)

    current = start

    while len(unvisited) > 0:
        print("current:", current)
        unv_neighbors = [node for node in graph[current] if node[0] in unvisited]
        for neighbor in unv_neighbors:
            if distances[current] + neighbor[1] < distances[neighbor[0]]:
                distances[neighbor[0]] = distances[current] + neighbor[1]
        print("distances:")
        print(distances)
        current = min({node: distances[node] for node in unvisited}, key=distances.get)
        print("min:", current)
        unvisited.remove(current)

    for d in distances:
        if d != start:
            print(distances[d], end="")
