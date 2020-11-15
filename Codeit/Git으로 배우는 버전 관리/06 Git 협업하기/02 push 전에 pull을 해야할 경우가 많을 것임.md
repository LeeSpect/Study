우리는 이전 수업에서 git push 커맨드와 git pull 커맨드를 배웠습니다.

![image](https://user-images.githubusercontent.com/64893709/99162608-024fac00-2743-11eb-8df9-dcfc0e613a43.png)

git push는 local repository에 있는 branch 내용을 remote repository의 branch로 보내는 것이었고

git pull은 remote repository에 있는 branch 내용을 local repository로 받아오는 것이었습니다.

이번 수업에서는 git push를 쓸 때 자주 만나게 되는 상황을 알려드리겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99162623-214e3e00-2743-11eb-8baf-9b2660a17ffe.png)

일단 저는 지금 master branch에 있는데요. premium branch로 이동하겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99162638-3cb94900-2743-11eb-9986-151393c50a0c.png)

이제 premium branch의 라이센스 파일을 살펴보겠습니다. 

![image](https://user-images.githubusercontent.com/64893709/99162644-4e025580-2743-11eb-9fcb-c6ae6ab3ba0a.png)

기본 라이센스에 Premium이라고만 적혀 있습니다.

Premium 버전에 대해서 더 자세한 정보를 추가해 보겠습니다. 먼저 서브라임 텍스트로 이동해주세요.

( 생략 ) 이제 Premium 버전이 기업용으로 얼마인지 작성해보겠습니다... 다시 터미널로 이동하겠습니다.

git add .를 해주고 commit을 해주겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99162686-b5200a00-2743-11eb-973a-f9eeb2c7d06b.png)

local repository의 premium branch에서 commit을 했습니다. 이제 remote repository의 premium branch로 가보겠습니다.   

GitHub 페이지로 이동해주세요.

( 생략 ) GitHub의 repository 안에 branch를 누르시고 premium을 클릭해주세요.   
그러면 premium branch로 이동하는데요.

premium branch인지 확인하는 방법은

![image](https://user-images.githubusercontent.com/64893709/99181411-b831ef00-2771-11eb-8493-22945bececa3.png)

이렇게 주소를 확인하면 됩니다.

( 생략 ~ ) GitHub의 premium branch에서도 라이센스 파일을 수정해보겠습니다.   
먼저 라이센스 파일을 클릭해주시구요.   
그리고 여기에 연필 모양을 눌러주세요.   
줄을 바꾼 다음에,   
GitHub에서는 교육용으로 이 프로그램을 쓸 경우에 얼마를 받을지 적어두겠습니다.   
이런 식으로 내용을 다 수정했는데요.   
교육용은 기업용보다 싸도록 한 달에 $10이라고 적었습니다.   
그리고 내려서 commit 메시지에는 'Update License for educational use'라고 적어두겠습니다.   
그리고 아래 초록 버튼을 눌러 commit을 하겠습니다. commit이 잘 됐죠? ( ~ 생략 )

지금 상황을 정리해보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99181590-c2082200-2772-11eb-8e79-0e56890a93a3.png)

local repository의 premium branch와 remote repository의 premium branch가 가리키는 최신 commit이 서로 다릅니다.    
local에서는 기업용 요금 정보를 추가했고 remote에서는 교육용 요금 정보를 추가했으니까요.   
그러니까 한 프로그램을 각각 다른 개발자가 다른 방식으로 개발한 것입니다. 이런 일은 실제로 자주 일어납니다.

![image](https://user-images.githubusercontent.com/64893709/99181695-65f1cd80-2773-11eb-8d44-344fee5cbc93.png)

방금 GitHub에서 직접 remote repository를 수정한 것은 사실 다른 개발자가 remote repository를 수정한 것을 가정한 것입니다.   
그러니까 저의 동료 개발자가 자기 컴퓨터에서 premium branch에 교육용 요금 정보를 추가하고 commit했다고 생각해보세요.

그리고 이것을 그대로 remote repository의 premium branch로 git push를 하면 저의 local repository에 있는 premium branch와는 내용이 달라집니다.

이런 상황은 어쩌면 당연할 수도 있는데요.   
remote repository를 중심으로 협업을 하다 보면 자연스럽게 일어나는 현상입니다.

![image](https://user-images.githubusercontent.com/64893709/99181725-bbc67580-2773-11eb-8ba3-3f063f735635.png)

이 상태에서, local repository에서 git push를 하면 어떻게 될까요?

![image](https://user-images.githubusercontent.com/64893709/99181737-cf71dc00-2773-11eb-9135-97dfc11ec9e3.png)

push가 되지 않습니다.   
왜냐하면 이미 다른 개발자가 추가한 내용이 있는데, 제 것을 그냥 반영해버리면 다른 개발자가 고생해서 개발한 내용이 덮어써지기 때문입니다.

이렇게 제가 local repository를 수정하는 동안 이미 remote repository에 변화가 생겼다면 바로 git push를 할 수 없습니다.

![image](https://user-images.githubusercontent.com/64893709/99182123-4dcf7d80-2776-11eb-96d5-9b2ea24c951e.png)

이때는 일단 git pull을 해야됩니다.

![image](https://user-images.githubusercontent.com/64893709/99182137-66d82e80-2776-11eb-99be-7c261bd8ec50.png)

git pull을 하면 다른 개발자가 작업했던 내용이 현재 저의 premium branch에도 반영됩니다. 한번 해보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99182239-17dec900-2777-11eb-89c5-6f9b63e8bdd4.png)

이번에도 뭔가 에러가 났습니다. 낯익은 에러 메시지네요.

예전에 merge를 할 때 conflict가 발생하는 경우에서 봤던 에러죠.   
그런데 지금 왜 merge conflict가 났을까요?

git pull을 하면 remote repository의 premium branch에 있는 최신 commit들을 local branch의 premium branch로 가져옵니다.

![image](https://user-images.githubusercontent.com/64893709/99182304-920f4d80-2777-11eb-8b45-d823b48fdd25.png)

그리고 그것을 그대로 merge하는데요.   

![image](https://user-images.githubusercontent.com/64893709/99182337-c71ba000-2777-11eb-99f2-741e06dbfe45.png)

이렇게 remote repository의 최신 commit들을 가져와서 merge하는 과정까지가 git pull입니다.

그래서 git pull을 할 때도 conflict가 발생할 수 있는 겁니다.   
이 상태에서 어떻게 하면 이 문제를 해겷할 수 있을까요?

예전에 conflict를 해결하는 방법 배웠었죠? 그때 했던 대로 하시면 됩니다.

( 생략 ) 일단 서브라임 텍스트로 이동해 볼게요.   
conflict가 발생한 라이센스 파일을 보면 예전에 봤었던 표시가 하나 보입니다.

![image](https://user-images.githubusercontent.com/64893709/99182401-1feb3880-2778-11eb-8655-fbba2b8f1ae6.png)

이 내용을 원하는 내용으로 만들어주면 됩니다.   
저는 제가 추가한 기업용 요금과 다른 개발자가 추가한 교육용 요금 두 가지 정보가 모두 필요합니다.   

![image](https://user-images.githubusercontent.com/64893709/99182432-51fc9a80-2778-11eb-93d1-8520e88f994e.png)

그래서 이런 식으로 필요 없는 부분을 모두 지우고 저장을 해주겠습니다.   
그 후 터미널로 가서 git add .를 해주시구요. 다시 git commit을 하겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99182474-82dccf80-2778-11eb-90a6-3a2da03d940a.png)

그러면 이런 식으로 commit 메시지가 준비되어 있죠?   
해석해보면 remote repository에 premium branch를 local repository의 premium branch로 merge한다는 뜻입니다.

사실 git pull은 결국 remote repository의 branch를 가져와서 merge하는 동작입니다.   
그래서 방금처럼 merge conflict도 나온 것입니다.   
이 merge를 잘 마무리하면 git pull이 완료되는 겁니다. 한번 해보겠습니다. ```:wq``` 하고 엔터하면

![image](https://user-images.githubusercontent.com/64893709/99182559-f088fb80-2778-11eb-943d-a162ae33fdfb.png)

이렇게 하면 하나의 새로운 commit이 생기고 git pull이 잘 완료된 겁니다.

결국 git pull은 remote repository의 branch를 가져와서 현재 branch에 merge하는 커맨드하고 이해할 수 있겠습니다.

지금 상태를 한번 살펴보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/99182598-229a5d80-2779-11eb-82c5-d11fe813657b.png)

그러면 저희가 방금 git pull을 통해서 merge한 commit이 잘 보이죠?   
이제 git push를 해줍시다.

![image](https://user-images.githubusercontent.com/64893709/99182622-46f63a00-2779-11eb-9010-df6458d0d48f.png)

그러면 이제는 push가 잘 됩니다.

( 생략 ) 이제 remote repository로 가서 확인해보겠습니다.   
GitHub 페이지로 이동해주세요.   
GitHub 페이지에서 라이센스 파일을 보시면 제가 merge한 내용이 잘 반영되어 있습니다.   
( 생략 )혹시 반영이 안 되어 있다면 새로고침 버튼을 한번 눌러주세요.

정리해보겠습니다.

A라는 개발자와 B라는 개발자가 동시에 똑같은 remote repository를 가져와서 각각 새로운 commit을 했다고 가정해봅시다.

![image](https://user-images.githubusercontent.com/64893709/99182679-b10edf00-2779-11eb-9251-850db1ce1bbd.png)

이때 개발자 B가 먼저 git push를 하고 나면 개발자 A는 바로 git push를 할 수 없습니다.

![image](https://user-images.githubusercontent.com/64893709/99182695-ce43ad80-2779-11eb-8aae-f12c83d53286.png)

그래서 이때 git pull을 이용해서 remote repository의 branch에 있는 다른 개발자가 한 commit을 자신의 local repository에 있는 branch에도 반영시켜야 합니다.

![image](https://user-images.githubusercontent.com/64893709/99182733-2084ce80-277a-11eb-9f15-7475d102050d.png)

이 과정은 결국 remote repository의 branch를 가져와서 내 local repository에 merge하는 것과 같습니다.

그런데 이때 git pull이 바로 성공하는 경우도 있지만 대부분의 경우에는 conflict가 납니다.   
이때는 그냥 conflict를 해결해주고 다시 commit을 하면 됩니다.

그리고 나서 git push를 해주면

![image](https://user-images.githubusercontent.com/64893709/99182778-6b064b00-277a-11eb-947c-a724ea75a82d.png)

정상적으로 push가 됩니다.   
현실에서는 여러 개발자가 하나의 프로젝트에서 협업할 때가 많습니다.   
그래서 git push가 바로 잘 안 되는 경우가 오히려 일반적입니다.   
그럴 때는 당황하지 말고 오늘 배운 것처럼 일단 git pull을 해보면 되겠죠.
