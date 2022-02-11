##### heapify
# heapq 모듈의 heapify ㅎ마수는 주어진 리스트를 힙 정렬할 때 사용합니다. 이때의 Time Complexity는 O(nlogn)입니다.

import heapq

my_list = [3, 2, 1, 5, 7]
heapq.heapify(my_list) #[1,2,3,5,7]


##### heappop(heap)
# heapq 모듈에서의 heappop 함수는 힙 정렬된 리스트에서 아래와 같은 역할을 합니다.
# 1. 가장 작은 원소를 빼낸다.
# 2. 나머지 원소가 힙을 유지하도록 정렬한다.
# ✔️리스트가 힙 정렬되어 있지 않은 상태에서 heappop 사용 시, 이상한 결과가 나올 수 있습니다!!

import heapq
my_list = [13, 2, 1, 5, 10]
heapq.heapify(my_list)

# 가장 작은 원소인 1이 리턴됩니다. my_list의 길이가 하나 줄어듭니다.
ret_val = heapq.heappop(my_list)

print("리턴된 값:", ret_val) # 1
print("남은 원소:", my_list) # [2,5,13,10]


##### heappush(heap, item)
# heapq 모듈에서의 heappush 함수는 리스트의 힙 상태를 유지하며, 데이터를 삽입시켜 줍니다.
# ✔️리스트가 힙 정렬되어 있지 않은 상태에서 heappush 사용 시, 이상한 결과가 나올 수 있습니다!!

import heapq
my_list = [13, 2, 1, 5, 10]
heapq.heapify(my_list)

# 7 삽입
heapq.heappush(my_list, 7)

# 기존에 가장 작았던 원소가 계속 앞에 위치
print("남은 원소:", my_list)
# 남은 원소: [1, 2, 7, 5, 10, 13]


##### 가장 작은 원소에 접근하는 방법
# heap 리스트에서 가장 작은 원소를 삭제하지 않고 단순히 읽기만 사용할 때 리스트와 같이 사용할 수 있습니다

import heapq
my_list = [13, 2, 1, 5, 10]
heapq.heapify(my_list)

# heappop을 하지만, 맨 앞 원소가 최솟값임은 변하지 않음
while my_list:
    print("리스트의 맨 앞 원소:", my_list[0])
    heapq.heappop(my_list)

'''
리스트의 맨 앞 원소: 1
리스트의 맨 앞 원소: 2
리스트의 맨 앞 원소: 5
리스트의 맨 앞 원소: 10
리스트의 맨 앞 원소: 13
'''


##### 최대 힙 (Max Heap) 구현하기
# heapq는 최소 힙이라는 것을 이용하여 모든 값에 -를 붙여 - 최대 값이 최소 값이 되도록 구현할 수 있습니다.

import heapq

nums = [5,1,10,13,2]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print("리스트의 맨 앞 원소 :", heapq.heappop(heap)[1])  # index 1
  
'''
리스트의 맨 앞 원소: 13
리스트의 맨 앞 원소: 10
리스트의 맨 앞 원소: 5
리스트의 맨 앞 원소: 2
리스트의 맨 앞 원소: 1
'''


##### K번째 최소값 / 최댓값 구하기
# Heap을 사용하여 K 번째의 최소값, 최대값을 효율적으로 구할 수 있습니다.

import heapq

def kth_smallest(nums, k):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)

  kth_min = None
  for _ in range(k):
    kth_min = heapq.heappop(heap)
  return kth_min

print(kth_smallest([4, 1, 7, 3, 8, 5], 3)) # 4
