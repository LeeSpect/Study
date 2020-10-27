저는 지금 branch를 총 2개 가지고 있습니다.   
무료 버전을 위한 master branch와 유료 버전을 위한 premium branch가 있습니다.   
앞으로 무료 버전에 대한 작업은 master branch로 checkout해서 작업하고 유료 버전에 대해 작업할 때는 premium branch로 checkout해서 작업하겠습니다.

지금 branch를 확인해보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97301041-9d6b0980-189a-11eb-8cf2-60fc6debb213.png)

저는 지금 master branch에 있는데요. 지금부터 할 작업은 무료 버전에 대한 것이어야겠죠?

일단 서브라임 텍스트로 이동해서 calculator.py 파일을 열어볼게요. 나눗셈을 구하는 divide 함수 추가..(생략)

그 다음에 git add .를 하고 commit을 해줄게요.

![image](https://user-images.githubusercontent.com/64893709/97307841-8c72c600-18a3-11eb-8c17-77590350aeff.png)

그런데 이쯤에서 회사에서 무료 버전에 있는 기능은 유료 버전에도 다 있어야 한다고 했다는 소식을 듣게 되었습니다.   
그러니까 방금 추가한 divide 함수는 무료 버전뿐만 아니라 유료 버전에도 추가되어야 한다는 겁니다.   
이런 경우에는 제가 premium branch로 가서 직접 divide 함수를 추가하고 commit하면 되겠죠?   
하지만 Git에서는 어떤 branch에서 한 commit을 그대로 다른 branch에 반영하는 것이 가능합니다.

일단 premium branch로 가서 calculator.py의 내용을 보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97308393-2aff2700-18a4-11eb-89e7-b58d74cd3acf.png)

아직 divide 함수가 없네요. 우리는 master branch에서 divide 함수를 추가했기 때문에 premium branch에서는 divide 함수가 없는 것이 당연합니다.

하지만 방금 master branch에서 했던 commit을 그대로 가져와서 합칠 수 있는 방법이 있는데요. 이런 작업을 __branch merge__ 라고 합니다.

![image](https://user-images.githubusercontent.com/64893709/97308720-85988300-18a4-11eb-8243-c63057dd7a4b.png)

한번 해보겠습니다. ```git merge master```을 하면 되는데요. 이것을 해석하면 다음과 같습니다.

![image](https://user-images.githubusercontent.com/64893709/97308870-afea4080-18a4-11eb-8c82-1779db6055e0.png)

실행을 하게 되면,

![image](https://user-images.githubusercontent.com/64893709/97309115-f770cc80-18a4-11eb-95cf-9d1d03959fb7.png)

이렇게 뜹니다. merge를 하면 merge commit이라는 새로은 commit이 생기는데요. 그래서 이런 commit 메시지를 입력하는 창이 뜹니다.   
여기서는 위에서 노란색으로 표시된 commit 메시지를 그대로 저장하겠습니다. 저장은 ```:wq```를 입력하고 Enter를 누르면 됩니다.

![image](https://user-images.githubusercontent.com/64893709/97309341-39017780-18a5-11eb-8745-ce8601cdf846.png)

Enter를 치고 나면 이렇게 Merge가 되었다는 문장이 출력됩니다.

그리고 calculator.py 파일을 보면,

![image](https://user-images.githubusercontent.com/64893709/97309421-58000980-18a5-11eb-8367-49fede3eb113.png)

divide 함수가 잘 추가되어 있는 것을 볼 수 있습니다.
