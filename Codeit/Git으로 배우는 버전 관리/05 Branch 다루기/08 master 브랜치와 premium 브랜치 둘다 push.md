이전 수업에서 remote repository의 master branch가 local repository의 master branch보다 항상 이전 commit에
머물러 있는 것을 확인했습니다.

다시 한번 commit history를 확인해보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97585004-fc1bb900-1a3b-11eb-86ca-282ee4ecd0eb.png)

그러면 위에서 노란색으로 표시된 local repository의 master branch보다 초록색으로 표시된 remote repository의
master branch가 더 이전에 있는 것을 알 수 있습니다.

local repository의 master branch에서 git push를 해봅시다.

일단 master branch로 이동하겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97585129-24a3b300-1a3c-11eb-883f-0ffe495ac670.png)

여기서 git push를 하겠습니다. 그러면 지금까지 local repository의 master branch에서 했던 commit들이
remote repository의 master branch로 올라가겠죠?   
실행을 하면,

![image](https://user-images.githubusercontent.com/64893709/97586019-1e620680-1a3d-11eb-8e12-e4e96a1afdfd.png)

실행이 잘 되었습니다.

다시 commit history를 보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97586381-89134200-1a3d-11eb-87ac-2690b8c80dd8.png)

그러면 이제 두 branch가 같은 commit에 놓여있는 것을 알 수 있습니다. remote repository의 master branch도
이제 최신 내용을 가지고 있는 것입니다.

저는 local repository에서 premium branch도 만들었는데요. premium branch도 remote repository에 올려보겠습니다.   
일단 premium branch로 이동한 다음에

![image](https://user-images.githubusercontent.com/64893709/97586792-0474f380-1a3e-11eb-94d6-40edd28ca7d0.png)

이 상태에서 git push를 하겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97587032-4d2cac80-1a3e-11eb-8ba4-1b791b42b91d.png)

그런데 에러가 발생했습니다.   
에러 내용을 읽어보면, premium branch가 upstream branch를 갖고 있지 않다는 내용이 출력되었습니다.   
그리고 git push --set-upstream origin premium을 실행하라는 내용도 출력되었습니다.

이전 강의에서 배웠던 내용 기억 나시나요?

![image](https://user-images.githubusercontent.com/64893709/97588215-9d583e80-1a3f-11eb-8cf1-b17813e19b63.png)

local repository에 있는 branch를 remote repository로 맨 처음 push 할 때는 --set-upstream 옵션을 붙여야 한다고 배웠습니다.   
그래야 tracking 정보가 설정되어서 git push만 써도 된다고 했습니다.   
premium repository는 remote repository에 처음 올리는 것이기 때문에 --set-upsetream 옵션을 써줘야 합니다.

그러면 ```git push --set-upstream origin premium```를 그대로 작성해보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97588559-f4f6aa00-1a3f-11eb-8b82-ab09d391ede1.png)

이렇게 하면 remote repository에도 premium branch가 생깁니다.

이제 GitHub로 들어가서 변경 사항을 살펴보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97588659-15266900-1a40-11eb-875e-ba647b6871f3.png)

2개의 branch가 생겼습니다. 이것을 클릭해보면,

![image](https://user-images.githubusercontent.com/64893709/97589019-6898b700-1a40-11eb-9871-2252252e92d8.png)

저희가 작성했던 premium branch가 추가된 것을 알 수 있습니다. 이것도 클릭해보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97589196-95e56500-1a40-11eb-95e2-d796fab6f85a.png)

premium branch를 클릭하시면 이런 식으로 저희가 지금까지 했던 12개의 commit이 잘 보입니다. 이것도 눌러보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97589446-d7761000-1a40-11eb-992b-9517bf1addcc.png)

commit history가 잘 보입니다.

터미널로 돌아가서 commit history를 살펴보면,

![image](https://user-images.githubusercontent.com/64893709/97589573-02f8fa80-1a41-11eb-8414-a6bff6289c94.png)

이제 remote repository의 premium branch도 잘 보입니다.
