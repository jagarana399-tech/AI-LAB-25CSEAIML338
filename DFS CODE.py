def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)
# Main program
graph = {}
n = int(input("Enter the number of vertices: "))
for i in range(n):
    vertex = input(f"Enter vertex {i+1}: ")
    neighbours = input(
        f"Enter adjacent vertices of {vertex} (space-separated): "
    ).split()
    graph[vertex] = neighbours
start = input("Enter the starting vertex: ")
print("\nGraph:", graph)
print("DFS Traversal:", end=" ")
visited = set()
dfs(graph, start, visited)
