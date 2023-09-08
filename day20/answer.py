from collections import deque

# Input
n, k, q = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

# Directions for moving up, down, left, and right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# List to keep track of visited cells
visited = [[False] * n for _ in range(n)]

def bfs(x, y):
    # Add the starting coordinates to the queue and mark them as visited
    queue = deque([(x, y)])
    visited[x][y] = True
    size = 1  # Store the size of the connected component
    components = [(x, y)]  # Store coordinates belonging to the connected component

    while queue:
        cur_x, cur_y = queue.popleft()

        # Move in all four directions from the current position
        for i in range(4):
            new_x = cur_x + dx[i]
            new_y = cur_y + dy[i]

            # Ignore if out of bounds
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n:
                continue

            # Ignore if already visited or if the cell contains '.'
            elif visited[new_x][new_y] or graph[new_x][new_y] == '.':
                continue

            # If an adjacent cell has the same letter, add it to the queue and mark it as visited
            elif graph[new_x][new_y] == graph[x][y]:
                queue.append((new_x, new_y))
                visited[new_x][new_y] = True
                size += 1
                components.append((new_x, new_y))

    return size, components

# Perform the operations
for _ in range(q):
    x, y, d = input().split()
    x, y = int(x), int(y)
    graph[x-1][y-1] = d

    # Find connected components
    visited = [[False] * n for _ in range(n)]
    component_size, component_coords = bfs(x-1, y-1)

    # If the component size is greater than or equal to K, remove the letters from the component
    if component_size >= k:
        for cx, cy in component_coords:
            graph[cx][cy] = '.'

# Output the updated array
for row in graph:
    print(''.join(row))
