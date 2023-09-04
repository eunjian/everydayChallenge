# 과일의 개수와 플레이어가 가진 돈 입력
n, k = map(int, input().split())
# 각 과일의 가격과 포만감 입력
l = []
for _ in range(n):
	p, c = map(int, input().split())
	l.append([p,c])

# 가격대비 포만감 높은 것부터 정렬, 가격대비 포만감 같을 땐 1개당 가격 높은 순
l.sort(key=lambda x: (x[1]/x[0], x[0]), reverse=True)

f = 0 # 포만감의 합
for p,c in l:
	if k >= p:
		k -= p
		f += c
	elif k > 0: # 돈은 남았지만 과일 1개를 전부 살 수는 없을 때 조각으로 구매
		f += (k/p)*c
		break
print(int(f))