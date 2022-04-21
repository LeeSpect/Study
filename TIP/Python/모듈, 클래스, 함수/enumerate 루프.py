for entry in enumerate(['A', 'B', 'C']):
    print(entry)
# (0, 'A')
# (1, 'B')
# (2, 'C')


# enumerate() 함수는 기본적으로 인덱스와 원소로 이루어진 tuple을 만들어주니다.
# 따라서 인덱스와 원소를 각각 다른 변수에 할당하고 싶다면 인자 풀기(unpacking)를 해줘야 합니다.
for i, letter in enumerate(['A', 'B', 'C']):
    print(i, letter)
# 0 A
# 1 B
# 2 C



## 시작 인덱스 변경

# 루프를 돌리다보면 인덱스를 0이 아니라, 1로 시작하고 싶을 때가 있습니다.
# 이럴 때는 enumertae() 함수를 호출할 때 start 인자에 시작하고 싶은 숫자를 넘기면 됩니다.
for i, letter in enumerate(['A', 'B', 'C'], start=1):
    print(i, letter)
# 1 A
# 2 B
# 3 C
for i, letter in enumerate(['A', 'B', 'C'], start=101):
    print(i, letter)
# 101 A
# 102 B
# 103 C


## enumerate() 원리

# 파이썬에서 for 문은 내부적으로 in 뒤에 오는 목록을 대상으로 계속해서 next() 함수를 호출하고 있다고 생각할 수 있습니다.
# 따라서 일반 리스트를 iter() 함수에 넘겨 반복자(iterator)로 만든 후 next() 함수를 호출홰보면 원소들이 차례로 얻어지는 것을 알 수 있습니다.
iter_letters = iter(['A', 'B', 'C'])
next(iter_letters)
# 'A'
next(iter_letters)
# 'B'
next(iter_letters)
# 'C'

# 이번에는 enumerate() 함수를 호출한 결과를 대상으로 next() 함수를 계속해서 호출해보면,
# 인덱스와 원소의 쌍이 튜플의 형태로 차례로 얻어지는 것을 알 수 있습니다.
enumerate_letters = enumerate(['A', 'B', 'C'])
next(enumerate_letters)
# (0, 'A')
next(enumerate_letters)
# (1, 'B')
next(enumerate_letters)
# (2, 'C')

# 결국, enumerate() 함수는 인자로 넘어온 목록을 기준으로
# 인덱스와 원소를 차례대로 접근하게 해주는 반복자 객체를 반환해주는 함수입니다.
# 이 부분은 enumerate() 함수의 반환 값을 리스트로 변환해보면 좀 더 명확하게 확인할 수 있습니다.


## [팁] 2차원 리스트 루프
# 아래와 같은 2차원 리스트나 터플이 담고 있는 데이터를 루프를 돌면서 접근해야한다고 가정해봅시다.
matrix = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
# for 문 내에서는 아래와 같이 표현됩니다.
>>> for r in range(len(matrix)):
...     for c in range(len(matrix[r])):
...             print(r, c, matrix[r][c])
...
0 0 A
0 1 B
0 2 C
1 0 D
1 1 E
1 2 F
2 0 G
2 1 H
2 2 I
# enumerate() 함수로 작성해보면 아래와 같이 표현할 수 있습니다.
>>> for r, row in enumerate(matrix):
...     for c, letter in enumerate(row):
...             print(r, c, letter)
...
0 0 A
0 1 B
0 2 C
1 0 D
1 1 E
1 2 F
2 0 G
2 1 H
2 2 I

# 2차원 배열을 다룰 때 인덱스를 사용하면 오타를 내기 쉬운데,
# enumerate() 함수를 사용하면 이러한 실수를 할 확률이 현저하게 줄어듭니다.

# 출처: https://www.daleseo.com/python-enumerate/
