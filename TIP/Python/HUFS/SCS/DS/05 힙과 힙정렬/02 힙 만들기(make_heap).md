## 힙 class

```py
class Heap:
    def __init__(self, L=[]):  # 입력 리스트가 없으면 빈 리스트를 default 값으로 지정
        self.A = L
    def __str__(self):
        return str(self.A)
    def __len__(self):
        return len(self.A)
```

## 힙 만들기

1. 리스트 A가 힙의 값 조건(각 노드는 자손노드 값보다 작으면 안 된다)을 만족하지 않는다면, 값 조건을 만족하도록 리스트의 값을 재배열한다.
2. A[k]는 자신의 자손 노드들과 같거나 커야 한다. 이 성질을 만족하도록 A[k]를 자식노드의 값과 비교하면서 더 큰 값을 갖는 자식노드와 swap하는 과정을 더 이상 필요 없을 때까지 반복하낟. 이 과정을 함수 heapify_down으로 작성한다.
  * heapify_down(k, n) : A[k] 가 밑으로 내려가면서 heap 성질을 만족하는 위치로 보냄. (여기서 n은 heap의 노드 수이며 heap_sort를 위해 필요한 매개변수임)
3. 그러면 마지막 노드인 A[n-1] 부터 첫 노드 A[0]까지 차례로 heapfiy_down을 호출해 make_heap을 완성한다.

```py
def heapify_down(self, k, n):
    # n = 힙의 전체 노드 수 [heap_sort를 위해 필요함]
    # A[k]가 힙 성질을 위배한다면, 밑으로
    # 내려가면서 힙성질을 만족하는 위치를 찾는다

while 2*k+1 < n:  # [ ? ] 조건문이 어떤 뜻인가?
    L, R = 2*k+1, 2*k+2  # [ ? ] L, R은 어떤 값?
    if L < n and self.A[L] > self.A[k]:
        m = L
    else:
        m = k
    if R < n and self.A[R] > self.A[m]:
        m = R  # m = A[k], A[l], A[R] 중 최대값의 인덱스
    if m != k:  # A[k]가 최대값이 아니라면 힙 성질 위배
        self.A[k], self.A[m] = self.A[m], self.A[k]
        k = m
    else: break  #왜 break할까?

def make_heap(self):
    n = len(self.A)
    for k in range(n-1, -1, -1):  # A[n-1] -> ... -> A[0]
        self.heapify_down(k, n)
```
