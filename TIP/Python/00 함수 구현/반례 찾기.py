from random import randint

# 예제 생성
def example():
    K=randint(1,10)
    N=randint(K,20)
    lines = [0]*K
    for i in range(K):
        lines[i]=randint(1,1000)
    return [K,N,lines]
  
# 맞은 답
def right_sol(K,N,lines):
    s=1
    e=max(lines)
    res=0
    while s<-e:
        cnt=0
        m=(s+e)//2
        for i in lines:
            if i>=m:
                cnt+=i//m
        if cnt<N:
            e=m-1
        else:
            res=m
            s=m+1
    return res
  
# 틀린 답
def wrong_sol(K,N,lines):
    s=0
    e=max(lines)
    res=0
    while s<=e:
        cnt=0
        m=(s+e)//2
        for i in lines:
            if i>m:
                cnt+i//m
        if cnt<N:
            e=m-1
        else:
            res=m
            s=m+1
    return res
  
# 반례 출력
def check():
    ex=example()
    right=right_sol(ex[0],ex[1],ex[2])
    wrong=wrong_sol(ex[0],ex[1],ex[2])
    if right!=wrong:
        print(ex[0],ex[1])
        for i in ex[2]:
            print(i)
        print('맞은 담:',right)
        print('틀린 답:',wrong)
        return
    else:
        check()
check()


# 출처 : https://veggie-garden.tistory.com/37
