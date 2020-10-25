지금까지 영상에서 계속 commit 히스토리를 보기 위해
```
git log
```
커맨드를 사용해왔습니다.

그리고 commit 하나당 한 줄씩 보기 위해
```
--pretty=oneline
```
이라는 옵션을 붙여서 사용하고 있죠.

그런에 옵션이 좀 길죠? 이렇게 긴 옵션을 매번 붙여서 사용하는 건 좀 힘들 것 같은데요.

Git에는 이렇게 길이가 긴 경우의 커맨드 전체에 별명을 붙여서 그 별명을 사용할 수 있도록 해주는 기능이 있습니다.

이 때 붙이는 별명을 alias라고 하고, 별명을 붙이는 행위를 aliasing이라고 합니다.

그럼 한번 aliasing을 해보겠습니다.
* git log --pretty=oneline을
* git history라는 별명으로

aliasing해보겠습니다. 어떻게 하면 될까요?

혹시 예전에 Git으로 가장 첫 번째 commit을 하기 전에 이런 설정을 했던 거 기억나시나요?
```
git config user.name 'codeit'
git config user.email 'codeit@codeit.kr'
```
누가 commit을 남기는지 그 사용자 정보를 저장하기 위해 했던 설정으로 사용자의 아이디와 이메일 주소를 설정하는 커맨드였습니다.

aliasing을 할 때도 이렇게
```
git config
```
커맨드를 사용하면 되는데요. 이렇게 적으면 됩니다.
```
git config alias.history 'log --pretty=oneline'
```
이렇게 쓰고 실행하고 나면 앞으로 git history라고만 써도 자동으로 git log --pretty=oneline을 실하게 됩니다.

다음 영상부터는 git log --pretty=oneline 대신 git history를 사용하도록 하겠습니다. history는 원래 git에 있는 커맨드가 아니라
단지 제가 만든 alias라는 것을 기억세요.

그리고 앞으로 여러분도 여러 커맨드와 옵션들을 배울 때 길이가 너무 길어서 짧게 나타내고 싶은 것이 생기면 방금 배운 aliasing을 활용해보세요.
