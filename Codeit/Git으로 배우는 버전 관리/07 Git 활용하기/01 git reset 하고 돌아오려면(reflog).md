Git reset은 HEAD가 가리키던 branch가 가리키는 commit을 바꾸는 커맨드라고 배웠는데요.

그런데 git reset을 보면 한 가지 궁금한 점이 생길 수 있습니다.

만약 과거의 commit으로 reset을 하면 그 commit 이후로 했던 commit들은 어떻게 되는 걸까요?

우선 commit history를 살펴보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99382546-0ed52f80-2910-11eb-8923-1c160f2eecbb.png)

위에서 가장 최초로 한 노란색 표시의 commit으로 reset을 해보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99382707-42b05500-2910-11eb-8316-0b34c89c1635.png)

working directory에 있는 내용도 다 초기화 되었습니다.

잘 되었는지 확인하기 위해서 cat 명령어를 실행해보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99383191-dd109880-2910-11eb-9939-8371d8ea5a10.png)

파일의 내용이 맨 처음 commit의 내용으로 돌아갔음을 확인할 수 있습니다.

다시 git history를 보면,

![image](https://user-images.githubusercontent.com/64893709/99383290-fdd8ee00-2910-11eb-81c2-45cc601658e2.png)

commit history가 하나밖에 없는 것을 확인할 수 있습니다.

그럼 제가 지금까지 한 commit들은 사라진 걸까요?

사실 그렇지는 않습니다.

![image](https://user-images.githubusercontent.com/64893709/99383401-252fbb00-2911-11eb-8043-9d696224bcb2.png)

다시 이전 commit history를 보면, 

![image](https://user-images.githubusercontent.com/64893709/99383507-4d1f1e80-2911-11eb-9861-9e583df4d686.png)

가장 최근의 했던 commit의 아이디가 9856이라는 것을 알 수 있습니다.

이 최신 commit으로 다시 reset을 해보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99386494-e51f0700-2915-11eb-9d33-feb2a75250ea.png)

다시 git history를 보면,

![image](https://user-images.githubusercontent.com/64893709/99386588-0f70c480-2916-11eb-9b06-b7dfb4731902.png)

이전처럼 다시 예전의 commit들이 잘 보인다는 것을 알 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/99386633-20213a80-2916-11eb-882b-3163998afa9d.png)

추가했던 divide_new 함수까지 내용이 잘 보입니다.

제가 방금 보여드린 대로 git reset을 하더라도 commit들이 삭제되는 것은 아닙니다.

단지 HEAD가 가리키는 branch가 새로운 commit을 가리키게 될 뿐입니다.

그래도 최신 commit으로 돌아가려면 방금 최신 commit의 아이디를 알아야 했는데요.

방금 같은 경우에는 제가 commit history를 미리 출력했어서 그 아이디를 찾을 수 있었지만 만약 commit history를 출력하지 않고 그냥 git reset을 했다면 어떻게 해야할까요?

git reset --hard를 하고 이번에도 맨 처음 commit으로 돌아가 봅시다.

![image](https://user-images.githubusercontent.com/64893709/99393189-4fd54000-2920-11eb-98f9-e99321d14d26.png)

그리고 git history를 하면

![image](https://user-images.githubusercontent.com/64893709/99393250-69768780-2920-11eb-8079-2cdab598c95b.png)

reset이 잘 되었습니다.

이제부터 최신 commit 아이디를 모른다고 가정해봅시다. 그러면 어떻게 원래대로 돌릴 수 있을까요?

이때 쓰는 커맨드가 바로 git reflog라는 커맨드입니다.

![image](https://user-images.githubusercontent.com/64893709/99393435-ad698c80-2920-11eb-8cf2-9fcb560fe990.png)

relog는 reference log의 줄임말인데요. reference log는 HEAD가 지금까지 가리켜왔던 commit들을 기록한 정보입니다.

실행을 해보면,

![image](https://user-images.githubusercontent.com/64893709/99393545-d7bb4a00-2920-11eb-9261-d24b2cfec781.png)

이런 식으로 HEAD가 가리켜온 commit들을 보여줍니다.

여기서 각 한 줄은 HEAD가 가리키던 commit이 바뀌었을 때 기록된 것이라고 보면 됩니다.

위에서 노란색으로 표시된 HEAD@{1}이라는 문구는 노란색으로 표시된 그 다음 문장의 동작을 통해서 HEAD가 가리키게 된 commit을 말합니다.

그리고 그 commit의 아이디는 바로 첫 번째의 노란색 표시인 9856988입니다. 이것을 통해서 저는 최신 commit으로 돌아갈 수 있습니다.

우선 ```q```를 눌러서 나간 후

![image](https://user-images.githubusercontent.com/64893709/99393928-6760f880-2921-11eb-937a-52317fb0f557.png)

이렇게 작성하면 HEAD가 다시 최신 commit을 가리키게 됩니다. (HEAD@{1}을 9856으로 적어도 같은 동작이 실행됩니다.)

git history를 다시 보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99394090-aabb6700-2921-11eb-828d-65d96cffad37.png)

내용이 잘 복구됐음을 알 수 있습니다.

