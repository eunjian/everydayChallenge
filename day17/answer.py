from collections import deque

# 컴퓨터의 개수와 회선의 개수 입력
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
# 통신 회선 정보 입력 후 그래프 생성
for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)
visited = [False] * (n + 1)
result = [] # 출력할 최대 밀도값을 가진 컴포넌트
max_density = 0 # 최대 밀도값

# BFS 탐색
def bfs(i):
	q = deque([i])
	component = set() # 해당 노드가 속한 컴포넌트 저장할 리스트
	edge_count = 0 # 해당 컴포넌트의 통신 회선 개수
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

for i in range(1, n+1):
	if not visited[i]:
		component, edge_count = bfs(i)
		component = sorted(list(component)) # 리스트 형변환 후 정렬
		density = edge_count / len(component) # 밀도 계산
		# 현재 밀도와 밀도 최대값 비교 (실수값이므로 == 이용하지 않고 절대값의 차가 1e-8보다 적으면 같은 값이라 여김)
		if abs(density - max_density) < 1e-8 : # 현재 밀도가 최대 밀도값과 같은 경우
			if len(result) > len(component): # 현재 컴포넌트 내 컴퓨터 개수가 더 적을 경우
				result = component
				max_density = density
			elif len(result) == len(component): # 두 컴포넌트의 컴퓨터 개수가 같은 경우
				if component[0] < result[0]: # 현재 컴포넌트가 더 작은 수의 컴퓨터를 가지고 있을 경우
					result = component
					max_density = density
		# 현재 밀도값이 최대 밀도 값보다 큰 경우
		elif density > max_density:
			result = component
			max_density = density


print(*result)