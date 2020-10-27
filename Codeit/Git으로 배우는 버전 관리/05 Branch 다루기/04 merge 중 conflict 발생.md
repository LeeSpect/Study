이전 수업에서는 merge를 해봤습니다. 그런데 merge를 할 때는 문제가 생기는 경우도 있는데요. 무슨 말인지 바로 보여드리겠습니다.

일단 저는 premium branch에 있는데요. 여기에서 calculator.py 파일을 고쳐보겠습니다.

서브라임 텍스트로 이동한 다음에 divide 함수의 이름을 divide_premium으로 수정(생략)

터미널로 이동한 다음에 git add .를 해주고 commit을 해주겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97309839-dfe61380-18a5-11eb-86ec-e8e21d32fac1.png)

이번에는 master branch 이동해 보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97309888-effdf300-18a5-11eb-948d-1f3df3db540e.png)

그리고 마찬가지로 서브라임 텍스트로 이동한 다음 calculator.py 파일에서 divide 함수의 이름을 divide_free로 바꿔주겠습니다.(생략)

다시 터미널로 가서 commit을 해주겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97312007-5be15b00-18a8-11eb-9cc6-98994775e645.png)

commit이 잘 되었습니다.

이제 다시 premium branch로 가볼게요.

![image](https://user-images.githubusercontent.com/64893709/97312135-7ca9b080-18a8-11eb-8afd-a28a51fa3047.png)

지금 이 상태에서 master branch를 merge하면 어떻게 될까요?

![image](https://user-images.githubusercontent.com/64893709/97312246-9cd96f80-18a8-11eb-98c0-d54fbbf86360.png)

실행을 하니까 처음 보는 문장들이 출력됩니다.

![image](https://user-images.githubusercontent.com/64893709/97312514-e5912880-18a8-11eb-81f2-1cb8c08a3b25.png)

이렇게 CONFLICT라는 단어가 출력됐는데요. 그리고 그 뒤를 보면 calculator.py 파일에서 Metge conflict가 발생했다는 문장이 있습니다.   
이 말은 merge를 하다가 충돌이 발생했다는 말인데요. 무슨 일이 생긴건지 확인해보겠습니다.

다시 서브라임 텍스트에서 calculator.py 파일을 열어주세요.

![image](https://user-images.githubusercontent.com/64893709/97312671-12ddd680-18a9-11eb-8729-bcc9c3586ea2.png)

위처럼 처음 보는 부분이 생겼는데요. 바로 이 부분이 conflict가 발생한 부분입니다.

조금 더 자세히 살펴보면,

![image](https://user-images.githubusercontent.com/64893709/97312823-402a8480-18a9-11eb-8ccc-06fdea995740.png)

노란색으로 표시된 가운데 선을 중심으로 각 branch의 내용이 입력되어 있습니다.

이런 상황에서 두 branch를 merge하려고 하면 Git은 divide_free와 divide_premium 중 어느 것을 반영해야 할지 결정할 수 없습니다. 

![image](https://user-images.githubusercontent.com/64893709/97313148-a57e7580-18a9-11eb-9a31-7f2c65af4913.png)

이것을 Comflict라고 부르는데요. Git은 Conflict가 발생하면 사용자에게 위와 같은 방법으로 알려줍니다.

그러면 이제 Conflict를 해결하는 방법을 알아보겠습니다.   
우선 지금은 premium branch에서 master branch를 merge하고 있는 상황입니다.   
일단 여러분은 선택을 해야 하는데요. 앞으로 premium branch에서 divide 함수의 이름을 무엇으로 정할지입니다. divide_premium으로 해도 됩니다.
아니면 아예 새 이름을 정해도 됩니다. 저는 아예 새로운 이름으로 해보겠습니다.

이제 위에서 표시된 부분들을 다 지워주시고 divide_new라는 함수를 새롭게 작성해주세요.

![image](https://user-images.githubusercontent.com/64893709/97313527-12920b00-18aa-11eb-8970-2892eef70e58.png)

다시 터미널로 이동하겠습니다.   

터미널로 이동한 다음에 그냥 commit을 해주면 되는데요.

![image](https://user-images.githubusercontent.com/64893709/97313638-36555100-18aa-11eb-82eb-e474d01bfd4e.png)

그러면 아래와 같이 commit 메시지를 쓸 수 있는 창이 하나 뜨는데요.

![image](https://user-images.githubusercontent.com/64893709/97313784-5e44b480-18aa-11eb-94d1-2d2f63f1bbe4.png)

Conflict를 해결하고 commit을 하면 위에서 노란색으로 표시된 것과 같은 commit 메시지가 뜹니다.
이 commit 메시지를 수정해도 되고 그대로 써도 됩니다. 저는 그냥 그대로 쓸게요. 그리고 ```:wq```를 사용해 저장합니다.

![image](https://user-images.githubusercontent.com/64893709/97314076-abc12180-18aa-11eb-8348-304facdc7241.png)

이제 merge가 완료되고 새로울 merge commit이 생겼을 것입니다.

한번 확인해보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97314149-c09db500-18aa-11eb-8142-ff354ab021fe.png)

merge commit이 잘 추가된 것을 볼 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/97314250-d6ab7580-18aa-11eb-9197-35bce322982c.png)

