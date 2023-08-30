from collections import deque

# Size of the village
n = int(input())
# Status of each house in the village
houses = [list(map(int, input().split())) for _ in range(n)]

# Count of generators to be installed
count = 0

# Direction vectors
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS function to traverse the village
def bfs(x, y):
    queue = deque([(x, y)])
    houses[x][y] = 2  # Mark visited houses as 2
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and houses[nx][ny] == 1:
                queue.append((nx, ny))
                houses[nx][ny] = 2

# Visit houses and install generators
for i in range(n):
    for j in range(n):
        if houses[i][j] == 1:
            count += 1
            bfs(i, j)

# Print the count of installed generators
print(count)
