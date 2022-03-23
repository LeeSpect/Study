#만약 n개만큼의 정점이 존재하고, m개만큼의 입력을 받는다면 
graph = [[] for _ in range(n+1)] # n+1개만큼의 공간을 만들어서 graph[n]이 n번 정점을 나타내도록 해 준다 
for _ in range(m):
    x,y = map(int,input().split()) #만약 1 2를 입력받으면 
        graph[x].append(y) # 1번 정점에 2를 넣어주고 -> graph[1] = [2] 
        graph[y].append(x) # 2번 정점에 1을 넣어준다 -> graph[2] = [1]
     
# DFS
# def dfs(v):
#     v를 이미 방문한 곳으로 처리한다 
#     for 각각의 v에 연결된 모든 정점 i에 대해서:
#         if i에 방문하지 않았다면:
#             dfs(i)
          
def dfs(v,visited=[]):
    visited.append(v)
    for i in graph[v]:
        if not i in visited:
            visited = dfs(i,visited)
    return visited # [1,2,5,6,7,3,4]
  
#BFS  
# def bfs(v):
#     큐 선언 
#     v를 이미 방문한 곳으로 처리 
#     v를 큐에 추가해준다 
#     while 큐가 비어있지 않다면:
#         큐에서 v를 pop해준다 
#         for v에 연결된 각각의 정점 i에 대하여:
#             if i에 아직 방문하지 않았다면:
#                 i를 방문한 곳으로 처리한다 
#                 큐에 i를 추가한다 

from collections import deque

def bfs(v): 
    visited = [v]
    que = deque([v])
    while que:
        v = que.popleft()
        for i in graph[v]:
            if i not in visited:
                visited.append(i)
                que.append(i)
    return visited # [1, 2, 3, 4, 5, 6, 7]
