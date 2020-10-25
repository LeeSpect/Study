커밋을 하고 나면 가끔씩 아쉬울 때가 있습니다.
'코드를 더 추가하고 commit할 걸', 'commit 메시지를 더 이해하기 쉽게 쓸 걸' 같은 후회가 생길 수도 있습니다
어떤 경우에는 잘못된 코드를 그대로 두고 commit을 하게 될 수도 있습니다. 물론 이 경우에는 잘못된 코드를 고치고 다시 commit을 해주면 됩니다.
하지만 그렇게 되면 굳이 없어도 되는 commit이 생기는 거겠죠?

그래서 Git은 자신이 했던 commit 중에서 최신 commit을 다시 수정할 수 있는 기능을 가지고 있습니다. 

우선 commit 히스토리를 살펴보기 위해 git log --pretty=oneline을 이용하겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97102764-93ef6f00-16eb-11eb-94b9-68322bde5752.png)

그러면 위처럼 지금까지 했던 6개의 commit이 나옵니다. 이 6개의 commit 중에서 노란색으로 표시된 최신 commit을 수정해보겠습니다.

우선 코드를 수정합니다.(생략)   
그리고 git add .와 git commit까지는 이전 commit 과정과 동일하게 진행하지만 최신의 commit을 수정하는 경우에는 아래와 같이 --amend를 입력합니다.

![image](https://user-images.githubusercontent.com/64893709/97102800-cbf6b200-16eb-11eb-96bd-0aed1850d359.png)

위와 같이 실행을 하면 commit 메시지를 적을 수 있는 창이 하나 뜹니다.

![image](https://user-images.githubusercontent.com/64893709/97102854-37408400-16ec-11eb-92e9-419fb0de45af.png)

위와 같이 노란색으로 표시된 맨 위에는 원래 commit 할 때 적었던 commit 메시지가 적혀져 있습니다. 

여기서 commit 메시지도 수정을 하고 싶다면, 키보드의 ```i```를 눌러서 INSERT 모드로 들어간 후 아래와 같이 상단의 텍스트에서 수정할 단어를 'multiply'로  
바꿔줍니다. 그리고 ```ESC```를 눌러 입력 모드에서 빠져나오고 ```:wq```를 입력해 저장합니다.

![image](https://user-images.githubusercontent.com/64893709/97102933-d49bb800-16ec-11eb-9e86-b1506477fdf8.png)

그러면 위와 같이 commit이 잘 되었다는 내용이 출력되고, commit 히스토리에서도 여전히 6개의 commit이 출력됨을 알 수 있습니다.   
기존 commit 히스토리와의 차이점은 수정한 최신 commit의 아이디가 바뀌었다는 점입니다.
