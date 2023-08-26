# Input the size of the board and the number of bombs to drop
n, k = map(int, input().split())
# Input the state of the land
s = [input().split() for _ in range(n)]
# Input the coordinates of the land where bombs will be dropped
b = [input().split() for _ in range(k)]

# Lists for moving coordinates (north, east, south, west, current position)
dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]
# Preserve the original land state to check '@' lands
original = [arr[:] for arr in s]

# Drop bombs
for i in range(k):
    x = int(b[i][0]) - 1
    y = int(b[i][1]) - 1
    for j in range(5):
        # New coordinates after moving
        nx = x + dx[j]
        ny = y + dy[j]
        if nx < 0 or ny < 0 or nx >= n or ny >= n: # If the new coordinates are out of bounds
            continue
        elif s[nx][ny] == '#': # If the land state is #
            continue
        elif s[nx][ny] == '@': # If the land state is @
            s[nx][ny] = 2
        elif s[nx][ny] == '0': # If the land state is 0
            s[nx][ny] = 1
        else: # If the land already has a bomb
            if original[nx][ny] == '@':
                s[nx][ny] += 2
            else:
                s[nx][ny] += 1

# Convert the 2D list into a 1D list containing only integers for finding the maximum value
num_only = []
for rows in s:
    for i in rows:
        if i == '0':
            num_only.append(0)
        elif i == '#' or i == '@':
            continue
        elif str(i).isnumeric():
            num_only.append(i)

if len(num_only) == 0: # If all land values are #
    print(0)
else:
    print(max(num_only)) # Print the maximum value after bombs are dropped
