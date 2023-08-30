# 플레이어의 통증 수치 입력
n = int(input())

# 아이템 A와 B가 줄일 수 있는 통증 수치 입력
a, b = map(int, input().split())

# 아이템의 통증 수치 리스트에 저장
items = [a, b]

# 최소 아이템 개수 저장하는 리스트 초기화
d = [1000001] * (n + 1)
d[0] = 0

# A와 B 각각 반복
for i in range(2):
    for j in range(items[i], n + 1):
        # 현재 통증 수치 j에 대해 최소 아이템 개수 계산
        d[j] = min(d[j], d[j - items[i]] + 1)

# 플레이어의 통증 수치를 0으로 만드는 데 필요한 최소 아이템 개수 출력
# 만약 통증 수치를 0으로 만들 수 없는 경우, -1 출력
if d[n] == 1000001:
    print(-1)
else:
    print(d[n])
