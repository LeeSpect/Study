# 참조 : https://brownbears.tistory.com/454

# 최대공약수 구하기
from math import gcd

print(gcd(1071, 1029))
> 21

# 최소공배수 구하기
from math import gcd

def lcm(x,y):
  return  x * y // gcd(x,y)

print(lcm(1071, 1029))
> 52479

# N개의 최소공배수
from math import gcd

def solution(arr):
  def lcm(x,y):
    return x * y // gcd(x,y)
  
  while 1:
    arr.append(lcm(arr.pop(), arr.pop()))
    if len(arr) == 1:
      return arr[0]
    
print(solution([2,6,8,14]))
> 168
