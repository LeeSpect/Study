# 단순한 풀이 방법

def getDivisor(n):
  
  divisorsList = []
  
  for i in range(1, n+1):
    if (n%i == 0):
      divisorsList.append(i)
      
  return divisorsList

# 시간 복잡도 : O(N)

# 더 효율적인 풀이방법

def getDivisor(n):
  
  divisorsList = []
  
  for i in range(1, int(n**0.5) + 1):
    if n%1 == 0:
      divisorsList.append(i)
      if i**2 != n:
        dividorsList.append(n // i)
        
  divisorsList.sort()
  
  return dividorsList

# N=A*B로 나타낼 수 있다는 것을 이용한 풀이이다. 항상 약수를 구하면 그 짝이 되는 수가 존재한다.(ex.6=2*3)
# for 문을 이용해 자연수 N의 제곱근까지의 약수를 구하면 그 짝이 되는 약수는 자동으로 구할 수 있다.
# N=A*B일 때, A==B일 수 있기 때문에 (ex. 25=5*5) 값을 중복해서 넣어주지 않기 위해 if 문으로 제곱했을 때 n이 되지 않는지 검사한다.
  # 혹은 i != (n//i)로도 검사할 수 있다.
# 시간 복잡도 O(N**0.5)
