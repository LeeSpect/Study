commit 히스토리를 보다 보면 commit A와 commit B간의 차이를 보고 싶을 때가 있습니다.   
그 사이에서 어떤 코드가 추가/삭제 되었는지 등을 알고 싶을 수 있습니다. 잠깐 commit 히스토리를 확인해보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97104083-5fcc7c00-16f4-11eb-8124-080b9692bdea.png)

위에서 노란색으로 표시된 git history는 git log --pretty=oneline 옵션을 git history로 aliasing해줬기 때문에 사용된 것입니다.

![image](https://user-images.githubusercontent.com/64893709/97104106-97d3bf00-16f4-11eb-8447-f5bf30a2d0d4.png)

그리고 노란색으로 표시된 Creat README commit과 초록색으로 표시된 README 수정 commit의 차이점을 알아보도록 하겠습니다.

이럴 때는 ```git diff```라고 입력하면 됩니다. diff는 차이점을 뜻하는 difference의 줄임말입니다.
그리고 이 뒤에 비교하고 싶은 commit 아이디 2개를 입력해주면 됩니다. 이전의 commit 아이디부터 입력합시다. commit 아이디는 처음 4글자로 줄여서 입력합니다.

![image](https://user-images.githubusercontent.com/64893709/97104202-52fc5800-16f5-11eb-85be-6a2f539a5686.png)

실행을 하게 되면 위처럼 두 commit 간의 차이가 보입니다.   
출력 결과를 자세히 보니까 git show 커맨드의 결과와 비슷해 보이네요. 그때와 똑같이 해석하시면 됩니다.
