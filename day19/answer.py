import heapq

# Use a large value to represent 'infinity'
INF = int(1e9)

# Input the number of nodes, edges, start node, and end node
n, e, start, end = map(int, input().split())

# Initialize a list to store connected nodes for each node
graph = [[] for _ in range(n + 1)]

# Initialize the distance table with all values set to 'infinity'
distance = [INF] * (n + 1)

# Initialize an array to record the shortest path
path = [-1] * (n + 1)

# List to keep track of construction in each city
construction = [False] * (n + 1)

# Input edge information (ignoring the cost)
for _ in range(e):
    n_a, n_b = map(int, input().split())
    graph[n_a].append(n_b)
    graph[n_b].append(n_a)  # Handle bidirectional edges

# Dijkstra's algorithm to calculate the shortest path
def dijkstra(start):
    # Priority queue data structure
    pq = []
    # Set the distance from the start node to itself to 0 and push it to the priority queue
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    # Continue until the priority queue is empty
    while pq:
        # Pop the node with the shortest distance (distance, node info)
        dist, n_now = heapq.heappop(pq)
        # Ignore nodes that have already been processed
        if distance[n_now] < dist:
            continue
        # Check adjacent nodes to the current node
        for n_next in graph[n_now]:
            # Skip nodes that are unavailable
            if construction[n_next]:
                continue
            c = dist + 1  # Ignore the cost and set the distance to 1
            # Update the shortest distance table if a shorter path is found
            if c < distance[n_next]:
                distance[n_next] = c
                path[n_next] = n_now  # Record the shortest path
                # Push (distance, node info) to the priority queue
                heapq.heappush(pq, (c, n_next))

# Reverse lookup of the shortest path
def get_shortest_path(end):
    path_nodes = []
    node = end
    while node != -1:
        path_nodes.append(node)
        node = path[node]
    path_nodes.reverse()
    return path_nodes

# Calculate and print the shortest path for each day
for day in range(1, n + 1):
    blocked_node = day
    construction[blocked_node] = True
    distance = [INF] * (n + 1)
    path = [-1] * (n + 1)
    dijkstra(start)
    if blocked_node in [start, end] or distance[end] == INF:
        print("-1")
    else:
        path_nodes = get_shortest_path(end)
        print(len(path_nodes))
    construction[blocked_node] = False
