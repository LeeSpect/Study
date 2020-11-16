이제 무료 버전을 수정해볼건데요. 그러려면 master branch로 이동해야 합니다.

![image](https://user-images.githubusercontent.com/64893709/99248014-2dbdbe00-284b-11eb-849d-ca00992ffdd1.png)

이제 무료 버전에서 어떤 수의 제곱을 해주는 square 함수를 추가해보겠습니다.

calculator.py 파일을 서브라임 텍스트에서 열어주세요.

( 생략 ) square 함수 추가
터미널로 이동해서 commit을 해주겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99258325-bcd2d200-285b-11eb-982b-46693d05a022.png)

이 commit을 remote repository의 master branch에도 반영하겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99258491-fe637d00-285b-11eb-9ec5-2e2c0be9d2f5.png)

무료 버전 작업을 하고 있던 중에 새로운 소식이 들려옵니다.   
square 함수를 추가하지 않기로 결정이 났다고 하네요. 이런 경우에는 어떻게 해야 할까요?
이미 저는 square 함수를 추가하고 remote repository에 push까지 해버렸는데 말입니다.

그러면 square 함수를 지우고 그냥 다시 commit을 하면 되겠죠. 그런데 여기서 이 동작을 한 번에 해주는 Git 커맨드가 있습니다.

먼저 commit history를 보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99258624-3074df00-285c-11eb-83f9-5e2c124ab10d.png)

지금 이런 상태인데요. 위에서 노란색으로 표시된 부분처럼 최신 commit에서 한 작업을 되돌리고 다시 commit을 해주는 커맨드가 있습니다.

바로 ```git revert```라는 커맨드가 있는데요. 다음과 같이 씁니다.

![image](https://user-images.githubusercontent.com/64893709/99258823-77fb6b00-285c-11eb-8840-fe0ab0e4bc88.png)

revert는 되돌리다, 복귀하다라는 뜻을 가지고 있는데요. revert 다음에 되돌리고 싶은 commit의 아이디를 써주면 됩니다.

그리고 실행을 하면,

![image](https://user-images.githubusercontent.com/64893709/99258988-b7c25280-285c-11eb-83aa-2af73bb1de78.png)

위와 같이 commit 메시지를 입력하라는 창이 뜹니다. 노란색으로 표시된 것처럼 Revert "Add square function" 메시지가 자동으로 세팅되어 있네요.

rever를 하면 해당 commit에서 했던 작업을 거꾸로 되돌리고 그것을 다시 commit하게 됩니다. 위의 commit 메시지는 그대로 사용하겠습니다.

```:wq```하고 엔터를 누르면 다음처럼 됩니다.

![image](https://user-images.githubusercontent.com/64893709/99259091-dc1e2f00-285c-11eb-8dab-018d261397d5.png)

revert가 완료된 것을 볼 수 있습니다.

이제 calculator.py 파일을 다시 살펴보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99259223-066fec80-285d-11eb-8863-9b1f0e9b4f49.png)

그러면 우리가 작성했던 square 함수가 사라진 것을 볼 수 있습니다.

다시 commit history도 보겠습니다.


새로운 commit이 하나 생겼죠? 방금 저는 calculator.py 파일에서 square 함수를 직접 지우지는 않았습니다.
단지 git revert라는 커맨드를 써서 square 함수를 추가한 작업을 되돌리는 commit을 새로이 했는데요.

이제 이 새로운 commit도 push를 해주겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99259461-68305680-285d-11eb-86d5-06e2ad9a576b.png)

그러면 remote repository의 master branch에서도 square 함수가 사라졌겠죠?

push를 해주고 나서 다시 commit history를 보도록 하겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99259611-9c0b7c00-285d-11eb-9820-1fcbec7201cb.png)

그러면 local repository의 master branch와 remote repository의 master branch가 이제 같은 commit을 가리키고 있죠?

여기서 어떤 궁금증이 생기신 분들도 계실텐데요.   
어차피 square 함수를 추가하기 직전의 commit으로 reset을 하면 되는 거 아닌가? 이런 생각을 하신 분들도 계실겁니다.
만약 여러분이 local repository에서만 작업중이었다면 그래도 됩니다.
하지만 remote repository를 두고 작업중이라면 안 됩니다.

![image](https://user-images.githubusercontent.com/64893709/99259872-fd334f80-285d-11eb-8b69-d903ddca1ad9.png)

제가 square 함수를 추가하고 나서 git push를 했을 때는 위와 같은 모습입니다.

그런데 만약 이 상태에서 ```git reset```을 했다고 생각해 봅시다.

![image](https://user-images.githubusercontent.com/64893709/99259969-2227c280-285e-11eb-80b8-5a0144dee1ce.png)

그러면 HEAD가 가리키고 있던 master branch가 직전 commit을 가리키게 됩니다. 여기까지는 좋습니다.

![image](https://user-images.githubusercontent.com/64893709/99260246-79c62e00-285e-11eb-892b-c0c862b050ca.png)

그런데 이 상태에서는 ```git push```를 시도할 수 없습니다.   
왜냐하면 지금 remote repository에 더 최신 commit인 "Add square function" commit이 있기 때문에 다음과 같이
```git pull```을 한 후 ```git push```를 하라는 안내문이 출력되게 됩니다.

![image](https://user-images.githubusercontent.com/64893709/99260215-6fa42f80-285e-11eb-8a39-dedb8b91bce7.png)

이것은 지금 제 local repository가 remote repository보다 commit이 한 단계 이전에 있기 때문에 당연한 내용이죠?

![image](https://user-images.githubusercontent.com/64893709/99260388-a417eb80-285e-11eb-9608-2aa3124021f6.png)

하지만 우리가 원래의 위 상태에서 ```git revert```를 했다고 하면 

![image](https://user-images.githubusercontent.com/64893709/99260478-c578d780-285e-11eb-9d88-83bc1640438e.png)

위와 같이 local repository에 새로운 commit이 생기게 됩니다.

이제 push를 해도 아무 문제 없이 실행됩니다.

![image](https://user-images.githubusercontent.com/64893709/99260520-d75a7a80-285e-11eb-90b7-7e3fa0b28535.png)

push를 하고 나면 remote repository도 위처럼 바뀌게 됩니다.

사실 네 번째 commit의 내용과 여섯 번째 commit의 내용은 같습니다.   
하지만 이미 remote repository에 다섯 번째 commit까지 올라가 있기 때문에 이런 낭비는 어쩔 수 없습니다.   
그래서 항상 git push를 하기 전에는 신중해야 합니다.
