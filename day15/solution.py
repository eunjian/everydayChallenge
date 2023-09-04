N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x : x[1] // x[0])

result = 0

while K and arr:
	P, C = arr.pop()
	
	if K >= P:
		result += C
		K -= P
	else:
		result += C // P * K
		K = 0

print(result)