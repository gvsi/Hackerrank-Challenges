inputArr = ["5 6",
        "1 2 3",
        "1 3 4",
        "4 2 6",
        "5 2 2",
        "2 3 5",
        "3 5 7",
        "1"
        ]
def input():
    return inputArr.pop(0)

n, m = input().split()
n, m = int(n), int(m)

graph = dict()

for i in range(m+1):
    graph[i+1] = set()

for i in range(m):
    st, end, val = list(map(int, input().split()))
    graph[st].add((end, val))
    graph[end].add((st, val))

start = int(input())

print(graph)

visited = set()
visited.add(start)

length = 0;
while len(visited) < n:
    potential_edges = set()
    for node in visited:
        for edge in graph[node]:
             if edge[0] not in visited:
                potential_edges.add((node, edge[1], edge[0]))
    # print("potential:", potential_edges)
    min_edge = min(potential_edges, key=lambda x:x[1])
    visited.add(min_edge[2])
    length += min_edge[1]

print(length)
