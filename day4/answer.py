n = int(input()) #재료 갯수 입력

taste_list = list(map(int, input().split())) #각 재료별 맛의 정도 입력
s = 0 #재료의 맛의 정도의 합

for i in range(n):
	#최대값 이전까지는, 재료의 맛의 정도가 증가하거나 다음 요소와 같아야 함
	if i < taste_list.index(max(taste_list)): 
		if taste_list[i] > taste_list[i+1]: #재료의 맛의 정도가 감소했을 경우
			s = 0 #완벽하지 않은 햄버거이므로 햄버거의 맛은 0이 됨
			break #s가 0이 될 경우 더는 반복문을 진행할 필요 없음
		else:
			s += taste_list[i]
	#최댓값의 경우, 재료 맛의 합 리스트에 추가
	elif i == taste_list.index(max(taste_list)):
		s += taste_list[i]
	#최대값 이후에는 재료의 맛의 정도가 감소하거나 이전 요소와 같아야함
	else:
		if taste_list[i] > taste_list[i-1]: #맛의 정도가 증가했을 경우
			s = 0
			break
		else:
			s += taste_list[i]

#재료의 맛의 정도의 합을 출력
print(s)