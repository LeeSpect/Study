이전 수업에서 다뤘던 calculator.py, License 파일을 모두 수정한 후 calculator.py 파일만 add해보겠습니다.   
그리고 git status 명령어를 입력하면 깃이 인식하고 있는 프로젝트 디렉토리의 현재 상태가 출력됩니다.

![1](https://user-images.githubusercontent.com/64893709/96225813-9dcaf100-0fcc-11eb-86f2-86bf714d661d.png)

출력은 두 가지로 나누어 볼 수 있습니다.

![2](https://user-images.githubusercontent.com/64893709/96226290-6577e280-0fcd-11eb-9af4-3fc610f9cda8.png)

Changes not staged for commit:으로 시작하는 2번째 부분에서 stage는 git add로 파일을 staging area에 추가하는 것을 뜻합니다.   
즉 calculator.py는 수정이 반영된 상태로, License는 수정이 반영되기 이전 모습으로 commit에 반영되게 됩니다.
commit을 하기 전에 git status를 통해 commit하고 싶은 파일들이 모두 staging area에 존재하는지 확인하는 것이 좋습니다.

이번에는 파일 말고 디렉토리를 하나 추가해보겠습니다. calculator 파일의 코드에 관한 회의 내용을 담을 디렉토리를 만들겠습니다.
mkdir meeting-log를 통해 디렉토리를 추가한 후 그 디렉토리로 이동하겠습니다.

![3](https://user-images.githubusercontent.com/64893709/96228081-09fb2400-0fd0-11eb-8646-9c4709759406.png)

day1이라는 파일과 day2라는 파일을 만들겠습니다.   
그리고 다시 부모 디렉토리로 돌아가겠습니다.   
그리고 staging area에 이전에 만들었던 meeting-log 디렉토리를 추가하겠습니다. 그리고 git status를 입력하면 다음과 같이 출력됩니다.

![4](https://user-images.githubusercontent.com/64893709/96228357-7413c900-0fd0-11eb-8623-c674a33f08be.png)

디렉토리를 추가하면 그 안에 들어있는 파일도 함께 staging area에 추가되는 것을 볼 수 있습니다.

변경 사항이 있는 파일들을 일일이 git add를 입력할 필요 없이 한 번에 staging area에 추가할 수 있는 방법이 있습니다.

![5](https://user-images.githubusercontent.com/64893709/96228831-0e740c80-0fd1-11eb-9699-2a52dfbc0ef9.png)

위처럼 add 뒤에 .을 추가하면 됩니다. 이제 commit을 해보겠습니다.

![6](https://user-images.githubusercontent.com/64893709/96229018-53983e80-0fd1-11eb-8e00-d7a32600a307.png)

commit이 모두 정상적으로 처리되었음을 알 수 있습니다.

