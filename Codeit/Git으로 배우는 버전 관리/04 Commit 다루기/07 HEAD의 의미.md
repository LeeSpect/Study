지금까지 commit 히스토리를 어떻게 보는지 배웠는데요. 이중에서 아직 안 배운 개념이 하나 있습니다. 우선 commit 히스토리를 보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97104370-bc309b00-16f6-11eb-85fc-778a01aebf82.png)

그럼 위에서 노란색으로 표시된 HEAD라는 글자가 보입니다.

![image](https://user-images.githubusercontent.com/64893709/97104400-f437de00-16f6-11eb-837c-c23b81d5b0c4.png)

Git에서 HEAD는 어떤 commit 하나를 가리키는데요. 보통 가장 최근에 한 commit을 가리킵니다.
그리고 commit을 할수록 HEAD는 매번 더 새로운 commit을 가리키게 됩니다.

그렇다면 이런 HEAD는 왜 필요한 걸까요? 여기서 중요한 요소 하나를 알려드리겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97106051-b9d43e00-1702-11eb-9feb-df75a2fdd6df.png)

위에서 노란색으로 표시된 MathTool 디렉토리를 working directory 또는 working tree라고 한다고 했었는데요.
바로 이 working directory의 내부는 HEAD가 가리키는 commit에 따라 다르게 구성됩니다. 

일단 working directory 내부를 살펴볼까요?

![image](https://user-images.githubusercontent.com/64893709/97106075-d2dcef00-1702-11eb-8677-d5837b9b998c.png)

파일 안의 내용들도 확인해보겠습니다.  
calculator.py, License, README 파일도 보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97106123-1a637b00-1703-11eb-9aa7-f44e86b26d59.png)

모든 파일이 최근에 commit 했던 상태 그대로 있는 것을 알 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/97106150-47b02900-1703-11eb-8eaa-2d14aeee4902.png)

이것은 HEAD가 가장 최근에 commit 했던 파일을 가리키고 있어서 그렇습니다.

![image](https://user-images.githubusercontent.com/64893709/97106175-657d8e00-1703-11eb-8f8c-fb7042ed9a33.png)

하지만 HEAD가 다른 commit을 가리키면 working directory 안에 있는 것들은 언제든지 다르게 바뀔 수 있습니다.   
HEAD가 최신 commit보다 더 이전의 commit을 가리키게 되면 working directory의 내부도 그 과거 commit의 모습대로 바뀌게 됩니다. 

![image](https://user-images.githubusercontent.com/64893709/97106232-a37ab200-1703-11eb-8559-62b54e8dbf47.png)
