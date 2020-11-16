이전 수업에서는 commit을 하고 그것을 바로 revert 해봤습니다.

그런데 사실 더 과거의 commit을 대상으로, 그리고 여러 개의 commit을 대상으로 한 번에 revert하는 것도 가능합니다.

이전에 저는 README 파일을 만들고 그것을 더 예쁘게 꾸며주기 위해 이런저런 markdown 언어를 붙인 적이 있었는데요.

![image](https://user-images.githubusercontent.com/64893709/99261228-c1998500-285f-11eb-8670-3f7362bd5e4f.png)

지금 README 파일은 위와 같이 생겼습니다.

그런데 이 README 파일을 다른 팀에서 더 예쁘게 만들어서 전달해 줄거라고 하네요.   
그래서 기존의 README 파일은 간단한 설명만 남겨두고 전부 초기화하라는 얘기를 들었다고 가정해 봅시다.

그러면 master branch와 premium branch에서 모두 README 파일을 초기화 해줘야겠죠?

일단 제가 있는 master branch에서 먼저 해보겠습니다. 우선 commit hisoty를 다시 보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99261464-1dfca480-2860-11eb-86ae-d2acfe0f2125.png)

위에서 노란색으로 표시된 commit에서 README 파일을 처음 생성하고,   
초록색으로 표시된 commit에서 README 파일에 calculator.py 파일에 대한 설명을 추가하고,   
마지막으로 파란색으로 표시된 commit에서 README 파일을 markdown으로 예쁘게 꾸며줬습니다.

이 중에서 README 파일을 생성한 commit을 제외한 나머지 두 commit을 revert 해보겠습니다.

그러면 ```git revert```를 쓰고 한 칸 띄어서 어느 commit부터 어느 commit까지 revert 해줄지를 써줘야 하는데요.

![image](https://user-images.githubusercontent.com/64893709/99262001-c7439a80-2860-11eb-8926-2e6c87234600.png)

위와 같이 써주면 되는데요.
여기서 주의해야 할 점은 처음의 facd commit은 revert에 포함되지 않는다는 점입니다.

실행하면 다음과 같이 commit 메시지를 작성할 수 있는 창이 뜹니다.

![image](https://user-images.githubusercontent.com/64893709/99262186-ff4add80-2860-11eb-81a0-64b683239780.png)

이전에 봤던 것처럼 Revert 하고 commit 메시지가 보입니다.   
commit 메시지를 수정해도 되지만 이 commit이 revert할 때 생긴 commit이라는 것을 알기 위해서 이대로 두는 것이 좋습니다.

![image](https://user-images.githubusercontent.com/64893709/99262346-34573000-2861-11eb-8627-74ddf5323415.png)

```:wq```를 쓰고 엔터를 누르면 위처럼 revert commit 이 두 개 생기게 되는데요. 정말 README 파일이 초기화됐을까요? 한번 확인해보겠습니다.

그러면 제가 처음에 README 파일을 만들었던 모습으로 돌아간 것을 알 수 있습니다. revert가 잘 된 것입니다.

![image](https://user-images.githubusercontent.com/64893709/99262525-741e1780-2861-11eb-94ed-ff218e01f286.png)

commit history도 보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99262629-8bf59b80-2861-11eb-9a25-c492aba9501a.png)

commit history를 보면 실제로 commit 했던 순서와는 다르게 거꾸로 commit들이 revert된 것을 알 수 있습니다.

새로운 revert commit 두 개도 remote repository에 push하겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99262828-c3644800-2861-11eb-89fc-081375835bed.png)

그리고 다시 commit history를 보면 

![image](https://user-images.githubusercontent.com/64893709/99262935-e42c9d80-2861-11eb-907a-4f962c8988c8.png)

remote repository에 제가 revert한 commit들이 다 반영되어 있다는 것을 알 수 있습니다.

이번에는 premium branch롤 가서 해보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99262997-f7d80400-2861-11eb-91d5-d41930c6af42.png)

이것도 마찬가지로 master branch와 똑같이 해주면 됩니다.

먼저 commit history를 보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99263115-1c33e080-2862-11eb-9995-0d72d6f1e351.png)

여기에서도 파란색으로 표시된 commit과 초록색으로 표시된 commit 두 개를 revert하면 되는데요.

![image](https://user-images.githubusercontent.com/64893709/99263263-4f766f80-2862-11eb-9ec7-4d3bd1aaf45a.png)

위처럼 한 후에 실행하면

![image](https://user-images.githubusercontent.com/64893709/99263355-661cc680-2862-11eb-8cb2-5aee992f20c0.png)

위처럼 commit 메시지를 작성할 수 있는 창이 나오고 이것을 그대로 저장해주면 

![image](https://user-images.githubusercontent.com/64893709/99263419-82206800-2862-11eb-8a28-36342397ef3b.png)

마찬가지로 revert commit이 두 개 출력되는 것을 볼 수 있습니다.

다시 commit history를 보면 

![image](https://user-images.githubusercontent.com/64893709/99263553-b7c55100-2862-11eb-82b8-ff9e19504236.png)

revert commit이 두 개 생겼다는 것을 알 수 있습니다.

이 두 개도 remote repository에 push하겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99263657-d62b4c80-2862-11eb-9018-c53a8f31165d.png)

그리고 다시 commit history도 다시 보면,

![image](https://user-images.githubusercontent.com/64893709/99263730-f3601b00-2862-11eb-8474-a34098eab3dd.png)

remote repository에 local repository에서 했던 revert commit 두 개가 잘 반영돼 있다는 것을 알 수 있습니다.
