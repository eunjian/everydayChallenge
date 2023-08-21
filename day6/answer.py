from itertools import combinations
n = int(input()) #문자열의 길이
s = input() #문자열

p = list() #부분문자열
d = list() #3개로 나뉜 문자열
for i in range(n-2):
	for j in range(i+1,n-1):
		#3개로 나눈 문자열 저장
		d.append([s[:i+1], s[i+1:j+1], s[j+1:]])
		#부분 문자열 저장
		p.append(s[:i+1])
		p.append(s[i+1:j+1])
		p.append(s[j+1:])

#부분문자열 중 중복 제거 후 사전 순서 배열
p = sorted(set(p))

#최대 점수 계산
score = list()
for i in range(len(d)):
	s = 0 #점수
	for item in d[i]:
		s += p.index(item)+1
		score.append(s)

#최대 점수 출력
print(max(score))