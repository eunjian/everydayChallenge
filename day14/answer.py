from collections import deque

# 노드의 개수, 간선의 개수, 시작 노드의 번호 입력
n,m,k = map(int, input().split())
# 간선이 잇는 양끝 정점의 번호들 입력 후 그래프 구현
graph = [[] for _ in range(n+1)]

for i in range(m):
	# 양방향 간선이니까 두개의 노드 모두 간선 추가
	s, e = map(int,input().split())
	graph[s].append(e)
	graph[e].append(s)
	
# 방문 가능한 노드들 작은 순으로 정렬
for i in range(1, n+1):
	graph[i].sort()

# 방문체크할 리스트 생성
v = [False] * (n+1)
# 시작 노드 방문처리
v[k] = True 
# 이동 경로 기록 리스트
l = [k]
# 현재 노드에서 이동가능한 노드들 추가할 수 있는 큐
q = deque([k])
# bfs 이용하여 탐색
while q: # 이동 가능한 노드가 없을 때까지 반복
	node = q.popleft() # 가장 작은 수의 노드부터
	for i in graph[node]: 
		if not v[i]:
			v[i] = True
			q.append(i)
			l.append(i)
			break # 현재의 노드에서 이동했으면 더는 반복문 진행하지 않음

print(len(l), l[-1])