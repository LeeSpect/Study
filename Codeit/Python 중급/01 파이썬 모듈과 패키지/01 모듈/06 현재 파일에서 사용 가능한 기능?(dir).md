이번 수업에서는 유용한 내장함수 하나를 소개해 드릴 건데요.

바로 dir이라는 함수입니다. 이 함수는 어떤 파일 안에서 정의된 모든 이름들을 알려주는 함수입니다.

area 모듈을 가져와서 dir(area)를 출력해보면,

![image](https://user-images.githubusercontent.com/64893709/106120450-bfc23b00-6199-11eb-8696-8b79cce97566.png)

area 모듈 안에 정의된 이름들을 확인할 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/106120738-14fe4c80-619a-11eb-9b71-f508e6dc668c.png)

위처럼 여러 이름들이 나오는데요. 저희가 area 모듈에서 정의한 'PI', 'circle', 'square'를 다 볼 수 있습니다.

그런데 이 세 개 말고도 다른 이름들도 나오는데요. 모두 이름 양옆에 언더 스코어(_)가 두 개씩 붙어 있습니다.

파이썬에서는 이렇게 이름 양옆에 언더 스코어(_)가 두개 씩 붙은 애들을 ```특수 변수```라고 부릅니다.

이걸 읽을 떄는 보통 ```던더```라는 단어를 사용하는데요.

던더는 ```더블 언더 스코어```를 줄인 말입니다.

그러니까 이런 파일들을 ```던더 파일```이라고 읽는 거죠.

특수 변수는 파이썬이 내부적으로 관리하는 변수들인데요. 일단 지금은 더 자세히 알아보지는 않겠습니다.

자, 이번에는 dir 함수를 써서 현재의 이 run 파일에서 정의된 이름들을 확인해 보겠습니다. 

![image](https://user-images.githubusercontent.com/64893709/106125093-154d1680-619f-11eb-9398-750f0d0c8f2d.png)

그러려면 위처럼 그냥 dir 함수 안에 아무 파라미터도 안 넣어 주면 됩니다. 한번 실행해 보면,

![image](https://user-images.githubusercontent.com/64893709/106127239-b210b380-61a1-11eb-88d6-90cd93db0991.png)

이번에도 이렇게 다양한 특수 변수들이 나오고 맨 뒤에 보면 area가 나오죠?

모듈을 import 하면 이 파일에서는 모듈의 이름만 정의되고 모듈 안에 있는 함수나 변수에 이름들은 정의되지 않습니다. PI나 square 또는 circle은 여기 나타나지 않는 거죠.

그리고 import area 뒤에 as ar을 붙여주면

![image](https://user-images.githubusercontent.com/64893709/106131557-2e0cfa80-61a6-11eb-859b-ff2ae6796d68.png)

이번에는 area 대신 ar이라고 나옵니다.

마지막으로 area 모듈의 함수들을 직접 가져와 볼게요.

from area import circle, square 이걸 실행해 보면

![image](https://user-images.githubusercontent.com/64893709/106131639-48df6f00-61a6-11eb-90dc-f8d53043695c.png)

이번엔 area는 나오지 않고 circle이랑 square만 나옵니다.

이렇게 import 방식에 따라 파일에 추가되는 이름이 달라지는데요.

이걸 이용하면 프로그램에서 사용된 이름들을 더 쉽게 관리할 수 있습니다.
