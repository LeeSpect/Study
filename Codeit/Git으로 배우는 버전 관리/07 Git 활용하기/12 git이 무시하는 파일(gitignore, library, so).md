우리는 **working directory**에 있는 파일들을

* **git add**
* **git commit**

하면서 프로젝트를 버전 관리합니다. 그런데 working directory 안에 있음에도 불구하고 Git에 의해 그 존재 자체가 무시되는 파일들이 있습니다.

### 1. gitignore 파일 살펴보기 

잠깐 아래 그림을 볼까요?

![image](https://user-images.githubusercontent.com/64893709/104832282-93720900-58d3-11eb-8f0a-7fa6a26764a0.png)

지금 GitHub에서 Mathbox라는 repository를 만드려고 하는데요. 여기서 화면 하단을 보면

```Add .gitignore: None```

이라는 설정 탭이 보입니다. 이 말은 .gitignore 파일을 만들지 않겠다는 뜻입니다. .gitignore 파일이 뭘까요?

```.gitignore``` 파일은

* working directory 내에 존재하는 파일들 중에서
* 마치 존재하지 않는 것처럼
* Git이 인식해야할 파일들을 목록이 적힌 파일입니다.

말그대로 **Git이 ignore(무시)하는 파일들의 이름이 적혀있는 파일**인데요. 이 탭을 클릭해보면,

![image](https://user-images.githubusercontent.com/64893709/104832423-4cd0de80-58d4-11eb-814a-630a06d70e82.png)

알파벡 A부터 순서대로 그 알파벳으로 시작하는 단어들이 등장합니다. 이 단어들은 모두 프로그램이 실행되는 **플랫폼**이나 **프로그래밍 언어**들을 말합니다. 이런 것들 중 하나를 선택하면

* 그 플랫폼에서 실행될 프로그램을 만들거나,
* 해당 프로그래밍 언어로 코드를 작성할 때
* (보통 자동으로) 생성되는 파일들 

중에서 굳이 Git에 의해 버전 관리될 필요가 없는, 불필요한 파일들의 이름이 정리된 **.gitignore** 파일을 자동으로 생성해줍니다.

이번 토픽에서 제가 해온 프로젝트는 코드가 다 파이썬이었죠?

저는 **Python**을 선택할게요.

![image](https://user-images.githubusercontent.com/64893709/104832461-97525b00-58d4-11eb-90f3-5ef498028b32.png)

Python을 검색해서 선택하고

![image](https://user-images.githubusercontent.com/64893709/104832467-a2a58680-58d4-11eb-9dcd-6a45bd44dc68.png)

repository를 생성하면

![image](https://user-images.githubusercontent.com/64893709/104832475-acc78500-58d4-11eb-85ad-834428724d27.png)

이렇게 **.gitignore** 파일이 생성됩니다. 클릭해서 내용을 보면

![image](https://user-images.githubusercontent.com/64893709/104832484-bd77fb00-58d4-11eb-948e-c29fadefb439.png)

여러 파일 이름 또는 directory 이름이 보입니다. 이 중에서 몇 가지만 추려볼게요.

***.py[cod]**

***$py.class**

***.so**

이것들은 모두 무슨 말일까요? 여기서

* *는 그냥 길이 0개 이상의 아무 단어라고 생각하면 됩니다.
* 그리고 대괄호([])는 그 안의 알파벳 중에 하나라고 생각하면 됩니다.

그러니까 지금 이 3가지의 뜻은 아래 표와 같은 겁니다.

![image](https://user-images.githubusercontent.com/64893709/104832528-0465f080-58d5-11eb-9772-ce44014461fb.png)

별로 어렵지 않죠?

여기에 해당하는 파일들은 모두 Git이 그냥 무시해버립니다.

그리고 위 그림에서 

* **build/**
* **develop-eggs/**

처럼 이름 맨 뒤에 **슬래시(/)**가 붙은 것은 directory를 말합니다. 이 2가지는 build directory에 있는 모든 파일과, develop-dggs directory에 있는 모든 파일들도 Git이 무시한다는 뜻이죠.

이렇게 Python의 .gitignore 파일에는 파이썬으로 작업을 하다보면 생겨나는 여러가지 전형적인 부산물들의 이름이 적혀있습니다.

이것들은 딱히

* 버전 관리를 할 정도의 가치가 없고,
* 오히려 버전 관리를 하면 용량만 더 차지하고,
* 나중에 각 버전을 살펴볼 때 가독성을 떨어뜨리기만 하기 때문에

이렇게 Git이 무시하도록 설정한 건데요. 그럼 Git이 무시한다는 게 정확히 어떤 의미일까요? 한번 살펴볼게요.

### 3. Git이 무시한다는 표현의 의미

Mathbox라는 remote repository를 GitHub에서 생성하고 **git clone** 커맨드로 이 remote repository를 제 컴퓨터로 가져왔습니다.

이제 제 컴퓨터에는 Mathbox라는 directory가 생기겠죠?

![image](https://user-images.githubusercontent.com/64893709/104832593-80603880-58d5-11eb-9cb8-8f9b0c997c9f.png)

Mathbox directory 안으로 들어가서 확인해보면 위 그림처럼 **.gitinore** 파일을 볼 수 있습니다.

그 다음 이 working directory 안에서 **calculator.py**라는 파일과 **library.so**라는 파일을 생성했습니다.

그리고 바로 **git status** 커맨드로 확인해보면 아직 **calculator.py** 파일을 아직 git add하지 않았다는 결과가 출력됩니다.

![image](https://user-images.githubusercontent.com/64893709/104832619-b43b5e00-58d5-11eb-8869-e75022611679.png)

그런데 이상하죠? 저는 **library.so**라는 파일도 분명히 생성했는데 왜 **calculator.py**만 뜬 걸까요? 잠깐 다시 스크롤을 올려서

**Python의 .gitignore 파일에 써있던 *.so**

를 찾아보세요. 이 표시에 따라 앞으로 Git은 이 working directory 안에서 **.so**라는 확장자로 끝나는 모든 파일들을 아예 무시하고 신경쓰지 않습니다. **library.so**가 바로 이 조건에 해당하는 이름의 파일이라 Git이 무시한 겁니다.

이 상태에서 **.gitignore 파일을 삭제**하고 **다시 확인**해보면,

![image](https://user-images.githubusercontent.com/64893709/104837025-499a1a80-58f5-11eb-9ac8-dbb249e993be.png)

이번엔 **library.so** 파일도 git add 해주지 않았다는 경고가 뜨는 것을 볼 수 있습니다. **.gitignore 파일이 삭제되어** Git이 이제 모든 파일을 인식하기 때문에 그런 겁니다.

Git이 특정 파일을 무시한다는 게 어떤 의미인지 이제 아시겠죠?

만약 여러분이 working directory에서 버전 관리를 할 필요가 없는 것들이 있다면 이렇게 **.gitignore** 파일에 그 이름을 추가하고 버전 관리를 시작하세요. 그럼 좀더 깔끔하게 버전 관리를 할 수 있습니다. 그리고 앞으로 어떤 파일들을 무시해야할지 잘 모르겠다면 위에서 봤던 것처럼 GitHub에서 기본으로 제공하는 각 플랫폼 또는 프로그래밍 언어별 .gitignore 파일을 참고하세요.
