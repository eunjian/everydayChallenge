from itertools import combinations

N = int(input())
S = input()

# 부분 문자열을 담을 P를 set()으로 선언합니다.
P = set()

# 공백의 번호를 담은 배열을 선언할게요.
blank = [i for i in range(1, N)]
# 공백 2개를 선택한 조합의 배열을 저장합니다.
comb = list(combinations(blank, 2))

# 현재 comb 배열의 각 원소는 위에서 언급한 (f, s) 꼴입니다. 변수의 개수를 맞추어 그대로 가져올게요.
for f, s in comb:
	# 부분 문자열로 쪼개어 P에 추가할게요.
	P.add(S[:f])
	P.add(S[f:s])
	P.add(S[s:])

# 구한 부분 문자열 집합을 list로 변환해줍니다.
P = list(P)

# 파이썬의 sort 함수는 문자열도 사전순으로 정렬이 가능합니다!
P.sort()

# 최대 점수를 저장할 변수를 선언할게요.
result = 0

# comb의 각 f, s에 대해 최대 점수를 완전탐색으로 찾아봅시다.
for f, s in comb:
	temp = 0

	# P에서 부분 문자열이 등장하는 위치를 찾습니다.
	# 이 때, 인덱스 + 1 을 해주어야 문제에서 말하는 점수가 됩니다.
	temp += P.index(S[:f]) + 1
	temp += P.index(S[f:s]) + 1
	temp += P.index(S[s:]) + 1

	result = max(result, temp)

# 답을 출력합니다!
print(result)

# 내 코드와 다른점/ 배울점
# 정해코드에서는 내가 처음에 문제를 봤을 때 생각했던 조합을 사용해서 문제를 풀어냄
# 문자열에서 슬라이싱할 기준점 두개를 뽑는 조합으로 생각할 수 있었는데 나는 그렇게 생각 못하고 for문을 두번 써서 코드 작성함
# 그리고 나는 3개로 슬라이싱한 문자열과 부분문자열들의 리스트를 따로 구했는데
# 정해코드에서는 처음에 set로 선언하고 나중에 list로 변환함으로서 더 간단하게 해결함