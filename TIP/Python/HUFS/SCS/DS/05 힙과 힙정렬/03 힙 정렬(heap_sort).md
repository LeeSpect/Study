## 힙 정렬(heap_sort)

1. 입력으로 주어진 리스트 **A**를 ```make_heap```을 호출하여 힙으로 만든다
  * **A**가 힙이 되었으므로, 힙의 루트 노드에는 항상 전체의 최대값이 저장되어 있다.
2. 후트 노드의 값(현재의 최대값) **A[0]** 을 현재 리스트의 가장 마지막 값과 바꾼다
3. 새로 루트노드에 저장된 값은 힙 성질을 만족하지 않을 수 있기 때문에, 자손노드로 내려가면서 힙의 위치를 찾아가야 한다. (heapify_down 함수 호출)
4. 위의 과정 2와 3을 **(n-1)** 번 반복하면 **(n-1)** 개의 수가 정렬되어, 결국 모든 n개의 수가 정렬된다.

```py
def heap_sort(self):
    n = len(self.A)
    for k in range(len(self.A)-1, -1, -1):
        self.A[0],self.A[k] = self.A[k],self.A[0]
        n = n-1  # A[n-1]은 정렬되었으므로
        self.heapify_down(0, n)
```
