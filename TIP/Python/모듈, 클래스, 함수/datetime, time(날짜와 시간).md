# datetime 패키지
```datetime``` 패키지에서는 날짜와 시간을 함께 저장하는 ```datetime``` 클래스,
날짜만 저장 ```datetime``` 패키지하는 ```data``` 클래스, 시간만 저장하는 ```time``` 클래스,
시간 구간 정보를 저장하는 ```timedelta``` 클래스 등을 제공한다.

먼저 datetime 패키지를 다움과 같이 임포트한다.
```py
import datetime as dt
```

# datetime 클래스
우선 ```datetime``` 클래스부터 알아보자.
패키지 이름과 클래스 이름이 ```datetime```으로 같기 때문에 사용할 때 주의해야 한다.
또한 다른 클래스와 달리 클래스 이름이 대문자로 시작하지 않는다.
```datetime``` 클래스에는 객체를 생성하지 않고도 바로 클래스에서 사용할 수 있는 클래스 메서드라는 것을 제공한다.
가장 대표적인 것이 현재 시각을 출력하는 ```now()``` 메서드이다.

```py
x = dt.datetime.now()
x

=> datetime.datetime(2021, 10, 2, 15, 27, 4, 517207)
```
```now``` 클래스 메서드는 컴퓨터의 현재 시각을 ```datetime``` 클래스 객체로 만들어 변환한다.
```datetime``` 클래스 객체는 다음과 같은 속성을 가진다.

* ```year```: 연도
* ```month```: 월
* ```day```: 일
* ```hour```: 시
* ```minute```: 분
* ```second```: 초
* ```microsecond```: 마이크로초(micro seconds, 백만분의 일초)

```py
x.year, x.month, x.day, x.hour, x.minute, x.second, x.microsecond

=> (2020, 10, 2, 15, 27, 4, 517207)
```

다음과 같은 메서드도 제공한다.

* ```weekday```: 요일 반환(0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일)
* ```strftime```: 문자열 반환
* ```date```: 날짜 정보만 가지는 ```date``` 클래스 객체 반환
* ```time```: 시간 정보만 가지는 ```time``` 클래스 객체 반환

```py
x.weekday()  # {0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일}

=> 4
```

이 중 특히 많이 사용되는 것이 날짜와 시간 정보를 문자열로 바꿔주는 ```strftime``` 메서드이다.
이 메서드는 어떤형식으로 문자열을 만들지 결정하는 형식 문자열을 인수로 받는다.
형식 문자열은 날짜 및 시간 지정 문자열을 포함한다.
다음은 많이 사용되는 날짜 및 시간 지정 문자열이다.

* ```%y```: 앞의 빈자리를 0으로 채우는 4자리 연도 숫자
* ```%m```: 앞의 빈자리를 0으로 채우는 2자리 월 숫자
* ```%d```: 앞의 빈자리를 0으로 채우는 2자리 일 숫자
* ```%H```: 앞의 빈자리를 0으로 채우는 24시간 형식 2자리 시간 숫자
* ```%M```: 앞의 빈자리를 0으로 채우는 2자리 분 숫자
* ```%S```: 앞의 빈자리를 0으로 채우는 2자리 초 숫자
* ```%A```: 영어로 된 요일 문자열
* ```%B```: 영어로 된 월 문자열

# dateutil 패키지
```strptime``` 클래스 메서드를 사용할 때는 문자열에 맞는 형식 문자열을 사용자가 제공해야 한다.
그러나 ```dateutil``` 패키지의 ```parse``` 함수를 쓰면 자동으로 형식 문자열을 찾아 ```datetime``` 클래스 객체를 만들어 준다.

```py
from dateutil.parser import parse

parse('2016-04-16')
=> datetime.datetime(2016, 4, 16, 0, 0)

parse("Apr 16, 2016 04:05:32 PM")
=> datetime.datetime(2016, 4, 16, 16, 5, 32)
```

다만 월과 일이 모두 12보다 작은 숫자일 때는 먼저 나오는 숫자를 월로 나중에 나오는 숫자를 일로 판단한다.
```py
parse('6/7/2016')
=> datetime.datetime(2016, 6, 7, 0, 0)
```

# 날짜/시간 연산
날짜나 시간의 간격을 구할 때는 두 개의 ```datetime``` 클래스 객체의 차이를 구한다.
이 결과는 ```timedelta``` 클래스 객체로 반환된다.

```py
dt1 = datetime.datetime(2016, 2, 19, 14)
dt2 = datetime.datetime(2016, 1, 2, 13)
td = dt1 - dt2
td

=> datetime.timedelta(days=48, seconds=3600)
```

```timedelta``` 클래스는 다음과 같은 속성과 메서드를 가진다.

속성
* ```days```: 일수
* ```seconds```: 초 (0 ~ 86399)
* ```microseconds```: 마이크로초 (0 and 999999)
메서드
* ```total_seconds```: 모든 속성을 초단위로 모아서 변환

```py
td.days, td.seconds, td.microseconds
=> (48, 3600, 0)

td.total_seconds()
=> 4150800.0
```

반대로 ```datetime``` 클래스 객체에 ```timedelta``` 클래스 객체를 더해서 새로운 시간을 구할 수도 있다.

```py
t0 = datetime.datetime(2018, 9, 1, 13)
d = datetime.timedelta(days=90, seconds=3600)
t0 + d

=> datetime.datetime(2018, 11, 30, 14, 0)
```

```timedelta```의 단점은 날짜와 초 단위로만 연산을 할 수 있다는 점이다.
이를 보완하기 위해 ```dateutil``` 패키지는 월 단위의 계산을 지원하는 ```relativedelta``` 클래스를 제공한다.

예를 들어 특정일의 2달 후 날짜를 구하려면 다음과 같이 실행한다.
```py
from dateutil.relativedelta import relativedelta

t0 + relativedelta(months=2)
=> datetime.datetime(2018, 11, 1, 13, 0)
```

# time 패키지
```time``` 패키지는 실행을 잠시 멈추는 ```sleep``` 함수를 제공한다.
```sleep``` 함수에 n이라는 숫자를 인수로 주면 n초만큼 쉬었다가 다음 코드를 실행한다.

```py
import time

print(1)

time.sleep(5)

print(2)

time.sleep(5)

print(3)

time.sleep(5)

print(4)
```
위 코드를 실행하면 1, 2, 3, 4이라는 숫자가 시간차를 두고 나타나는 것을 알 수 있다.

출처: https://datascienceschool.net/01%20python/02.15%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C%20%EB%82%A0%EC%A7%9C%EC%99%80%20%EC%8B%9C%EA%B0%84%20%EB%8B%A4%EB%A3%A8%EA%B8%B0.html
