이번에는 브랜치(branch)에 대해 좀더 많은 것들을 배워보겠습니다.

여러분, 혹시 [GitHub 시작하기 챕터의 'Local Repository의 내용을 Remote Repository로 보내기'](https://github.com/LeeSpect/Study/blob/main/Codeit/Git%EC%9C%BC%EB%A1%9C%20%EB%B0%B0%EC%9A%B0%EB%8A%94%20%EB%B2%84%EC%A0%84%20%EA%B4%80%EB%A6%AC/03%20GitHub%20%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0/01%20Local%20Repository%EC%9D%98%20%EB%82%B4%EC%9A%A9%EC%9D%84%20Remote%20Repository%EB%A1%9C%20%EB%B3%B4%EB%82%B4%EA%B8%B0.md)
에서 했던 작업, 기억나시나요?

저는 그때

1. GitHub에서 Math_Box라는 remote repository를 만들고
2. local repository의 내용을 그 remote repository에 보내기 위해 아래와 같은 커맨드 2개를 실행한 적이 있습니다.

```
git remote add origin https://github.com/kyuri-dev/Math_Box.git
```
```
git push -u origin master 
```
그때는 이 2개의 커맨드를 그냥 복사-붙여넣기해서 실행만 하고 정확한 의미에 대해서 설명하지 않았는데요. 이번 노트에서는 그 의미를 알아보겠습니다.

## 1. origin이란?

먼저 첫 번째 커맨드를 봅시다. 
```
git remote add origin https://github.com/kyuri-dev/Math_Box.git
```
이 커맨드에서 __remote__ 는 remote repository에 관한 작업을 할 때 쓰는 커맨드입니다. 

그리고 그 뒤의 __add__ 는 새로운 remote repository를 등록하겠다는 뜻입니다. 

그 다음에는 __origin https://github.com/kyuri-dev/Math_Box.git__ 이라고 써있죠?

이 표현은 __https://github.com/kyuri-dev/Math_Box.git__ remote repository를

__origin__ 이라는 이름으로 등록하겠다는 뜻입니다.

그러니까 이 커맨드를 실행하고 나면 __https://github.com/kyuri-dev/Math_Box.git__ 를 __origin__ 으로 간단하게 나타낼 수 있게 되는 거죠.

그럼 왜 하필 __origin__ 이라고 하는 걸까요? origin이 아닌 여러분이 원하는 다른 단어를 입력해도 큰 상관은 없습니다.
하지만 Git에서는 remote repository를 최초로 추가할 때 origin이라는 이름으로 가리키는 것이 관례화되어 있습니다.

origin은 ‘근원’, ‘기원’이라는 뜻을 가집니다.
아마도 다른 사람의 remote repository를 자신의 컴퓨터로 가져와서 작업을 하는 사람의 입장에서는
remote repository가 프로젝트의 근원이 되는 존재이기 때문에 그런 관습이 생긴 것으로 추측됩니다. 

사실
```
git remote add hello https://github.com/kyuri-dev/Math_Box.git
```
처럼 origin 대신 우리가 원하는 단어(hello)를 써도 상관은 없지만, 되도록 관례에 따라 origin을 써주는 게 좋겠죠?

## 2. Remote Repository에 있는 branch

이제 두 번째 커맨드를 설명해드릴게요.
```
git push -u origin master
```
이 커맨드의 뜻은
* 현재 local repository에 있는 master branch의 내용(=master branch와 관계된 모든 commit들)을
* origin이라는 remote repository로 보낸다는 뜻입니다.

이때 같은 이름의 branch로 전송하게 되는데 만약 origin이라는 remote repository에 master 브랜치가 __없으면 master 브랜치를 새로 생성하고 푸시합니다.__ 

그런데 여기서 옵션 __-u__ 는 무슨 뜻일까요? -u는 __--set-upstream__ 이라는 옵션의 약자입니다. 

이렇게 __--set-upstream(-u) 옵션__ 을 주면
* local repository에 있는 master branch가
* origin에 있는 master branch를 tracking(추적)하는 걸로 설정됩니다.

tracking이라는 건 local repository의 한 branch가 remote repository의 한 branch와 연결되어
그것을 계속 바라보는 상태가 되는 것이라고 생각하시면 됩니다.
이렇게 맺어진 연결 상태를 tracking connection이라고 합니다. 

만약
* local repository에 A라는 branch가 있고,
* remote repository에 B라는 branch가 있을 때
* 이런 __Tracking connection__ 이 서로 맺어진 경우,
* B branch를 A branch의 __upstram branch__ 라고 합니다.
* 지금은 구별하기 위해서 A와 B라고 표현했지만 보통은 같은 이름인 경우가 대부분입니다.

이렇게 __tracking connection__ 이 한번 설정되고 나면,

사용자가 현재 master branch에 위치해있을 때,
```
git push
```
라고만 써도 자동으로 remote repository의 master branch를 대상으로 git push가 동작하고,
```
git pull
```
라고만 써도 remote repository의 master branch를 대상으로 git pull이 동작합니다. 

사실 __--set-upstream(-u)__ 옵션을 주지 않아도 그 후에 git push와 git pull을 할 수 있기는 합니다.
하지만 맨 처음에 이 옵션을 주지 않으면 tracking connection이 없기 때문에 나중에 git push를 하고 싶을 때
```
git push origin master:master
```
이런 식으로 적어줘야 합니다. 여기서
* origin은 remote repository를 나타내고,
* master:master에서 더 먼저 나오는 master는 local repository의 master branch(~에서)/더 뒤에 나오는 master는 remote repository의 master branch(~으로)를 나타냅니다.

그러니까 tracking connection이 없으면 매번 이런 식으로 git push를 해줘야 합니다.
git pull도 마찬가지로 이런 식의 복잡한 표현이 필요하게 됩니다.

그러니까 그냥 처음부터 tracking connection을 설정하고 그 이후부터는 git push, git pull이라고만 써서 편하게 푸시와 풀을 하는 게 좋겠죠?
이게 바로 제가 맨 처음에 local repository의 내용을 remote repository로 보낼 때 -u라는 옵션을 썼던 이유입니다.

## 3. origin/master의 의미

자, 이제
* local repository의 master branch
* remote repository의 master branch

이렇게 같은 이름이지만, 서로 다른 2개의 branch가 있다는 걸 알겠죠? 

그럼 remote repository에 있는 master branch는 어떻게 볼 수 있을까요? GitHub 페이지에서 보면 될 겁니다.

하지만 제 컴퓨터에서도 확인할 수 있는 방법이 있습니다. 잠깐 commit history를 살펴보면

![image](https://user-images.githubusercontent.com/64893709/97329968-fb0f4e00-18ba-11eb-9992-30b2b7ad9cdd.png)

위 그림에서
* __master__ 가 local repository의 master branch를 나타내고
* __origin/master__ 가 remote repository의 master branch를 나타냅니다.

이때까지 local repository의 master branch에서 여러 commit을 했지만 그러고나서 git push를 해준 적은 없었습니다.
그래서 위 그림처럼 origin/master가 master보다 이전의 commit을 가리키고 있는 겁니다.

다음 영상에서는 master, premium 브랜치 둘 다에서 리모트 레포지토리로 git push 하겠습니다. 그러고 나면 이제 origin/master도 master와 같은 커밋을 가리키게 될 것입니다.
