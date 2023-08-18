n, k = map(int, input().split()) #정수의 수n, 찾으려는 위치k
int_list = [*map(int,input().split())] #정수 리스트

b_list = [] #변환한 2진수 리스트

#10진수 정수를 2진수로 변환
for i in int_list:
	b = format(i,'b') #2진수로 변환
	b_list.append(b) #2진수 리스트에 추가
	
#2진수들을 1의 개수 기준으로 내림차순 정렬, 1의 개수 같으면 10진수 기준으로 내림차순 정렬
r = sorted(b_list, key=lambda x: (x.count('1'),int(x,2)), reverse=True)

#k번째 위치한 수 10진수로 변환 후 출력 (인덱스는 k-1)
print(int(r[k-1],2))