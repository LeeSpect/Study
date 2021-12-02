### 문자 개수 세기 (count)
>>> a = "hobby"
>>> a.count('b')
2

### 위치 알려주기1 (find)
>>> str = 'abcabcabc'
>>> str.find('b')
1
>>> str.find('b', 2)
4
>>> str.find('k)
-1
             
### 위치 알려주기2 (index)
>>> a = "Life is too short"
>>> a.index('t')
8
>>> a.index('k')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: substring not found   # find 함수와 다른 점은 문자열 안에 존재하지 않는 문자를 찾으면 오류가 발생한다는 점이다.
            
### 문자열 삽입(join)
>>> ",".join('abcd')
'a, b, c, d'
>>> ",".join(['a', 'b', 'c', 'd'])
'a,b,c,d'

### 소문자를 대문자로 바꾸기 (upper) a.upper()
### 대문자를 소문자로 바꾸기 (lower) a.lower()
             
### 왼쪽 공백 지우기 (lstrip) a.lstrip()
### 오른쪽 공백 지우기 (rstrip) a.rstrip()
### 양쪽 공백 지우기 (strip) a.strip()
             
### 문자열 바꾸기 (replace)             
>>> a = "Life is too short"
>>> a.replace("Life", "Your leg")
'Your leg is too short'                      
