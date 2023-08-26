import numpy as np

# Input the size of the game board and the flag value to find
n, k = map(int, input().split())
# Input the information for each cell of the game board
m = [input() for _ in range(n)]

# Create a matrix to represent the cloud-marked game board
matrix = []
for i in range(len(m)):
    matrix.append(m[i].split())

# Create a game board to represent the flag values
result = []

for r in range(n):
    result.append([])
    for c in range(n):
        if matrix[r][c] == '1':
            # For cloud-marked cells, use 10 to indicate a flag value which is beyond the range
            result[r].append(10)
            continue
        else:
            count = 0
            if c < len(matrix[r])-1 and matrix[r][c+1] == '1':
                count += 1
            if c != 0 and matrix[r][c-1] == '1':
                count += 1
            if r < len(matrix)-1 and c < len(matrix[r])-1 and matrix[r+1][c+1] == '1':
                count += 1
            if r < len(matrix)-1 and matrix[r+1][c] == '1':
                count += 1
            if c != 0 and r < len(matrix)-1 and matrix[r+1][c-1] == '1':
                count += 1
            if r != 0 and c < len(matrix[r])-1 and matrix[r-1][c+1] == '1':
                count += 1
            if r != 0 and matrix[r-1][c] == '1':
                count += 1
            if r != 0 and c != 0 and matrix[r-1][c-1] == '1':
                count += 1
            result[r].append(count)

# Flatten the 2D list into a 1D list
result = np.array(result).flatten().tolist()
# Print the count of flag values equal to k
print(result.count(k))
