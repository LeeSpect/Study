1. sort

원본을 변형시켜 정렬한다. '변수. sort( )' 형태로 사용.   
정렬 기준은 문자열은 알파벳, 가나다순이고 숫자는 오름차순이 기본값이다.

```py
>>> num_list = [15, 22, 8, 79, 10]
>>> num_list.sort()
>>> print(num_list)
[8, 10, 15, 22, 79]

>>> str_list = ['좋은하루','good_morning','굿모닝','niceday']
>>> str_list.sort()
>>> print(str_list)
['good_morning', 'niceday', '굿모닝', '좋은하루']
```



2. sorted
정렬된 결과를 반환. 원형을 변형시키지 않는다. 괄호( ) 안에 반복 가능한 iterable 자료형을 입력하여 사용한다.   
정렬 기준은 문자열은 알파벳, 가나다순이고 숫자는 오름차순이 기본값이다.

```py
>>> print(sorted([15, 22, 8, 79, 10]))
[8, 10, 15, 22, 79]

>>> str_list = ['좋은하루','good_morning','굿모닝','niceday']
>>> print(sorted(str_list))
['good_morning', 'niceday', '굿모닝', '좋은하루']
```



3. Parameter

sort, sorted 모두 key, reverse 매개변수를 갖고 있다.

### 3-1. reverse
bool값을 넣는다. 기본값은 reverse=False(오름차순)이다.   
reverse=True를 매개변수로 입력하면 내림차순으로 정렬할 수 있다.

```py
>>> num_list = [15, 22, 8, 79, 10]
>>> num_list.sort(reverse=True)
>>> print(num_list)
[79, 22, 15, 10, 8]

>>> print(sorted(['좋은하루','good_morning','굿모닝','niceday'], reverse=True))
['좋은하루', '굿모닝', 'niceday', 'good_morning']
```

### 3-2. key
정렬을 목적으로 하는 함수를 값으로 넣는다. lambda를 이용할 수 있다.   
key 값을 기준으로 정렬되고 기본값은 오름차순이다.

```py
>>> str_list = ['좋은하루','good_morning','굿모닝','niceday']
>>> print(sorted(str_list, key=len))  # 함수
['굿모닝', '좋은하루', 'niceday', 'good_morning']

>>> print(sorted(str_list, key=lambda x : x[1]))  # 람다
['niceday', 'good_morning', '굿모닝', '좋은하루']
```

여러 개의 요소를 가진 경우, 튜플로 사용할 수 있다.

```py
>>> tuple_list = [('좋은하루', 0),
    	          ('niceday', 1), 
    	          ('좋은하루', 5), 
    	          ('good_morning', 3), 
    	          ('niceday',5)]
                  
>>> tuple_list.sort(key=lambda x : (x[0], x[1]))  # '-'부호를 이용해서 역순으로 가능
>>> print(tuple_list)
[('good_morning', 3), ('niceday', 1), ('niceday', 5), ('좋은하루', 0), ('좋은하루', 5)]
```

출처 : https://ooyoung.tistory.com/59
