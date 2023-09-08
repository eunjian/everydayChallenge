from collections import deque

# Input the number of computers and the number of communication lines
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# Input information about communication lines and create the graph
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
result = []  # Store the component with the maximum density for output
max_density = 0  # Maximum density value

# BFS traversal
def bfs(i):
    q = deque([i])
    component = set()  # List to store the component to which the node belongs
    edge_count = 0  # Number of communication lines in the current component
    while q:
        now = q.popleft()
        if visited[now]:
            continue
        visited[now] = True
        component.add(now)
        for to in graph[now]:
            if not visited[to]:
                q.append(to)
                edge_count += 1
    return component, edge_count

for i in range(1, n + 1):
    if not visited[i]:
        component, edge_count = bfs(i)
        component = sorted(list(component))  # Convert to a list and sort
        density = edge_count / len(component)  # Calculate density
        # Compare current density with maximum density (Use absolute difference less than 1e-8 for floating-point values)
        if abs(density - max_density) < 1e-8:  # If the current density is equal to the maximum density
            if len(result) > len(component):  # If the current component has fewer computers
                result = component
                max_density = density
