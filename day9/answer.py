# 한 변의 길이, 폭탄을 떨어트릴 횟수 입력
n, k = map(int, input().split())
# 땅의 상태 입력
s = [input().split() for _ in range(n)]
# 폭탄을 떨어트릴 땅의 좌표들 입력
b = [input().split() for _ in range(k)]

# 좌표 이동을 위한 dx, dy 리스트 (현좌표 후 북동남서 순서)
dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]
# '@'땅을 확인하기 위해 원래 땅 보존
original = [arr[:] for arr in s]


# 폭탄 던지기
for i in range(k):
	# x번째 줄에서 y번째 문자는 인덱스로 표현했을 때는 [x-1][y-1]
	x = int(b[i][0]) - 1
	y = int(b[i][1]) - 1
	for j in range(5):
		#이동 좌표
		nx = x + dx[j]
		ny = y + dy[j]
		if nx < 0 or ny < 0 or nx >= n or ny >= n: # 이동한 좌표가 영역 밖인 경우
			continue
		elif s[nx][ny] == '#': # 땅의 상태가 #일때
			continue
		elif s[nx][ny] == '@': # 땅의 상태가 @일때
			s[nx][ny] = 2
		elif s[nx][ny] == '0': #땅의 상태가 0일때
			s[nx][ny] = 1
		else: #폭탄이 떨어진 땅일 때
			if original[nx][ny] == '@': #원래 땅의 상태가 @인 경우
				s[nx][ny] += 2
			else:
				s[nx][ny] += 1
			
# 최대값 추출을 위해 1차원 리스트로 변환 후 정수만 저장
num_only = []
for rows in s:
	for i in rows:
		if i == '0':
			num_only.append(0)
		elif i == '#' or i == '@':
			continue #num_only.append(0)로 하면 밑에서 if문 쓰지 않고 그냥 max값 출력가능할 듯
		elif str(i).isnumeric():
			num_only.append(i)

if len(num_only) == 0: # 모든 땅의 값이 #였을 경우
	print(0)
else:
	print(max(num_only))