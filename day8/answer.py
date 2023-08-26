# 플레이어의 통증 수치 입력
n = int(input())
# 사용한 아이템의 개수
count = 0

# 통증 수치 감소 아이템 3종류 (큰 순서대로 배열)
items = [14, 7, 1]

# 통증 수치 감소 아이템 개수 최소로 사용
for item in items:
	count += n//item #사용된 해당 아이템 개수 세기
	n %= item 

# 필요한 아이템 최소 개수 출력
print(count)