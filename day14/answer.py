from collections import deque

# Input: Number of nodes, number of edges, starting node
n, m, k = map(int, input().split())

# Initialize the graph with edges between nodes
graph = [[] for _ in range(n+1)]
for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# Sort neighbors of each node in ascending order
for i in range(1, n+1):
    graph[i].sort()

# Initialize visited node list and mark the starting node as visited
visited = [False] * (n+1)
visited[k] = True

# Initialize the path list with the starting node
path = [k]

# Initialize a queue with the starting node
q = deque([k])

# BFS traversal
while q:  # Continue until there are no more reachable nodes
    node = q.popleft()  # Get the smallest node available
    for next_node in graph[node]:  # Iterate through its neighbors
        if not visited[next_node]:  # If the neighbor is not visited yet
            visited[next_node] = True  # Mark it as visited
            q.append(next_node)  # Add it to the queue for further exploration
            path.append(next_node)  # Record the path
            break  # Move to the smallest neighbor and exit the loop

# Output the number of visited nodes and the last visited node
print(len(path), path[-1])
