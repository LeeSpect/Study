git reset을 할 때는 보통 아래와 같은 형식으로 쓰는데요.
```
git reset [옵션] [커밋 아이디]
```
그런데 이렇게 commit 아이디를 쓰려면 매번 commit 아이디를 찾아야한다는 불편함이 조금 있습니다. 사실 [커밋 아이디] 자리에 다른 걸 써줘도 되는데요.

예를 들어 아래와 같은 commit 히스토리가 있다고 합시다. 

![image](https://user-images.githubusercontent.com/64893709/97165072-77743500-17c6-11eb-9b45-59d8048eaa76.png)

지금 가장 오래된 첫 번째 commit부터 최신 commit인 여섯 번째 commit까지 번호를 붙인 상태입니다.(1 -> 2 -> 3 -> 4 -> 5 -> 6)

지금처럼 HEAD가 6번 커밋를 가리키는 상태에서,
만약 5번 commit으로 --hard 옵션과 함께 git reset하고 싶다면 이렇게 써야겠죠?
```
git reset --hard 7f3d
```
하지만 이렇게 쓰지 않고 이렇게 써도 됩니다.
```
git reset --hard HEAD^
```
HEAD^는 현재 HEAD가 가리키고 있는 commit의 바로 이전 커밋을 나타냅니다. 즉, 이 상황에서는 5번 commit을 나타내죠.

실제로 실행해보면 아래와 같이 HEAD가 이제 5번 commit을 가리키는 것을 알 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/97165343-e487ca80-17c6-11eb-8900-b9d7d4f8533c.png)

만약 '바로 이전'보다 좀더 이전에 있는 commit을 나타내고 싶다면 아래와 같이 쓰면됩니다.
```
git reset --hard HEAD~2
```
여기서 HEAD~2는 현재 HEAD가 가리키는 commit보다 2단계 전에 있는 commit을 나타냅니다.
지금 HEAD가 5번 commit을 가리키고 있죠?
이 상태에서 위 커맨드를 실행해보면 

![image](https://user-images.githubusercontent.com/64893709/97165467-126d0f00-17c7-11eb-8005-265371340151.png)

HEAD가 이제 3번 commit을 가리킵니다.

방금 본 표기처럼 HEAD~x는 현재 HEAD가 가리키는 commit보다 x단계 전에 있는 commit을 말합니다. 

앞으로 git reset을 할 때 commit 아이디를 써주기 귀찮다면,
* HEAD^
* HEAD~2

같은 것들을 쓰는 게 더 편합니다. 참고하세요.

HEAD가 현재 가리키는 커밋을 기준으로 한 상대적인 표현법인
