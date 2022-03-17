## 바이너리 서치 - 이진탐색(binary search)

* O(log N)
* 정렬된 자료를 반으로 나누어 탐색하는 방법
* 주의 : 자료는 **오름차순**으로 정렬된 자료여야 한다.
* **퍼포먼스가 좋고** 구현하는 중에 dynamic programing, recursion을 볼 수 있다.

### 특징

* Linear search(순차검색) : 순서대로 찾는. 성능평가시 비교대상으로 사용한다.
* Linear search는 정렬 방식이 상관 없다.
* binary search(이진탐색) : **반드시 정렬된 상태**에서 시작해야한다. 로그실행시간을 보장한다.

### 구현을 위한 준비

* target : 찾고자 하는 값
* data : 오름차순으로 정렬된 list
* start : data의 처음 값 인덱스
* end : data의 마지막 값 인덱스
* mid : start, end의 중간 인덱스

### 구현 개요

* 자료의 중간 값(mid)이 찾고자 하는 값인지 검사
* 아니라면 대소관계를 비교하여 start, end값 이동
* 동일 연산 반복 (재귀로 구현 가능)

### 구현

```py
# data 중에서 target을 검색하여 index 값을 return 한다.
# 없으면 return None

def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return None
    
# 테스트용 코드
if __name__ == "__main__":
    li = [i**2 for i in range(11)]
    target = 9
    idx = binary_search(target, li)
    
    if idx:
        print(li[idx])
    else:
        print(f'찾으시는 타겟 {target}가 없습니다')
```

### 바이너리 서치 재귀적 구현

```py
# data는 오름차순으로 정렬된 리스트
def binary_search_recursion(target, start, end, data):
    if start > end:
        return None
      
    mid = (start + end) // 2
    
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
        
    return binary_search_recursion(target, start, end, data)
    
# 테스트용 코드
if __name__ == '__main__':
    li = [i*3 for i in range(11)]
    target = 6
    idx = binary_search_recursion(target, 0, 10, li)
    
    print(li)
    print(idx)
```


참고
https://wayhome25.github.io/cs/2017/04/15/cs-16/
https://heytech.tistory.com/64
