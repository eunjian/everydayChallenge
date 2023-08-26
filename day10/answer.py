import numpy as np

# Input the size of the game board
n = int(input())

# Input the coordinates where the Goorm and player placed their tokens
r_g, c_g = map(int, input().split())
r_p, c_p = map(int, input().split())

# Input the instructions written on each cell of the board
arr = [list(input().split()) for _ in range(n)]

# Create a matrix to track the movements of Goorm and the player
org = [[r_g, c_g], [r_p, c_p]]
result = []

# Iterate through the movements of both Goorm and the player
for xy in org:
    repeat = True

    # Create a game board to track the movements
    b = [[0] * n for _ in range(n)]
    x = xy[0] - 1
    y = xy[1] - 1
    b[x][y] = 1

    while repeat:
        c = int(arr[x][y][:-1])  # Number of cells to move
        if 'U' in arr[x][y]:  # Move upwards
            for i in range(c):
                x -= 1
                if x < 0:
                    x = n - 1
                if b[x][y] != 0:
                    repeat = False
                    break
                b[x][y] = 1
        elif 'D' in arr[x][y]:  # Move downwards
            for i in range(c):
                x += 1
                if x >= n:
                    x = 0
                if b[x][y] != 0:
                    repeat = False
                    break
                b[x][y] = 1
        elif 'L' in arr[x][y]:  # Move left
            for i in range(c):
                y -= 1
                if y < 0:
                    y = n - 1
                if b[x][y] != 0:
                    repeat = False
                    break
                b[x][y] = 1
        else:  # Move right
            for i in range(c):
                y += 1
                if y >= n:
                    y = 0
                if b[x][y] != 0:
                    repeat = False
                    break
                b[x][y] = 1

    # Count the number of cells visited by each player and store it in the result list
    result.append(np.array(b).flatten().tolist().count(1))

# Compare the number of cells visited by Goorm and player, then print the result
if result[0] > result[1]:
    print('goorm', result[0])
else:
    print('player', result[1])
