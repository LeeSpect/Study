# Dijkstra 최단 경로 알고리즘 구현

# Input:
# 첫 번째 줄에는 노드(정점) 개수 n <= 10,000이 주어진다.
    # 노드는 0번 부터 시작한다고 가정한다.
# 두 번째 줄에는 에지 개수 m <= 100,000이 주어진다.
# 세 번째 줄부터 에지 정보 (세 정수 u v w)가 한 줄에 하나씩 주어진다:
    # u v w는 가중치(cost) w를 갖는 에지 (u,v)임을 나타낸다.
    # u와 v는 [0, .., n-1] 사이의 수로 노드의 번호를 나타낸다.
    # u는 에지 가중치로 양의 정수이다.
    
# Output:
# 소스 노드를 0번 노드라고 할 때, 0번 노드에서 다른 모든 노드까지의 최단 경로의 길이를 차례대로 출력한다. 리스트 dist에 최단 경로 길이가 저장된다면, dist[0], dist[1], dist[2], ..., dist[n-1] 순서로 차례대로 한 줄에 모두 출력하면 된다.
    # dist[0] = 0 임에 주의하자
    # 만약, 소스 노드에서 어떤 노드까지 경로 자체가 존재하지 않는다면 inf을 출력한다.

# Caution:
# 앞 부분에서 배운 heap 자료구조를 사용한다. (여기선 min heap이어야 함)


import sys

def dijkstra(K,V,graph):
    INF = sys.maxsize
    s = [False] * V  # s는 해당 노드 방문 여부를 저장하는 변수
    d = [INF] * V  # d는 memoization을 위한 array이다. d[i]는 정점 k에서 i까지 가는 최소한의 거리가 저장되어 있다.and
    d[K - 1] = 0
    
    while 1:
        m = INF
        N = -1
        
        # 방문하지 않은 노드 중 d값이 가장 작은 값을 선택해 그 노드의 번호를 N에 저장한다.
        # 즉, 방문하지 않은 노드 중 K 정점과 가장 가까운 노드를 선택한다.
        for j in range(V):
            if not s[j] and m > d[j]:
                m = d[j]
                N = j
            
        # 방문하지 않은 노드 중 현재 K 정점과 가장 가까운 노드와의 거리가 INF 라는 뜻은
        # 방문하지 않은 남아있는 모든 노드가 A에서 도달할 수 없는 노드라는 의미이므로 반복문을 빠져나간다.
        if m == INF:
            break
            
        # N번 노드를 '방문'한다.
        # '방문'한다는 의미는 모든 노드를 탐색하며 N번 노드를 통해서 가면 더 빨리 갈 수 있는 노드가 있는지 확인하고,
        # 더 빨리 갈 수있다면 해당 노드(노드의 번호 j라고 하자)의 d[j]를 업데이트 해준다.
        s[N] = True
        
        for j in range(V):
            if s[j]: continue
            via = d[N] + graph[N][j]
            if d[j] > via:
                d[j] = via
    return d
                
if __name__ == "__main__":
    V = int(input())
    E = int(input())
    K = 0
    INF = sys.maxsize
    graph = [[INF]*V for _ in range(V)]
    
    for _ in range(E):
        u,v,w = map(int, input().split())
        graph[u-1][v-1] = w
        
    print(0, end = ' ')
    for d in dijkstra(K, V, graph):
        if d == 0: 
            continue
        elif d != INF:
            print(d, end = ' ')
        else:
            print('inf', end = ' ')
