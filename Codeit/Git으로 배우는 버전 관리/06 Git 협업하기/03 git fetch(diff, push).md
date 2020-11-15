이전 수업에서는 git으로 다른 개발자와 협업을 하는 상황에서 git push를 하기 전에 git pull을 해야할 때가 많다라고 배웠습니다.

그리고 git pull은 remote repository에 있는 branch를 가져와서 현재 branch에 자동으로 merge하는 커맨드라고 했었습니다.

이때 branch를 가져온다는 것은 그 branch가 가리키고 있는 commit 이전에 이루어진 모든 commit을 가져온다는 뜻입니다.

![image](https://user-images.githubusercontent.com/64893709/99182816-c59fa700-277a-11eb-88f8-c09f928167f6.png)

그런데 이때 merge는 하지 않고 딱 가져오는 단계까지만 해주는 커맨드도 있습니다.

바로 ```git fetch```라는 커맨드입니다.

![image](https://user-images.githubusercontent.com/64893709/99182839-f8499f80-277a-11eb-890f-a6cdc8f14aa3.png)

예를 들어서 회사에 신입 직원이 한 명 들어왔다고 합시다.   
그런데 신입 개발자가 제가 만든 calculator.py 파일을 바꿨다고 생각해보죠. 그것도 잘못된 방향으로요.

( 생략 ) GitHub 페이지에서 calculatory.py 파일을 클릭해 들어갈 건데요. 먼저 premium branch인지 확인해주세요.   
그리고 연필 모양을 눌러서 파일을 수정하겠습니다. 맨 아래에다가 [def say_hello():print("hello")]를 적어주겠습니다.   
commit 메시지도 "Add say_hello function"을 하고 초록색 버튼을 눌러 commit을 해보겠습니다.   
그런데 지금 보니까 say_hello 함수는 계산기 프로그램에 전혀 어울리지 않는 함수입니다.
( 생략 ) 일단 터미널로 돌아가보겠습니다.

터미널로 돌아왔는데요. 만약 지금 git pull을 하면 어떻게 될까요.   
다른 개발자가 코드를 어떻게 추가했는지도 모른 채 내 프로그램에 자동으로 say_hello 함수가 merge되겠죠?   
물론 git pull을 하고 나서 혹시나 이상한 코드가 merge된 것은 아닌지 확인을 해도 되지만 그럼 조금 귀찮아집니다.   

그래서 이렇게 git pull하게 될 내용이 조금 의심스러운 상황에서는 git fetch로 remote repository의 내용을 가져오기만 하는 것이 좋습니다. 한번 해보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99183003-19f75680-277c-11eb-813d-477b631609a1.png)

origin에 있던 premium branch의 commit이 local repository로 들어오게 됩니다.   
노란색으로 표시된 부분은 지금 remote repository에 있는 branch의 내용이 local repository로 들어왔다는 뜻입니다.

![image](https://user-images.githubusercontent.com/64893709/99183042-6b9fe100-277c-11eb-93b9-b7f6cf0800e8.png)

remote repository의 입장에서는 그냥 첫 노란색 표시의 premium branch지만 local repository에서 remote에 있는 premium branch는 두 번째 노란색 표시처럼 나타냅니다.

이제 local repository에 있던 premium branch와 remote repository의 premium branch 사이에 어떤 차이가 있는지 비교해봐야 합니다.

우리가 배웠던 ```git diff```라는 커맨드를 쓰면 됩니다. 그러면 두 commit 간의 차이를 볼 수 있는데요. git diff는 commit 간의 차이뿐만 아니라 branch 간의 차이도 볼 수 있습니다.

우선 git diff를 입력하고 local repository의 premium branch를 써주겠습니다. local repository는 그냥 'premium'이라고 써도 됩니다.   
그리고 한 칸 띄우고 remote repository의 premium branch를 써주겠습니다. remote에서는 'origin/premium'이라고 써주세요.

실행하면,

![image](https://user-images.githubusercontent.com/64893709/99183388-ac98f500-277e-11eb-9f56-2175ab3f7c04.png)

두 branch 사이의 차이점을 확인할 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/99183410-dc47fd00-277e-11eb-987f-49702b02f241.png)

remote repository에 뭔가 문제가 있다는 것을 발견했습니다.

여기서 이 문제를 해결할 수 있는 방법은 두 가지가 있는데요.

![image](https://user-images.githubusercontent.com/64893709/99183420-f4b81780-277e-11eb-9e0d-70c0da670de8.png)

첫 번째는 잘못된 코드를 추가한 개발자에게 함수를 지우고 다시 remote repository에 올려달라고 하는 것입니다. 지금 이 상황에서는 say_hello를 추가한 개발자를 찾아가서 함수를 지우고 다시 repository에 올려달라고 하는 겁니다.

그리고 두 번째는 그냥 제가 잘못된 부분을 알아서 해결하고 다시 git push를 하는 겁니다.

그럼 이 상태에서 remote repository의 premium branch를 merge 하겠습니다. 실행하면,

![image](https://user-images.githubusercontent.com/64893709/99183534-e8808a00-277f-11eb-8157-785044677b00.png)

merge가 잘 됐습니다.

calculator.py 파일을 살펴보겠습니다. 서브라임 텍스트로 이동해주세요.
( 생략 ) calculator.py 파일에 say_hello 함수가 보이죠?   
이 코드는 잘못된 거니까 제거한 다음에 다시 commit을 해주겠습니다.   
( 생략 ) say_hello 함수를 지우고 저장합니다. 그리고 터미널로 이동하고 commit을 해주겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99183586-4d3be480-2780-11eb-8b02-2e1132e3a264.png)

그리고 remote repository로 push 하겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99183602-617fe180-2780-11eb-8255-573fa1d8cc90.png)

그럼 이제 remote repository의 premium branch에서도 calculator.py 파일이 올바르게 바뀌었을 겁니다.

![image](https://user-images.githubusercontent.com/64893709/99183624-88d6ae80-2780-11eb-98bd-da7937f434c7.png)

어떤 경우든 git fetch로 가져와서 git diff로 비교하면서 확인하면 됩니다.

중요한 것은 git pull은 결국 git fetch를 하고 자동으로 merge까지 해주는 커맨드라는 사실입니다.

![image](https://user-images.githubusercontent.com/64893709/99183673-e7039180-2780-11eb-9ff8-f1b968aede4e.png)

그럼 git pull과 git patch 중에 무엇을 써야 하는 걸까요?

![image](https://user-images.githubusercontent.com/64893709/99183697-11ede580-2781-11eb-82f1-93cec88f2cad.png)

한 번 더 검토해야할 필요가 있을 때는 fetch를 사용하면 됩니다.
