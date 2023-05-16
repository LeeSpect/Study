# 재귀로 구현한 find 함수: 시간 초과 가능성
# def find_parent(parents,node1):
#     if parents[node1]!=node1:
#         parents[node1]=find_parent(parents,parents[node1])
#     return parents[node1]

# find 함수를 while 문으로 작성
def find_parent(parents,node1):
    while parents[node1] != node1:
        parents[node1] = parents[parents[node1]]
        node1 = parents[node1]
    return parents[node1]

def Union(parents,node1,node2):
    a = find_parent(parents,node1)
    b = find_parent(parents,node2)
    
    if a == b:
        return False
    elif a < b:
        parents[b] = a
    else:
        parents[a] = b
    return True
