from collections import deque

# Using BFS to explore the adjacent cells (up, down, left, right) and count buildings of the same type
def bfs(x, y, building_type, village, n):
	q = deque([(x, y)])
	village[x][y] = 0  # Mark the visited cell as 0
	count = 1  # Count of buildings
	directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Direction vectors
	while q:
		x, y = q.popleft()
		for dx, dy in directions:
			nx, ny = x + dx, y + dy
			# Check if coordinates are in range, unvisited, and have the same building type
			if 0 <= nx < n and 0 <= ny < n and village[nx][ny] != 0 and village[nx][ny] == building_type:
				q.append((nx, ny))
				village[nx][ny] = 0
				count += 1
	return count

# Finding the building type with the most neighborhoods
def find_most_building_type(village, n, k):
	building_counts = {}  # Store the count of neighborhoods for each building type
	for building_type in range(1, 31):
		count = 0  # Count of neighborhoods
		for i in range(n):
			for j in range(n):
				if village[i][j] == building_type:
					building_count = bfs(i, j, building_type, village, n)
					# Count it as a neighborhood if there are at least k buildings of the same type
					if building_count >= k:
						count += 1
		# If there's a building type already associated with the same count, choose the one with higher number
		if building_counts.get(count) is None or building_type > building_counts[count]:
			building_counts[count] = building_type
	max_building_type = building_counts[max(building_counts.keys())]
	return max_building_type

# Input the size of the village and the criterion for a neighborhood
n, k = map(int, input().split())
# Input the state of the village
village = [list(map(int, input().split())) for _ in range(n)]

# Finding the building type with the most neighborhoods
result = find_most_building_type(village, n, k)
print(result)
