### 1. 이전 수업의 내용(git reset) 복습
이전 수업에서는 아래 그림과 같은 상태에서

![image](https://user-images.githubusercontent.com/64893709/98689264-16945180-23af-11eb-8015-a0005fe678d3.png)

```
git reset 9033
```
를 실행하면

![image](https://user-images.githubusercontent.com/64893709/98689322-26139a80-23af-11eb-965c-4daef6ba7e84.png)

이 그림과 같은 결과가 된다고 했습니다. 이렇게 HEAD는 __보통__ 본인이 직접 commit을 가리키는 게 아니라 branch를 통해서 간접적으로 commit을 가리킵니다.

## 2. git checkout이 하는 일
하지만 HEAD 자체가 가리키던 것을 바꿀 수도 있습니다. 사실 HEAD가 아예 commit을 직접적으로 가리키게 하는 것도 가능한데요.

바로 __git checkout__ 커맨드를 쓰면 됩니다.

![image](https://user-images.githubusercontent.com/64893709/98926883-347ec500-251b-11eb-8c02-e2ed64a54577.png)

원래 이 상태에서
```
git checkout 9033
```
를 실행하면 아래 그림처럼 바뀝니다.

![image](https://user-images.githubusercontent.com/64893709/98926944-48c2c200-251b-11eb-9891-9c92d1a88096.png)

이 그림을 자세히 보세요. 이제 HEAD가 master branch를 가리키는 게 아니라 본인이 직접 __9033.. commit__ 을 가리키고 있죠?

이렇게 branch를 통해서 commit을 가리키는 게 아니라 본인이 직접 commit을 가리키고 있는 상태의 HEAD를 특별히 가리키는 말이 있습니다.

바로 __Detached HEAD__ 입니다. Detached는 우리말로 ‘~로부터 떨어진, 분리된’이라는 뜻을 갖는데요. branch로부터 떨어진 상태이기 때문에 이렇게 부르는 겁니다. 

이렇게 HEAD가 특정 commit을 직접 가리키게 하는 이유는 여러가지가 있을 수 있는데요.

그 중에서 주된 이유 한 가지는 바로 과거의 특정 commit에서 새로운 branch를 만들고 싶을 때입니다. 

예를 들어 지금 위의 그림과 같이 Detached HEAD인 상태에서
```
git branch premium
```
으로 premium branch를 새로 만들면 아래 그림과 같은 결과가 됩니다.

![image](https://user-images.githubusercontent.com/64893709/98927377-ce467200-251b-11eb-9271-df6a3e965b83.png)

1. 지금 premium이라는 branch가 새로 생성되었고
2. premium branch는 HEAD가 가리키던 commit을 똑같이 가리키게 됩니다.

자, 그리고 여기서 새로운 사실을 하나 알려드릴게요.

git checkout 커맨드로는 
* HEAD가 commit을 직접적으로 가리키게 할 수도 있을 뿐만 아니라
* branch를 직접 가리키게 만들 수도 있습니다.

HEAD가 branch를 가리키도록 해볼게요. 이렇게 쓰면
```
git checkout premium
```
HEAD가 premium 브랜치를 가리키게 됩니다.

그러니까 아래 그림과 같이 이제 HEAD가 premium branch를 가리키게 되는 겁니다. 그리고 이것은 곧 Detached HEAD 상태에서 벗어나 HEAD가 branch를 가리키는 정상적인 상태로 돌아오는 거죠.

![image](https://user-images.githubusercontent.com/64893709/98932243-6d6e6800-2522-11eb-977c-71c5adea6ad1.png)

그리고 이렇게 HEAD가 premium branch를 가리키는 상태일 때 새 commit을 하면

![image](https://user-images.githubusercontent.com/64893709/98932357-955dcb80-2522-11eb-9e1f-427dd6611d8f.png)

이제 premium branch로 master branch와 다른 새로운 코드 관리 흐름을 가져갈 수 있게 되는 겁니다.

방금 한 것처럼 특정 commit을 시작점으로 하는 새로운 branch를 만들고 싶을 때 HEAD를 잠시 Detached HEAD 상태로 두는 경우가 많습니다.

이 내용을 정리하면

* git checkout 커맨드로는 HEAD가 직접적으로 가리키는 것을 바꿀 수 있고
* git checkout 뒤에는 commit 아이디 또는 branch의 이름을 줘서
* HEAD가 직접 commit을 가리키거나, branch를 가리키도록 할 수 있다는 뜻입니다.

그런데 사실 git checkout 뒤에 branch의 이름이 오는 경우는 이미 우리가 배웠습니다. 우리가 어떤 branch로 가고 싶을 때
```
git checkout [가고 싶은 branch 이름]
```
형식의 커맨드를 쓴다고 배웠죠?

이제 이 커맨드가 좀 새로운 시각에서 느껴지지 않나요? 자, 그림으로 바로 보여드릴게요.

지금 위 그림과 같은 상태에서
```
git checkout master
```
를 실행하면

![image](https://user-images.githubusercontent.com/64893709/98933023-7ad82200-2523-11eb-84cc-97b40a996412.png)

이렇게 HEAD가 master branch를 가리키게 됩니다. 바로 이게 우리가 이전에 git checkout 커맨드를 사용해서 다른 브랜치로 이동할 때 벌어지는 일이었던 겁니다.

이렇게
* HEAD가 다른 branch가 가리키던 commit을 가리키게 되면
* 그에 맞게 working directory 내부도 바뀌게 되고,
* 그 결과 우리는 branch가 변경되었다는 걸 실감할 수 있었던 겁니다.

이해하기 쉽게 다시 한번 풀어서 말하자면
```
git checkout master
```
이 커맨드의 뜻은 다음과 같이 해석됩니다.

= master branch로 이동하라

= HEAD가 master branch를 가리키도록 하라

= HEAD가 master branch가 가리키던 commit을 간접적으로 가리키게 됨으로써

= working directory의 내부도 그 commit에 맞게 변함으로써

= master branch로 이동한 것을 사용자는 실감하게 됨

이렇게 되는 거죠.

자, git checkout의 비밀을 이제 알겠죠?

## 3. git reset vs git checkout
마지막으로 git reset과 git checkout의 차이점을 짚고 넘어갈게요.

둘의 차이점은 아래 표와 같습니다.

![image](https://user-images.githubusercontent.com/64893709/98934842-018dfe80-2526-11eb-86d1-3bcdba5ea3cf.png)
