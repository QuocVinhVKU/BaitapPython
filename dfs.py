import time
graph = {
    'A' : set(['B', 'C', 'D']),
    'B' : set(['E', 'A']),
    'C' : set(['E', 'F', 'A']),
    'D' : set(['F', 'A']),
    'E' : set(['B', 'C', 'Z']),
    'F' : set(['Z', 'C', 'D']),
    'Z' : set(['E', 'F'])
}

def dfs(graph, vertex, visited=None):
    time.sleep(1)
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex)
    for node in graph[vertex] :
        if node not in visited:
            print('Neighbour of {}: {}'.format(vertex , graph[vertex]))
            print('Visited: {}\n'.format(visited))
            dfs(graph, node, visited)

s = input('Bat dau tu: ')
dfs(graph, s)