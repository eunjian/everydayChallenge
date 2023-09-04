from collections import deque
# BFS implementation
def bfs(graph, start, visited):
	q = deque([start])
	visited[start] = True
	while q:
		v = q.popleft()
		for i in graph[v]:
			if not visited[i] and v in graph[i]:
				q.append(i)
				visited[i] = True
				
# Input of the numbers of islands and bridges
n, m = map(int, input().split())
# Create a graph with the input of bridges
graph = [[] for _ in range(n+1)]
for i in range(m):
	n1, n2 = map(int, input().split())
	graph[n1].append(n2)
# A list for checking visited islands
visited = [False] * (n+1)

# Count the alliances
count = 0
for i in range(1, n+1):
	if not visited[i]:
		bfs(graph, i, visited)
		count += 1
		
# Print the number of alliances
print(count)
