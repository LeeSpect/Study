# dictionary를 이용한 카운팅
# 아래 코드는 어떤 단어가 주어졌을 때 단어에 포함된 각 알파멧의 글자 수를 세어주는 간단한 함수입니다.
def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter

countLetters('hello world'))
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}



# collections.Counter를 이용한 카운팅
# 파이썬에서 제공하는 collections 모듈의 Counter 클래스를 사용하면 위 코드를 단 한 줄로 줄일 수가 있습니다.

from collections import Counter

Counter('hello world') # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})


# collections.Counter 기본 사용법
# collections 모듈의 Counter 클래스는 파이썬의 기본 자료구조인 사전(dictionary)를 확장하고 있기 때문에, 사전에서 제공하는 API를 그대로 다 시용할 수 있습니다.
# 예를 들어, 주어진 단어에서 가장 많이 등장하는 알파벳과 그 알파벳의 개수를 구하는 함수를 다음과 같이 사전처럼 작성할 수 있습니다.
from collections import Counter

def find_max(word):
    counter = Counter(word)
    max_count = -1
    for letter in counter:
        if counter[letter] > max_count:
            max_count = counter[letter]
            max_letter = letter
    return max_letter, max_count

find_max('hello world') # ('l', 3)



# Counter 클래스는 이와 같은 작업을 좀 더 쉽게 할 수 있도록, 데이터의 개수가 많은 순으로 정렬된 배열을 리턴하는 most_common이라는 메서드를 제공하고 있습니다. 

from collections import Counter

Counter('hello world').most_common() # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]

# 이 메서드의 인자로 숫자 K를 넘기면 그 숫자 만큼만 리턴하기 때문에, 가장 개수가 많은 K개의 데이터를 얻을 수도 있습니다.

from collections import Counter

Counter('hello world').most_common(1) # [('l', 3)]
