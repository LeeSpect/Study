# 1. 순열(=permutations);  permutations(반복 가능한 객체, r)
# 반복 가능한 객체(=길이가 n인)에 대해서 중복을 허용하지 않고 r개를 뽑아서 나열한다.
# 뽑힌 순서대로 나열하기 때문에 순서가 의미가 있다. (같은 값이 뽑히더라도 순서가 다르면 다른 경우의 수)

from itertools import permutations

for i in permutations([1,2,3,4], 2):
    print(i, end=' ')
# (1, 2) (1, 3) (1, 4) (2, 1) (2, 3) (2, 4) (3, 1) (3, 2) (3, 4) (4, 1) (4, 2) (4, 3)

l=list(permutations([1,2,3,4],2))
print(l)
# [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]


# 2. 조합(combinations); combinations(반복 가능한 객체, r)
# 반복가능한 객체(=길이가 n인)에 대해서 중복을 허용하지 않고 r개를 뽑는다.
# 어떤 것을 뽑는지만 중요하게 보기 때문에 순서는 고려하지 않는다.

from itertools import combinations

for i in combinations([1,2,3,4], 2):
    print(i, end=' ')
# (1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4)


# 3. 중복 순열(=product); product(반복 가능한 객체, repeat=1)

from itertools import product

for i in product([1,2,3],'ab'):
    print(i, end=" ")
# (1, 'a') (1, 'b') (2, 'a') (2, 'b') (3, 'a') (3, 'b') 

for i in product(range(3), range(3), range(3)):
    print(i, end=" ")
# (0, 0, 0) (0, 0, 1) (0, 0, 2) (0, 1, 0) (0, 1, 1) (0, 1, 2) (0, 2, 0) (0, 2, 1) (0, 2, 2) (1, 0, 0) (1, 0, 1) (1, 0, 2) (1, 1, 0) (1, 1, 1) (1, 1, 2) (1, 2, 0) (1, 2, 1) (1, 2, 2) (2, 0, 0) (2, 0, 1) (2, 0, 2) (2, 1, 0) (2, 1, 1) (2, 1, 2) (2, 2, 0) (2, 2, 1) (2, 2, 2) 

for i in product([1,2,3], repeat=2):
    print(i, end=" ")
# (1, 1) (1, 2) (1, 3) (2, 1) (2, 2) (2, 3) (3, 1) (3, 2) (3, 3) 

for i in product([1,2,3], repeat=3):
    print(i, end=" ")
# (1, 1, 1) (1, 1, 2) (1, 1, 3) (1, 2, 1) (1, 2, 2) (1, 2, 3) (1, 3, 1) (1, 3, 2) (1, 3, 3) (2, 1, 1) (2, 1, 2) (2, 1, 3) (2, 2, 1) (2, 2, 2) (2, 2, 3) (2, 3, 1) (2, 3, 2) (2, 3, 3) (3, 1, 1) (3, 1, 2) (3, 1, 3) (3, 2, 1) (3, 2, 2) (3, 2, 3) (3, 3, 1) (3, 3, 2) (3, 3, 3) 


# 4. 중복 조합(=combinations_with_replacement); combinations_with_replacement(반복 가능한 객체, r)

from itertools import combinations_with_replacement

for cwr in combinations_with_replacement([1,2,3,4], 2):
    print(cwr, end=" ")
# (1, 1) (1, 2) (1, 3) (1, 4) (2, 2) (2, 3) (2, 4) (3, 3) (3, 4) (4, 4) 


# 출처: https://juhee-maeng.tistory.com/91
