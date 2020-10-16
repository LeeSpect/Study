git add와 반대되는 명령어는 git reset입니다.

![1](https://user-images.githubusercontent.com/64893709/96249062-8fd69980-0fe7-11eb-99bc-d968a810d7e3.png)

git reset과 파일 이름을 입력하면 다음과 같은 메시지가 출력됩니다.

![2](https://user-images.githubusercontent.com/64893709/96249184-c57b8280-0fe7-11eb-84d6-74e55dc70208.png)

위에서 초록색으로 표시된 문장은 staging area에서 reset으로 인해 제거된 파일이 있다는 것을 의미하며, 노란색으로
표시된 문장은 제거된 파일의 이름을 나타내고 있습니다.

git status 명령어를 통해 현재 상태를 살펴보도록 하겠습니다.

![3](https://user-images.githubusercontent.com/64893709/96249433-23a86580-0fe8-11eb-8e0a-24bfd1390b54.png)

변경 사항이 있지만 staging area에 추가되지 않은 파일, calculator.py가 있다고 표시됩니다.   
staging area에서 제거되었다고 해도 calculator.py는 여전히 변경 사항이 적용된 모습 그대로 working directory에 남아있습니다. working directory는 현재 작업중인 프로젝트 디렉토리를 말합니다.

calculator.py 파일에서 변경됐던 사항을 다시 이전으로 돌린 후 git status 명령어를 입력하면 다음과 같이 출력됩니다.

![4](https://user-images.githubusercontent.com/64893709/96249791-b0532380-0fe8-11eb-8886-cc10742d2c1b.png)

초록색으로 표시된 부분과 같이 working tree가 깨끗하다고 표시되는데요. working tree는 working directory와 같은 말입니다.   
여기서 working directory가 깨끗하다는 말은 calculatory.py가 이전 commit에 있던 모습과 일치한다는 뜻입니다.   
즉 이전 commit 이후로 변경사항이 없다는 뜻입니다.

![5](https://user-images.githubusercontent.com/64893709/96250066-37080080-0fe9-11eb-8116-1ceaff40c978.png)
