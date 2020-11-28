지금 저는 commit history를 볼 때마다 ```git history``` 커맨드를 이용해서 보고 있습니다.

그리고 이것은 ```git log --pretty=oneline``` 커맨드로 aliasing 된 상태입니다. 그래서 git history로 짧게 쳐줘도 같은 결과물이 나온다고 했습니다.

지금 저는 premium branch에 있는데요. 이 상태에서 commit history를 보면 현재 branch에 해당하는 commit들만 보입니다.

만약 현재 있는 branch 뿐만 아니라 다른 branch도 보려면 어떻게 해야할까요?

```--all```이라는 옵션을 붙여주면 되는데요.

![image](https://user-images.githubusercontent.com/64893709/100507206-a8260080-31b0-11eb-8789-087df9c8d9ba.png)

위처럼 git log --pretty=oneline에 뒤에 --all을 붙여주면 됩니다. 실행하면

![image](https://user-images.githubusercontent.com/64893709/100508001-e4f1f780-31b0-11eb-8314-18bafc7ca211.png)

master branch와 premium branch 모두 commit history가 잘 보입니다.   
그런데 지금 보기엔 뭔가 헷갈리는 부분이 있습니다.

![image](https://user-images.githubusercontent.com/64893709/100509133-40bc8080-31b1-11eb-872c-fb918a3ada88.png)

예를 들어서 노란색 박스로 표시된 두 commit은 master branch의 revert commit인데, commit들이 그냥 순서대로 정렬되어 있다 보니까 마치 premium branch의 revert commit인 것처럼 보이네요.

사실 premium branch의 revert commit은 위에서 초록색 박스로 표시된 두 개가 있는데 말입니다.

![image](https://user-images.githubusercontent.com/64893709/100509791-6fd2f200-31b1-11eb-8e92-f3e163ed3595.png)

git log에는 이런 문제를 해결해주는 '''--graph```라는 옵션이 있습니다.   
이 옵션을 쓰면 commit history가 각 branch와의 관계가 잘 드러나도록 그래프 형식으로 출력됩니다. 

![image](https://user-images.githubusercontent.com/64893709/100510420-9ee96380-31b1-11eb-94dd-ef6f9c037947.png)

위처럼 실행을 하면,

![image](https://user-images.githubusercontent.com/64893709/100511622-00113700-31b2-11eb-8a89-37cb77272ee9.png)

위처럼 화려한 선들이 보입니다. 위에서 노란색으로 표시된 ```*``` 표시 하나가 commit 하나입니다.

![image](https://user-images.githubusercontent.com/64893709/100513745-de647f80-31b2-11eb-9e70-3204920e03d8.png)

그리고 위에서 뭔가 갈라진 모습은 여러 branch로 코드 관리 흐름이 달라졌던 모습입니다.

graph 옵션을 쓰니까 commit과 branch의 관계가 입체적으로 잘 보이네요.

아까 조금 헷갈리게 보였던 revert commit들도 다시 찾아봅시다.

![image](https://user-images.githubusercontent.com/64893709/100513783-208dc100-31b3-11eb-9f33-17d493b3ef99.png)

초록색으로 표시된 premium branch의 revert commit 2개와 노란색 박스로 표시된 master branch의 revert commit 2개가 분리되어서 잘 보입니다.

![image](https://user-images.githubusercontent.com/64893709/100513810-47e48e00-31b3-11eb-89c7-e793fdc2ebb4.png)

위에서 노란색 박스로 표시된 것처럼 두 선이 합쳐지는 곳의 commit 메시지를 보면 전부 merge commit이라는 것을 알 수 있습니다.

이렇게 graph라는 옵션을 쓰면 commit과 branch의 관계를 그래프 형식으로 보여줍니다. 그리고 이런 식으로 commit history를 봐야 제대로 볼 수 있습니다.
