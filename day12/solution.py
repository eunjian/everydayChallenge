from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0

def bfs(i, j):
	q = deque([(i, j)])
	
	while q:
		y, x = q.popleft()
		
		if not arr[y][x]:
			continue
		
		arr[y][x] = 0
		
		for k in range(4):
			ny, nx = y + dy[k], x + dx[k]
			
			if ny in (-1, N) or nx in (-1, N) or not arr[ny][nx]:
				continue
			
			q.append((ny, nx))
			
for i in range(N):
	for j in range(N):
		if arr[i][j]:
			result += 1
			bfs(i, j)

print(result)