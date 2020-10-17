Local Repository의 최신 내용을 Remote Repository에도 반영하려면
```
git push
```
를 해야한다고 배웠습니다. 그런데 여기서 잠깐 궁금한 점이 있습니다.

그렇다면 아무나 git push라고만 쓰면 자신이 작업한 내용을 저의 remote repository에 반영할 수 있은 걸까요?

##### 그건 아닙니다.

이게 만약 가능하다면 저도 모르는 사이에 제 remote repository의 내용이 맘대로 바뀌어 버릴 수도 있겠죠?   
사실 git push는 remote repository의 주인, 그러니까 본인만 할 수 있습니다. 만약 본인이 아닌 다른 사용자도 git push를 할 수 있게 하려면
GitHub에서 추가 작업을 해줘야 합니다.

일단 GitHub 페이지에서 저(codeitTeacher)의 remote repository인 MathBox의 설정을 살펴보겠습니다.

상단의 여러 탭 중에서 settings 탭을 클릭하세요. 그 다음 화면 왼쪽의 Manage access 탭을 클릭하면 되는데요.

![1](https://user-images.githubusercontent.com/64893709/96339355-3d70a800-10cf-11eb-8786-1b37702cabbc.png)

화면에 PUBLIC REPOSITORY라는 표현이 보이죠? 이 말은 지금 누구나 제 repote repository의 주소만 알면, 그 내용을
살펴볼 수 있다는 뜻입니다. 그리고 누구든지 제 repository를 자기 컴퓨터로 가져갈 수도 있다는 뜻입니다.
그리고 자기 컴퓨터에서 추가 작업을 할 수도 있습니다. 하지만 그래도 본인이 아닌 이상 그 내용을 git push할 수 없기 때문에
remote repository에 반영할 수는 없습니다.

그럼 저 말고 이제 다른 사용자도 git push할 수 있도록설정을 조금 바꿔볼게요. 아래 그림을 보세요.

![2](https://user-images.githubusercontent.com/64893709/96339423-8e809c00-10cf-11eb-9b70-08b49219d95b.png)

화면 하단에서 Invite a collaborator 버튼이 보이시나요? collaborator를 초대한다는 뜻인데요. 다른 사용자를 colla
borator로 초대하면 그 사용자는 제 remote repository에 git push할 수 있는 권한을 가질 수 있습니다. 버튼을 클릭해볼게요.

![3](https://user-images.githubusercontent.com/64893709/96339454-bec83a80-10cf-11eb-8081-169d0f8eec01.png)

그 다음 뜨는 창에서 위 그림과 같이 GitHub의 codeitDeveloper라고 하는 사용자를 검색해서 클릭할게요.
(codeitDeveloper는 제가 따로 준비해둔 다른 사용자 계정입니다.)

![4](https://user-images.githubusercontent.com/64893709/96339481-ee774280-10cf-11eb-9c25-5df840a59587.png)

그리고 codeitDeveloper에게 "내 repository의 collaborator가 되어달라"라는 초대장을 보낼게요.

그럼 이제 codeitDeveloper에 대해서 Pending invite 상태가 됩니다.

![5](https://user-images.githubusercontent.com/64893709/96339505-25e5ef00-10d0-11eb-8d0f-21a760d2969c.png)

그럼 이제 codeitDeveloper는 아래와 같은 초대장을 받게 됩니다.

![6](https://user-images.githubusercontent.com/64893709/96339517-4150fa00-10d0-11eb-813d-c209d2b20afa.png)

여기서 View invitation 버튼을 클릭해서 초대장을 살펴보면

![7](https://user-images.githubusercontent.com/64893709/96339610-cd632180-10d0-11eb-9195-71df73b89206.png)

그럼 이렇게 저 codeitTeacher가 codeitDeveloper를 초대한 내용을 확인할 수 있습니다. codeitDeveloper가 Accept invitation 버튼을 클릭하면 이제
```
codeitDeveloper는 codeitTeacher가 소유한 MathBox 레포지토리의 collaborator가 됩니다. 
```
![8](https://user-images.githubusercontent.com/64893709/96339646-ff748380-10d0-11eb-913f-a5a15e4edcb6.png)

그리고 다시 원래 codeitTeacher 계정에서 확인해보면 codeitDeveloper가 정말 collaborator가 된 것을 확인할 수 있는데요. 이제 codeitDeveloper는 MathBox 레포지토리를 자신의 컴퓨터로 가져가서 수정한 후 git push를 해서 저의 리모트 레포지토리를 수정할 수 있습니다. 

자, 정리해볼게요.

1. 원칙적으로 자신의 리모트 레포지토리에는 자신만 git push를 할 수 있습니다. 
2. 만약 다른 사용자도 git push를 할 수 있게 해주려면 그 사용자를 해당 리모트 레포지토리의 collaborator로 지정하면 됩니다. 
