import numpy as np

# 게임판의 크기, 찾고 싶은 깃발의 값 입력
n, k = map(int, input().split())
# 게임판의 각 칸에 대한 정보 입력
m = [input() for _ in range(n)]

# 구름표시 게임판
matrix = []
for i in range(len(m)):
	matrix.append(m[i].split())
	
# 깃발의 값 나타내는 게임판 생성
result = []

for r in range(n):
	result.append([])
	for c in range(n):
		if matrix[r][c] == '1':
			# 구름 칸의 경우 깃발의 값 범위를 넘어서는 10으로 표시
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

# 2차원 리스트를 1차원으로 바꿈
result = np.array(result).flatten().tolist()
# 값이 k인 깃발의 개수 출력
print(result.count(k))