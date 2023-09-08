# Input the length of one side of a square and the number of lines to draw
n, m = map(int, input().split())

# Create a square-shaped board
board = [[[] for j in range(n)] for i in range(n)]

# Draw lines
for i in range(m):
    x, y, d = input().split()
    x, y = int(x) - 1, int(y) - 1  # Convert to integers and adjust for indexing
    if d == 'R':
        for j in range(y, n):
            board[x][j].append(1)
    elif d == 'L':
        for j in range(0, y + 1):
            board[x][j].append(2)
    elif d == 'U':
        for i in range(0, x + 1):
            board[i][y].append(3)
    elif d == 'D':
        for i in range(x, n):
            board[i][y].append(4)

# Calculate the number of intersection points
count = 0  # Number of intersection points
for i in range(n):
    for j in range(n):
        horizontal = 0  # Number of lines passing through this cell horizontally
        vertical = 0    # Number of lines passing through this cell vertically
        for direction in board[i][j]:
            if direction == 1 or direction == 2:
                horizontal += 1
            elif direction == 3 or direction == 4:
                vertical += 1
        count += horizontal * vertical

# Print the number of intersection points
print(count)
