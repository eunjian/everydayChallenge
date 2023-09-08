from collections import deque

# 입력 받기
n, k, q = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

# 상하좌우 이동을 위한 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 확인을 위한 리스트
visited = [[False] * n for _ in range(n)]

def bfs(x, y):
	# 시작 좌표를 큐에 추가하고 방문 처리
	queue = deque([(x, y)])
	visited[x][y] = True
	size = 1  # 연결 요소 크기 저장
	components = [(x, y)]  # 연결 요소에 속하는 좌표 저장
	while queue:
		cur_x, cur_y = queue.popleft()
		# 현재 위치에서 상하좌우 방향으로 이동
		for i in range(4):
			new_x = cur_x + dx[i]
			new_y = cur_y + dy[i]
			# 범위를 벗어나면 무시
			if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n:
				continue
			# 이미 방문한 곳이거나 '.'인 경우 무시
			elif visited[new_x][new_y] or graph[new_x][new_y] == '.':
				continue
			# 연결된 알파벳 대문자를 찾으면 큐에 추가하고 방문 처리
			elif graph[new_x][new_y] == graph[x][y]:
				queue.append((new_x, new_y))
				visited[new_x][new_y] = True
				size += 1
				components.append((new_x, new_y))
	return size, components

# 구름이의 작업을 수행
for _ in range(q):
	x, y, d = input().split()
	x, y = int(x), int(y)
	graph[x-1][y-1] = d
	# 연결 요소 찾기
	visited = [[False] * n for _ in range(n)]
	component_size, component_coords = bfs(x-1, y-1)
	# 크기가 K 이상인 연결 요소의 문자를 지우기
	if component_size >= k:
		for cx, cy in component_coords:
			graph[cx][cy] = '.'

# 배열 출력
for row in graph:
	print(''.join(row))
