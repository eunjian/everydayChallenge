N = int(input())
A, B = map(int, input().split())

dp = [float('inf')] * (N + 1)
dp[0] = 0

for i in range(N + 1):
	if i - A >= 0:
		dp[i] = min(dp[i], dp[i - A] + 1)
	if i - B >= 0:
		dp[i] = min(dp[i], dp[i - B] + 1)

print(dp[N] if dp[N] != float('inf') else -1)

# 내 코드랑 다른점/ 배울점
# 나는 for문을 2번 사용해서 반복했는데 정해 코드에선 if문을 두번 써서 아이템 A와 B를 각각 비교함