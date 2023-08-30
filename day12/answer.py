from collections import deque

# 마을 크기
n = int(input())
# 마을 상태
houses = [list(map(int, input().split())) for _ in range(n)]

# 발전기 개수
count = 0

# 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# def dfs(x, y):
# 	houses[x][y] = 2  # 방문한 집은 2로 표시
# 	for i in range(4):
# 		nx, ny = x + dx[i], y + dy[i]
# 		if 0 <= nx < n and 0 <= ny < n and houses[nx][ny] == 1:
# 			dfs(nx, ny)
def bfs(x, y):
	queue = deque([(x, y)])
	houses[x][y] = 2  # 방문한 집은 2로 표시
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			if 0 <= nx < n and 0 <= ny < n and houses[nx][ny] == 1:
				queue.append((nx, ny))
				houses[nx][ny] = 2

# 발전기를 설치 및 방문 가능한 집 모두 방문
for i in range(n):
	for j in range(n):
		if houses[i][j] == 1:
			count += 1
			bfs(i, j)

print(count)