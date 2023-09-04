from collections import deque
# BFS 탐색
def bfs(graph, start, visited):
	q = deque([start])
	visited[start] = True
	while q:
		v = q.popleft()
		for i in graph[v]:
			if not visited[i] and v in graph[i]:
				q.append(i)
				visited[i] = True
				
# 섬의 개수와 다리의 개수 입력
n, m = map(int, input().split())
# 다리 정보 입력하여 그래프 생성
graph = [[] for _ in range(n+1)]
for i in range(m):
	n1, n2 = map(int, input().split())
	graph[n1].append(n2)
# 방문 노드 체크를 위한 리스트
visited = [False] * (n+1)

# 연합 개수 세기
count = 0
for i in range(1, n+1):
	if not visited[i]:
		bfs(graph, i, visited)
		count += 1
		
# 연합 개수 출력
print(count)