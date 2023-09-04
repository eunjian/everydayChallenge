from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(i, j):
	q = deque([(i, j)])
	M = arr[i][j]
	cnt = 0
	
	while q:
		y, x = q.popleft()
		
		if arr[y][x] != M:
			continue
		
		arr[y][x] = 0
		cnt += 1
		
		for k in range(4):
			ny, nx = y + dy[k], x + dx[k]
			
			if ny in (-1, N) or nx in (-1, N) or arr[ny][nx] != M:
				continue
			
			q.append((ny, nx))
	
	return cnt

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
count = [0] * 31

for i in range(N):
	for j in range(N):
		if arr[i][j]:
			M = arr[i][j]

			if bfs(i, j) >= K:
				count[M] += 1

result, temp = 0, 0

for i in range(31):
	if temp <= count[i]:
		result = i
		temp = count[i]

print(result)