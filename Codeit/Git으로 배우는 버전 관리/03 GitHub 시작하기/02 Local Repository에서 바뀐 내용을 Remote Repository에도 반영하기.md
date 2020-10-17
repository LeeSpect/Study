이전 영상에서는 local repository와 똑같은 repository를 GitHub에 만들었습니다. 그리고 이런 repository를 remote repository라고 한다고 배웠습니다.

다시 local repository를 수정해보겠습니다. (README.md 추가 설명 생략)

그리고 터미널로 가서 디렉토리의 상태를 살펴보겠습니다.

![1](https://user-images.githubusercontent.com/64893709/96328885-9c5c0000-1082-11eb-9eb8-32c9d8fa03d2.png)

위와 같이 README.md가 추가되어 있는 것을 볼 수 있습니다. 이제 이 상태로 commit을 해보겠습니다.

![2](https://user-images.githubusercontent.com/64893709/96328908-de854180-1082-11eb-9f6e-5ca5eaf1d9b3.png)

git add .과 git commit -m "Create README.md"를 통해 commit이 잘 이행되었음을 알 수 있습니다.

현 상태는 아래와 같이 local repository의 새로운 commit이 아직 remote repository에는 반영되지 않은 상태입니다.

![3](https://user-images.githubusercontent.com/64893709/96328919-112f3a00-1083-11eb-86af-f0dd4a7ebff7.png)

local repository의 새로운 commit을 remote repository에도 반영하고 싶을 때는 아래와 같이 git push라는 명령어를 사용합니다.

![4](https://user-images.githubusercontent.com/64893709/96328950-594e5c80-1083-11eb-8bac-92e146adc696.png)

다음과 같이 git push를 터미널에 입력하면 local repository의 새로은 commit이 remote repository에도 반영됩니다.

![5](https://user-images.githubusercontent.com/64893709/96328973-a6323300-1083-11eb-8e2b-c6aff286ee87.png)

![6](https://user-images.githubusercontent.com/64893709/96329010-df6aa300-1083-11eb-99d4-ade7c38dc62b.png)
