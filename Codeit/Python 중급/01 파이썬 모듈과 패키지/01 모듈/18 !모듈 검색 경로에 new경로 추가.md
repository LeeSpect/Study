저번 수업에서는 모듈 검색 경로에 대해 알아봤습니다. 파이썬은 import하려는 module을 찾기 위해서 **sys.path**라는 리스트에 있는 경로들을 살펴보는데요. 이번 수업에서는 **sys.path**에 새로운 경로를 추가하는 방법들을 알아보겠습니다.

## sys.path에 .append()로 경로 추가

첫 번째 방법은 **sys.path**에 새로운 경로를 직접 추가하는 것입니다. **sys.path**는 결국 리스트이기 때문에 **.append()** 함수를 써서 쉽게 새로운 경로를 추가할 수 있습니다.

예를 들어 **sys.path**에 바탕 화면의 경로를 추가하고 싶다면 아래와 같은 코드를 추가해 주면 됩니다.

run.py
``` python
import sys
sys.path.append('/Users/codeit/Destkop') # macOS
sys.path.append('C:\\Users\\codeit\\Desktop') # Windows
```

윈도우스의 경로 같은 경우 역슬래시를 2개 써주는데요. 프로그래밍에서는 \<char> 패턴을 가진 특수문자들이 있습니다. 예를 들어 \t는 탭을 뜻하고 \n은 새로운 줄을 뜻합니다. 윈도우스 파일 경로는 \가 들어가기 때문에 \와 다음 문자가 특수 문자로 인식될 수 있겠죠? 그래서 윈도우스 파일 경로를 다룰 때는 \를 뜻하는 특수 문자, \\를 사용해야 합니다.

그러면 이제 import하고자 하는 module을 찾을 때 바탕 화면도 찾아보겠죠? 예를 들어 바탕화면에 test.py라는 새로운 파일을 만들고:

![image](https://user-images.githubusercontent.com/64893709/112156007-35da9f80-8c29-11eb-8378-a5070362ad23.png)

**test** module을 run 파일에서 import 해주면 (import문은 바탕화면의 경로가 **sys.path**에 추가된 후에 실행돼야 합니다.) 아무 오류 없이 module이 import됩니다.

![image](https://user-images.githubusercontent.com/64893709/112156306-789c7780-8c29-11eb-9fdb-35f6ffdac664.png)

그리고 바탕화면의 경로가 **sys.path**에 추가된 것을 확인할 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/112156385-8baf4780-8c29-11eb-80d0-8d99cb6b76c8.png)

## sys.path에 영구적으로 경로 추가

**sys.path**에 어떤 경로를 **append()** 해주고 프로그램이 종료되면 그 경로는 **sys.path**에서 사라집니다. 그 경로에 있는 module을 쓰고 싶으면 매번 **append()**를 해줘야 합니다.

그럼 어떤 경로를 영구적으로 **sys.path**에 추가하려면 어떻게 해야 할까요?

PyCharm의 설정(Windows: File -> Settings, macOS: PyCharm -> Preferences)으로 가서 Project 탭 안에 있는 Project Interpreter를 클릭해 줍니다.

![image](https://user-images.githubusercontent.com/64893709/112156721-dd57d200-8c29-11eb-9f3b-ad76daa45c73.png)

그리고 톱니바퀴 버튼을 누른 후 Show All 옵션을 클릭해 줍니다.

![image](https://user-images.githubusercontent.com/64893709/112156802-eea0de80-8c29-11eb-81f0-2a0ced66f3c9.png)

![image](https://user-images.githubusercontent.com/64893709/112156845-f8c2dd00-8c29-11eb-9491-de6e879966d2.png)

그런 다음에 파일 경로 아이콘을 클릭해 줍니다.

![image](https://user-images.githubusercontent.com/64893709/112156910-09735300-8c2a-11eb-8d5d-9239a13bdeaa.png)

그리고 + 아이콘을 누른 후 원하는 경로를 추가해줍니다. (밑에 사진은 바탕화면의 경로를 추가해줍니다.)

![image](https://user-images.githubusercontent.com/64893709/112158108-34aa7200-8c2b-11eb-91fa-0e5e96016a26.png)

![image](https://user-images.githubusercontent.com/64893709/112158152-3ffd9d80-8c2b-11eb-9d7e-23265c9d5eb8.png)

그리고 OK를 눌러줍니다.

![image](https://user-images.githubusercontent.com/64893709/112158226-4f7ce680-8c2b-11eb-9a07-f4e9d30074bb.png)

그러면 이제 코드에서 **sys.path.append()**를 지워도 바탕화면에 있는 **test** module이 import됩니다. 그리고 **sys.path**에 바탕화면의 경로가 나오는 것을 확인할 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/112158389-76d3b380-8c2b-11eb-8c60-b2375afaced5.png)


