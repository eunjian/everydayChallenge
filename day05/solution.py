N, K = map(int, input().split())
arr = list(map(int, input().split()))

newArr = []

for i in range(N):
	binaryNumber = bin(arr[i])[2:]
	
	count = 0
	
	for c in binaryNumber:
		if c == '1':
			count += 1
	
	newArr.append( [count, arr[i]] )

newArr.sort(reverse=True)
print(newArr[K - 1][1])