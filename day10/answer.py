import numpy as np
# 게임판의 크기 입력
n = int(input())
# 구름이와 플레이어가 말을 올려둔 칸의 좌표
r_g, c_g = map(int, input().split())
r_p, c_p = map(int, input().split())
# 보드의 각칸에 적혀있는 지시 사항
arr = [list(input().split()) for _ in range(n)]
org = [[r_g,c_g],[r_p,c_p]]
result = []

for xy in org:
	repeat = True
	# 구름이와 플레이어의 이동 확인을 위한 게임판 생성
	b = [[0] * n for _ in range(n)]
	x = xy[0]-1
	y = xy[1]-1
	b[x][y] = 1
	while repeat:
		c = int(arr[x][y][:-1]) #이동할 칸의 수
		if 'U' in arr[x][y]: #위쪽이동
			for i in range(c):
				x -= 1
				if x < 0:
					x = n-1
				if b[x][y] != 0:
					repeat = False
					break
				b[x][y] = 1
		elif 'D' in arr[x][y]: #아래쪽 이동
			for i in range(c):
				x += 1
				if x >= n:
					x = 0
				if b[x][y] != 0:
					repeat = False
					break
				b[x][y] = 1
		elif 'L' in arr[x][y]: #왼쪽 이동
			for i in range(c):
				y -= 1
				if y < 0:
					y = n-1
				if b[x][y] != 0:
					repeat = False
					break
				b[x][y] = 1
		else: # 오른쪽 이동
			for i in range(c):
				y += 1
				if y >= n:
					y = 0
				if b[x][y] != 0:
					repeat = False
					break
				b[x][y] = 1
	# result.append(b)
	result.append(np.array(b).flatten().tolist().count(1))
		
# 구름이와 플레이어의 이동 횟수 비교
if result[0] > result[1]:
	print('goorm', result[0])
else:
	print('player', result[1])