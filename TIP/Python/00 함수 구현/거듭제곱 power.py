def power(a, n):
    if n == 0:
        return 1
    
    x = power(a, n//2)

    if n % 2 == 0:
        return x * x
    
    else:
        return x * x * a
      
# 분할 정복 활용

# 지수법칙을 활용한다.
# 두 제곱의 밑인 a가 같을 때 a의 n제곱과 a의 m제곱을 곱한 수는 a^(n+m)으로 표현할 수 있다.
# 이는 a^n = a^(n/2) * a^(n/2)로 표현할 수 있다.

# 홀수라면 a를 한 번더 곱해준다.
# a = 2, n -5라면,
# 2**5 = 2^2 * 2^2 * 2 로 표현할 수 있다.

# 즉, n을 2로 나누어 거 작은 문제로 해결하는 분할 정복 방식이다.

# n을 2로 나누는 과정에서 n이 1일 때, 다음 재귀함수에 들어가는 n은 0이 될 수 있으므로(1//2 = 0), Base Case에 n이 0일 때 return할 값도 포함한다.
# 사실 Base Case는 n이 0일때만 처리해주면 된다. n이 1이 될 때는 power(a, 1 // 2)가 호출되므로 이는 즉 power(a, 0)을 호출하기 때문이다.

# https://seongonion.tistory.com/88


# 아래는 1629 boj 문제
# 자연수 A를 B번 곱하고 C로 나눈 나머지
import sys; input=sys.stdin.readline

def power(a,b,c):
    if b==1:
        return a%c
    else:
        k=power(a,b//2,c)
        if b%2:
            return k*k*a%c
        else:
            return k*k%c

a,b,c=map(int,input().split())

a=power(a,b,c)
print(a)

# 2147483646 2147483646 2147483647
# ans: 1
# 2 222 41 <= 반례들: 처음에 재귀 함수 호출할 때 매개변수를 a%c, b%c, c로 하면 틀리는 케이스
# ans: 4
# 3 200 241
# ans: 225
