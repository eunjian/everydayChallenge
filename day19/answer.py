import heapq

# '무한'을 의미하는 값으로 10억을 활용
INF = int(1e9)

# 노드와 간선의 개수, 시작 노드 번호, 도착 노드 번호 입력받기
n, e, start, end = map(int, input().split())

# 노드별로 연결된 노드 정보를 저장할 리스트 선언
graph = [[] for _ in range(n + 1)]

# 최단 거리 테이블: 초기에는 모든 값을 무한으로 초기화
distance = [INF] * (n + 1)

# 최단 경로를 기록하기 위한 배열
path = [-1] * (n + 1)

# 공사 중인 도시를 저장할 리스트
construction = [False] * (n + 1)

# 간선 정보 입력받기 (비용을 무시)
for _ in range(e):
	n_a, n_b = map(int, input().split())
	graph[n_a].append(n_b)
	graph[n_b].append(n_a)  # 양방향 간선 처리

# 최단 경로 계산 함수
def dijkstra(start):
	# 우선순위 큐 자료구조 생성
	pq = []
	# 시작 노드의 자기 자신까지의 거리는 0으로 설정, 우선순위 큐에 삽입
	heapq.heappush(pq, (0, start))
	distance[start] = 0
	# 우선순위 큐가 비어있을 때까지 무한 반복
	while pq:
		# 최단 거리가 가장 짧은 노드 추출(거리, 노드 정보 순)
		dist, n_now = heapq.heappop(pq)
		# 이미 처리된 노드는 무시
		if distance[n_now] < dist:
			continue
		# 현재 처리 중인 노드와 인접한 노드 확인
		for n_next in graph[n_now]:
			# 사용 불가능한 노드라면 다른 경로로 계산
			if construction[n_next]:
				continue
			c = dist + 1  # 비용을 무시하고 거리를 1로 고정
			# 현재 노드를 거쳐 다른 노드로 가는 거리가 더 짧은 경우
			if c < distance[n_next]:
				# 최단 거리 테이블 갱신
				distance[n_next] = c
				path[n_next] = n_now  # 최단 경로를 기록
				# 우선순위 큐에 (거리, 노드 정보) 삽입
				heapq.heappush(pq, (c, n_next))

# 최소 이동 경로 역추적
def get_shortest_path(end):
	path_nodes = []
	node = end
	while node != -1:
		path_nodes.append(node)
		node = path[node]
	path_nodes.reverse()
	return path_nodes

# 각 날짜에 대한 최단 경로 계산 및 출력
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