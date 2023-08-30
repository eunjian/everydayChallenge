from collections import deque

# bfs를 이용해 상하좌우 탐색하여 동일 유형 건물 개수 구하기
def bfs(x, y, building_type, village, n):
	q = deque([(x, y)])
	village[x][y] = 0 # 방문한 칸 0 표시
	count = 1 # 건물 개수
	directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 방향 벡터
	while q:
		x, y = q.popleft()
		for dx, dy in directions:
			nx, ny = x + dx, y + dy
			# 좌표의 범위, 방문칸, 동일한 유형의 건물인지 확인
			if 0 <= nx < n and 0 <= ny < n and village[nx][ny] != 0 and village[nx][ny] == building_type:
				q.append((nx, ny))
				village[nx][ny] = 0
				count += 1
	return count

# 가장 많은 단지가 있는 건물 유형 찾기
def find_most_building_type(village, n, k):
	building_counts = {}  # 각 건물 유형의 단지 수를 저장
	for building_type in range(1, 31):
		count = 0 # 단지 수
		for i in range(n):
			for j in range(n):
				if village[i][j] == building_type:
					building_count = bfs(i, j, building_type, village, n)
					# k개 이상의 동일 유형의 건물이 있을 때 단지로 카운드
					if building_count >= k: 
						count += 1
		# 이미 해당 단지 수에 대한 건물 유형 있으면 더 높은 숫자의 건물 선택
		if building_counts.get(count) is None or building_type > building_counts[count]:
			building_counts[count] = building_type
	max_building_type = building_counts[max(building_counts.keys())]
	return max_building_type

# 마을의 크기와 단지의 기준 입력
n, k = map(int, input().split())
# 마을 상태 입력
village = [list(map(int, input().split())) for _ in range(n)]

# 가장 많은 단지 수를 가진 건물 유형 찾기
result = find_most_building_type(village, n, k)
print(result)