이번 시간에는 git rebase라는 것을 배워보겠습니다.

우선 git rebase가 뭔지 설명하기 전에 현 상황부터 설명하도록 하겠습니다. 

![image](https://user-images.githubusercontent.com/64893709/100518675-4d9f9b00-31d6-11eb-98a0-aefaa55dd2f9.png)

일단 저는 지금 premium branch에 있는데요. 이 상태에서 실험용 branch를 하나 더 만들겁니다.

그리고 앞으로 premium 버전에 좀 복잡한 함수를 추가해야 할 때는 추가하기 전에 실험용 branch에서 실험을 하고 나서 premium branch에 추가할 것입니다.

우선 실험용 branch를 만들겠습니다.

![image](https://user-images.githubusercontent.com/64893709/100518714-97888100-31d6-11eb-89a3-fab382db6ee6.png)

그리고 현재 위치은 premium branch에서 간단한 함수 하나를 추가하겠습니다.   
( 생략 ) 서브라임 텍스트로 이동해 주세요.   
( 생략 ) 나머지를 구하는 get_Remainder 함수를 추가하겠습니다.

commit을 해주겠습니다.

![image](https://user-images.githubusercontent.com/64893709/100518755-f0f0b000-31d6-11eb-9717-a165032a6c67.png)

그리고 방금 만든 test branch로 가서 두 수의 중간값을 구해주는 get_Median 함수를 추가하겠습니다.

우선 test branch로 이동한 다음,

![image](https://user-images.githubusercontent.com/64893709/100518917-f8648900-31d7-11eb-8536-feada684def8.png)

( 생략 ) 그리고 다시 서브라임 텍스트로 이동합니다.
( 생략 ) get_Median 함수를 추가해줍니다.

터미널로 이동해서 commit을 해주겠습니다.

![image](https://user-images.githubusercontent.com/64893709/100518966-4ed1c780-31d8-11eb-9316-cc056887626a.png)

여기까지 했는데 회사에서 좋은 소식이 하나 들려옵니다. 우리가 test branch에 추가했던 get_Median 함수를 이제 premium branch에 추가해도 된다는 결정이 났습니다.   
그러면 premium branch에 test brach를 merge하면 될 것 같습니다.

일단 premium branch로 이동해볼게요.

![image](https://user-images.githubusercontent.com/64893709/100519057-d6b7d180-31d8-11eb-9f7e-f1201a2beab1.png)

이제 test branch를 merge하겠습니다.

![image](https://user-images.githubusercontent.com/64893709/100519078-f5b66380-31d8-11eb-9085-81d5cab09a97.png)

그러면 위에서 노란색으로 표시된 것처럼 CONFLICT가 출력되는데요.

( 생략 ) 잠깐 calculator.py 파일을 확인해보겠습니다.
( 생략 ) conflict가 생긴 함수들을 모두 남겨둔 후 불필요한 부분은 삭제하고 다시 저장을 해주겠습니다.

그리고 다시 commit을 해주면 다음과 같은 화면이 출력되는데요.

![image](https://user-images.githubusercontent.com/64893709/100519139-63fb2600-31d9-11eb-8edb-9a4f86621426.png)

```:wq```로 기존의 내용을 변경하지 않은 채 commit을 마무리하겠습니다.

commit history를 살펴보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/100519194-b63c4700-31d9-11eb-9619-f185727a075d.png)

위처럼 두 branch가 잘 merge된 것을 볼 수 있습니다.

그런데 방금처럼 git merge를 하지 않고 git rebase를 쓰는 방법도 있습니다. 오늘은 git rebase라는 것을 한번 써보겠습니다.

일단 premium branch를 merge하기 전으로 되돌려야 하는데요.

![image](https://user-images.githubusercontent.com/64893709/100519258-28149080-31da-11eb-8091-e59c26cc56e3.png)

그러면 premium branch를 merge하기 직전인 위의 commit으로 되돌리면 됩니다.

```q```를 통해서 나간 후 다음과 같이 커맨드를 입력합니다.

![image](https://user-images.githubusercontent.com/64893709/100519392-edf7be80-31da-11eb-9165-e82b614cdcab.png)

그리고 다시 commit history를 보면 

![image](https://user-images.githubusercontent.com/64893709/100519409-0a93f680-31db-11eb-8ee4-fad0d1ebabcb.png)

premium branch가 reset이 잘 되었다는 것을 알 수 있습니다.

이제 merge 말고 git rebase를 써보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/100519467-63638f00-31db-11eb-9fa8-bbc79cc93d5d.png)

여기서 rebase의 뜻은 무엇일까요? rebase는 '베이스를 다시 지정하다'라는 뜻인데요. commit을 재배치한다고 이해해주시면 됩니다.
그러니까 이 커맨드는 premium branch의 베이스를 test branch로 재지정한다는 뜻입니다.

실행을 했더니 위에서 CONFLICT가 발생하는 것을 확인할 수 있었습니다.   
( 생략 ) conclict가 났으니까 서브라임 텍스트에서 해결해보겠습니다.

rebase는 git commit을 하는 merge와 달리 git add .를 하고 다음과 같은 커맨드를 입력해야 합니다.

![image](https://user-images.githubusercontent.com/64893709/100519815-8b53f200-31dd-11eb-9756-f13e8c232817.png)

위 커맨드는 conflict가 발생해서 제대로 진햏되지 못한 rebase를 계속 진행하라는 뜻을 가지고 있습니다.   
그 결과 위에서 노란색으로 표시된 메시지가 출력되는데요. 무슨 일이 생긴 걸까요?

commit history를 다시 보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/100520290-63b25900-31e0-11eb-947a-f38a76de681e.png)

commit history를 보니까 merge할 때와 조금 다르게 생긴 것을 볼 수 있습니다.   
merge할 때처럼 새로운 commit이 생긴 것이 아닙니다.

마치 위에서 노란색으로 표시된 Add get_Median function commit이 원래 premium branch에서 했던 것처럼 보입니다.

그림으로 설명해보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/100520365-c9064a00-31e0-11eb-9ac5-114c15e3e62b.png)

제가 premium branch에서 get_Remainder 함수를 추가하고 test branch(B)에서 get_Median 함수를 추가하고 나면 위와 같은 상태가 됩니다.

그리고 이때 premium branch와 test branch를 merge하면

![image](https://user-images.githubusercontent.com/64893709/100520515-5ea1d980-31e1-11eb-8f02-fd7cfb11b131.png)

위처럼 새로운 merge commit이 생길겁니다.

하지만 만약 merge가 아니라 rebase를 하면 이렇게 됩니다.

![image](https://user-images.githubusercontent.com/64893709/100520560-b2142780-31e1-11eb-9e6d-73c95cc601b0.png)

premium branch가 Add get_Median function을 거쳐온 것처럼 commit history의 구조 자체가 바뀝니다.

rebase의 뜻 그대로 test branch가 가리키는 commit을 premium branch가 자신의 새로운 base로 만드는 것입니다.

![image](https://user-images.githubusercontent.com/64893709/100520554-a7f22900-31e1-11eb-94cc-78990c12f3a5.png)

![image](https://user-images.githubusercontent.com/64893709/100520566-bb9d8f80-31e1-11eb-8005-0c863f8134c5.png)

![image](https://user-images.githubusercontent.com/64893709/100520576-ceb05f80-31e1-11eb-8b32-02929b553902.png)

![image](https://user-images.githubusercontent.com/64893709/100520583-d96af480-31e1-11eb-986f-f154aa182a3b.png)
