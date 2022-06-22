[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 의 정렬된 배열이 있을 때,
현재 정렬된 상태를 유지하면서 n = 5 이라는 요소를 배열에 추가하고 싶다고 해봅시다.
어떤 인덱스에 넣어야하는지 계산하는 함수를 구해봅시다.

## 이분 탐색을 사용하지 않고 구현
```python
nums = [0,1,2,3,4,5,6,7,8,9]
n = 5
for i in range(len(nums)):
	if n <= nums[i]:
    	break
result = i
print(result)

'''
결과값
5
'''
```
이 방법은 직관적이고 구현이 매우 쉽지만, n 이 커지게 되면 배열을 전부 탐색해야하니 , 정렬된 배열인 점을 전혀 이용하지 못하게 되어 O(n)의 시간 복잡도를 가집니다. 그래서 보통 이분탐색으로 구현을 하죠!

## 이분 탐색을 사용해서 구현
```python
nums = [0,1,2,3,4,5,6,7,8,9]
n = 5
l = 0
r = len(nums)-1
result = 0
while l <= r:
	mid = (l+r) // 2
    if nums[mid] >= n:
    	result = mid
        r = mid - 1
    else:
    	l = mid + 1
       
print(result)

'''
결과값
5
'''
```
배열이 오름차순으로 정렬된 점을 이용해서, mid를 집고, mid 인덱스의 값이 작으면 l(left) 을 mid +1 로 올려 다음 후보 값을 높여주고, 아니면 r(right)을 mid -1 로 내려 다음 후보 값을 낮춰주는 방식입니다. 절반씩 후보를 줄여가기에 O(logN) 이 성립합니다.

이 방법을 간단하게 해주는 것이 bisect 입니다!!

# bisect 사용

* bisect_left(literable, value) : 왼쪽 인덱스를 구하기
* bisect_right(literable, value) : 오른쪽 인덱스를 구하기

### 예제 1
```python
from bisect import bisect_left, bisect_right

nums = [0,1,2,3,4,5,6,7,8,9]
n = 5

print(bisect_left(nums, n))
print(bisect_right(nums, n))

'''
결과값
5
6
'''
```

### 예제 2
```python
from bisect import bisect_left, bisect_right

nums = [4, 5, 5, 5, 5, 5, 5, 5, 5, 6]
n = 5

print(bisect_left(nums, n))
print(bisect_right(nums, n))


'''
결과값
1
9
'''
```

### 응용하기 (특정 범위에 속하는 원소의 개수 구하기)
```python
from bisect import bisect_left, bisect_right


def calCountsByRange(nums, left_value, right_value):
    r_i = bisect_right(nums, right_value)
    l_i = bisect_left(nums, left_value)
    return r_i - l_i


nums = [-1, -3, 5, 5, 4, 7, 1, 7, 2, 5, 6]

# 5 ~ 7 을 갖는 요소의 개수 구하기
nums.sort()  # 정렬은 필수
print(calCountsByRange(nums, 5, 7))

'''
결과값
6
'''
```

출처: https://programming119.tistory.com/196 [개발자 아저씨들 힘을모아:티스토리]
