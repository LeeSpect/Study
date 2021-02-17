## re

프로그래밍에서 Regular Expression (RegEx, re, 한국어로는 정규 표현식)은 특정한 규칙/패턴을 가진 문자열을 표현하는 데 사용됩니다.

```
import re

# 알파벳으로 구성된 단어들만 매칭
pattern = re.compile('^[A-Za-z]+$')
print(pattern.match('I'))
print(pattern.match('love'))
print(pattern.match('python3'))

print()

# 숫자가 포함된 단어들만 매칭
pattern = re.compile('.*\d+')
print(pattern.match('I'))
print(pattern.match('love'))
print(pattern.match('python3'))

print()
```
```
------------------------------------------------------------------------------------------
<re.Match object; span=(0, 1), match='I'>
<re.Match object; span=(0, 4), match='love'>
None

None
None
<re.Match object; span=(0, 7), match='python3'>
------------------------------------------------------------------------------------------
```
