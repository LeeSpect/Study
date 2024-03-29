# 백준 1786 찾기 풀이
def makeTable(pattern):
    table = [0 for _ in range(len(pattern))]

    idx = 0
    for i in range(1, len(pattern)):
        while idx>0 and pattern[i] != pattern[idx]:
            idx = table[idx-1]
        if pattern[i] == pattern[idx]:
            idx += 1
            table[i] = idx
    return table

def KMP(string, pattern):
    ans = []
    table = makeTable(pattern)
    idx,cnt = 0,0
    for i in range(len(string)):
        while idx>0 and string[i] != pattern[idx]:
            idx = table[idx-1]
        if string[i] == pattern[idx]:
            if idx == len(pattern)-1:
                ans.append(i-idx+1)
                cnt += 1
                idx = table[idx]
            else:
                idx += 1
        
    print(cnt)
    print(*ans)


def main():
    string = input().rstrip()
    pattern = input().rstrip()

    KMP(string, pattern)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------


# 블로그 필자의 학교 알고리즘 책에 나온 코드
# -*- encoding: cp949 -*-
next = [0 for i in xrange(50)]
def initnext(p):
    next[0] = -1
    i = 0; j = -1
    while i<len(p):
        next[i] = next[j] if (p[i]==p[j] and j>=0) else j
        while((j>=0) and (p[i]!=p[j])):
            j = next[j]
        i += 1; j += 1

def kmp(p,t):
    initnext(p)
    i = 0; j = 0
    while j<len(p) and i<len(t):
        while((j>=0) and (t[i]!=p[j])):
            j = next[j]
        i += 1; j += 1
    if j==len(p):
        return i-len(p)
    return i

def main():
    text = 'ababababcababababcaabbabababcaab'
    pattern = 'abababca'
    i = 0; pre = 0
    while True:
        pos = kmp(pattern, text[i:])
        pos += pre
        i = pos + len(pattern)
        if i<len(text):
            print '패턴이 발생한 위치 {}'.format(pos)
        else: break
        pre = i
    print '스트링 탐색 종료.'

if __name__=='__main__':
    main()

# 출처 : https://qkqhxla1.tistory.com/648?category=685988

# ----------------------------------------------------------------------------------------------------

# 블로그 필자의 알고리즘 문제집에 나온 
# -*- encoding: cp949 -*-
def getpartialmatch(N):
    m = len(N)
    pi = [0]*m
    begin = 1; matched = 0
    while begin + matched < m:
        if N[begin + matched] == N[matched]:
            matched += 1
            pi[begin+matched-1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]
    return pi

def kmp(H,N):
    n = len(H); m = len(N)
    ret = []
    pi = getpartialmatch(N)
    begin = 0; matched = 0
    while begin <= n-m:
        if matched < m and H[begin + matched] == N[matched]:
            matched += 1
            if matched == m:
                ret.append(begin)
        else:
            if matched==0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]
    return ret

print kmp('ababbaba','aba')

# 출처 : https://qkqhxla1.tistory.com/648?category=685988

# ----------------------------------------------------------------------------------------------------

def computeLPS(pat, lps):
    leng = 0  # length of the previous longest prefix suffix

    # 항상 lps[0]==0이므로 while문은 i==1부터 시작한다.
    i = 1
    while i < len(pat):
        # 이전 인덱스에서 같았다면 다음 인덱스만 비교하면 된다.
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            # 일치하지 않는 경우
            if leng != 0:
                # 이전 인덱스에서는 같았으므로 leng을 줄여서 다시 검사
                leng = lps[leng-1]
                # 다시 검사해야 하므로 i는 증가하지 않음
            else:
                # 이전 인덱스에서도 같지 않았다면 lps[i]는 0 이고 i는 1 증가
                lps[i] = 0
                i += 1

def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    lps = [0]*M

    # Preprocess the pattern
    computeLPS(pat, lps)

    i = 0  # index for txt[]
    j = 0  # index for pat[]
    while i < N:
        print(i,txt[i],j,pat[j])
        # 문자열이 같은 경우 양쪽 인덱스를 모두 증가시킴
        if pat[j] == txt[i]:
            i += 1
            j += 1
        # Pattern을 찾지 못한 경우
        elif pat[j] != txt[i]:
             # j!=0인 경우는 짧은 lps에 대해 재검사
            if j != 0:
                j = lps[j-1]
            # j==0이면 일치하는 부분이 없으므로 인덱스 증가
            else:
                i += 1

        # Pattern을 찾은 경우
        if j == M:
            print("Found pattern at index " + str(i-j))
            # 이전 인덱스의 lps값을 참조하여 계속 검색
            j = lps[j-1]

# 조금 더 긴 텍스트
txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
# 본문에서 다룬 예제
# txt = 'ABXABㅅBXAB'
# pat = 'ABXAB'
KMPSearch(pat, txt)

# This code is contributed by Bhavya Jain
# 출처 : https://devbull.xyz/python-kmp-algorijeumeuro-munjayeol-cajgi/


```java
char[] txt = br.readLine().toCharArray();
char[] ptn = br.readLine().toCharArray();
int tLen=txt.length, pLen=ptn.length;

// 실패함수 만들기: KMP의 아이디어을 똑같이 적용
int[] pi = new int[pLen];
for(int i=1, j=0; i<pLen; i++){              // i:접미사 포인터
    while(j>0 && ptn[i]!=ptn[j]) j=pi[j-1];  // j:접두사 포인터
    if(ptn[i]==ptn[j]) pi[j] = ++j;
}
```
