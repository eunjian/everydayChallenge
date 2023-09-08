# 정사각형의 한 변의 길이와 그리려는 반직선의 개수 입력
n, m = map(int, input().split())
# 정사각형 모양의 칸 생성
board = [[[] for j in range(n)] for i in range(n)]
# 반직선 그리기
for i in range(m):
	x, y, d = input().split()
	x, y = int(x)-1, int(y)-1 # 정수형 변환 후 인덱스로 나타내기 위해 -1
	if d == 'R':
		for j in range(y,n):
			board[x][j].append(1)
	elif d == 'L':
		for j in range(0,y+1):
			board[x][j].append(2)
	elif d == 'U':
		for i in range(0,x+1):
			board[i][y].append(3)
	elif d == 'D':
		for i in range(x,n):
			board[i][y].append(4)
# print(board)
	
# 중첩점 계산
count = 0 # 중첩점 개수
for i in range(n):
	for j in range(n):
		horizontal = 0 # 해당칸 수평으로 지나는 반직선 개수
		vertical = 0 # 해당 칸 수직으로 지나는 반직선 개수
		for direction in board[i][j]:
			if direction == 1 or direction == 2:
				horizontal += 1
			elif direction == 3 or direction == 4:
				vertical += 1
		count += horizontal * vertical

# 중첩점 개수 출력
print(count)