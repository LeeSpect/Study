remote repository의 commit 내용이 local repository보다 최신의 버전이라면 remote repository의 commit을 local repository에 반영해야 할 필요가 있을 수 있습니다.

이럴 때는 다음과 같이 git pull 명령어를 사용하면 됩니다.

![1](https://user-images.githubusercontent.com/64893709/96329079-86e7d580-1084-11eb-9546-4b25b15939d2.png)

git pull을 입력하면 아래처럼 출력됩니다.

![2](https://user-images.githubusercontent.com/64893709/96329086-9d8e2c80-1084-11eb-913e-4360bc4dfd01.png)

이전에 remote repository에서 수정했던 README.md의 내용을 출력해보겠습니다. 출력은 ```cat```이라는 명령어를 사용합니다.

![3](https://user-images.githubusercontent.com/64893709/96329109-d4fcd900-1084-11eb-897a-1eec9bac5c4d.png)

초록색으로 표시된 수정 사항이 잘 반영된 모습을 볼 수 있습니다.

### remote repository를 왜 쓰는가?   
local repository와 똑같은 내용의 remote repository를 만드는 이유에는 크게 2가지가 있습니다. 

첫 번째 이유는 ```안전성```입니다. 예를 들어 내 컴퓨터를 잃어버리거나 내 컴퓨터에 문제가 생겨서 local repository가 사라졌다고 생각해봅시다.
딱히 복원할 방법이 없습니다. 하지만 remote repository가 있다면 다른 컴퓨터에서 이 remote repository의 내용을 가져오기만 하면 됩니다.

두 번째 이유는 다른 개발자들과 ```협업 가능```입니다. git push 커맨드와 git pull 커맨드를 생각해봅시다. 각 개발자들은
하나의 remote repository에 git push와 git pull을 사용하면서 새로운 commit을 추가하고 수정하는 등의 협업을 할 수 있습니다.

![1](https://user-images.githubusercontent.com/64893709/96329247-ee525500-1085-11eb-80c1-5d29c7eb1196.png)
