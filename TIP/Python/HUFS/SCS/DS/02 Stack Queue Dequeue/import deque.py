from collections import deque
dq=deque('korea')
print(dq)
>>> deque(['k', 'o', 'r', 'e', 'a'])

# 스택 구현

dq.append('a')
dq.pop()

# 큐 구현
dq.appendleft('a')
dq.popleft()

# deque 확장
dq.extend('you')
dq.extendleft('you')

# 리스트처럼 사용
dq[2] = 'n'
dq.insert(0, 'k')
dq.remove('k')

# deque 좌우반전
dq.reverse()
