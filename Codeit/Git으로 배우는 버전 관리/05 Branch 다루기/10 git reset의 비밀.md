이전 수업에서는
* 사실 branch는 commit을 가리키는 포인터이고,
* HEAD는 이런 branch를 통해 commit을 간접적으로 가리키는 포인터

라고 배웠습니다.

자, 이제 이 사실을 안다면 우리가 이전에 배운
```
git reset
```
커맨드의 동작 원리를 더욱 정확하게 알 수 있는데요.

### 1. git reset을 할 때 HEAD의 변화는?
지금 총 4개의 commit을 한 아래와 같은 상황이라고 가정합시다.

![image](https://user-images.githubusercontent.com/64893709/98686305-bea81b80-23ab-11eb-962c-33977c5dc712.png)

현재 각 박스 안에 있는 텍스트는 각 commit의 commit 아이디 앞 부분입니다.

이 상태에서
```
git reset [--hard 또는 --soft 또는 --mixed] 9033
```
을 실행한다면 어떻게 될까요?
이전에 git reset을 배울 때를 떠올려보면 HEAD가 9033.. commit을 가리키게 되겠죠?
그럼 정확히 어떤 모습으로 가리키게 되는 건지 보여드리겠습니다.
어떤 옵션을 쓰든 아래 그림과 같은 결과가 됩니다.

![image](https://user-images.githubusercontent.com/64893709/98686701-36764600-23ac-11eb-82d7-be75fa7fb8a2.png)

지금 HEAD는 여전히 master branch를 가리킵니다. 대신 master branch가 가리키던 commit이 바뀌었네요. 그래서 결과적으로 HEAD가 9033.. commit을 가리키게 된 겁니다.

방금 발생한 일을 정리하면 다음과 같습니다. git reset 커맨드를 사용하면

1. HEAD는 여전히 같은 branch를 가리키고,
2. HEAD가 가리키는 branch가 다른 특정 commit을 가리키게 됩니다.
3. 이 때문에 결국 HEAD가 간접적으로 가리키던 commit도 바뀌게 되는 겁니다.

git reset을 했을 때 HEAD가 가리키던 commit이 바뀐다는 말이 정확히 무슨 뜻인지, 이제 아시겠죠? 바로 이런 원리가 있었던 겁니다. 그리고 이전에 배운대로 각 옵션(--soft/--mixed/--hard)에 따라 과거의 commit처럼 working directory나 staging area도 리셋되는지가 결정되는 거구요.

하지만 한 가지 더 알아야할 git reset의 비밀이 있는데요.

### 2. git reset을 한다고 그 이후의 commit이 사라지는 건 아닙니다.
git reset을 한다고 하면 그 이후의 commit이 삭제되는 것으로 착각하기 쉽습니다. 그러니까 위 상황에서 네 번째 commit인 43kf.. commit이 사라진다고 오해하실 수도 있는데요. 전혀 그렇지 않습니다. 43kf.. commit은 계속 남아있습니다.

그리고 git reset은 꼭 과거의 commit으로만 할 수 있는 것도 아닙니다. 현재 HEAD가 가리키고 있는 commit 이후의 commit으로도 리셋할 수 있죠.

* 지금처럼 HEAD가 3번째 commit인 9033.. commit을 가리키고 있는 상태에서
```
git reset 43kf
```
를 실행하면 master branch가 다시 43kf.. commit을 가리키게 됩니다. 아래 그림처럼요.

![image](https://user-images.githubusercontent.com/64893709/98688893-b00f3380-23ae-11eb-993a-98fcf86cb12b.png)

그러니까 git reset에 관해서 분명하게 아셔야할 게

1. 과거의 commit을 git reset을 한다고 그 이후의 commit들이 삭제되는 게 절대 아닙니다. 계속 남아있습니다.
2. git reset은 과거의 commit뿐만 아니라 현재 HEAD가 가리키는 commit 이후의 commit으로도 할 수 있습니다.

이 사실을 확실히 알고 나면 앞으로 git reset을 사용해서 commit 사이를 자유자재로 이동할 수 있을 겁니다.
