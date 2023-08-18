##sort()사용
N = int(input())
arr = list(map(int, input().split()))

MAX = max(arr)
maxIndex = arr.index(MAX)

left = arr[:maxIndex]
right = arr[maxIndex:]

left.sort()
right.sort(reverse=True)

sortedArr = left + right

check = True

for i in range(N):
	if arr[i] != sortedArr[i]:
		check = False
		break

if check:
	print(sum(arr))
else:
	print(0)
    
##sorted()사용
N = int(input())
arr = list(map(int, input().split()))

MAX = max(arr)
maxIndex = arr.index(MAX)

left = arr[:maxIndex]
right = arr[maxIndex:]

sortedLeft = sorted(left)
sortedRight = sorted(right, reverse=True)

sortedArr = sortedLeft + sortedRight

check = True

for i in range(N):
	if arr[i] != sortedArr[i]:
		check = False
		break

if check:
	print(sum(arr))
else:
	print(0)