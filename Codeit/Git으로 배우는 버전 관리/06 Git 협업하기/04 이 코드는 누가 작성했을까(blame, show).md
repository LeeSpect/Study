Git을 쓰다 보면 하나의 파일이 지금까지 어떻게 변해온 것인지를 파악해야 할 때가 있습니다.

예를 들어 지금 제 프로젝트에 있는 calculator.py 파일도 모든 코드를 한 번에 다 쓰고 commit한 것이 아닙니다.

아주 조금씩 내용을 추가하거나 수정하면서 여러 번의 commit을 한 결과가 지금의 모습인 겁니다.

한 가지 파일이 완성되기까지 어떤 commit들이 있었는지를 볼 수 있는 커맨드가 있습니다.

바로 ```git blame```이라는 커맨드입니다.

![image](https://user-images.githubusercontent.com/64893709/99247052-b89db900-2849-11eb-829d-d521529d6510.png)

이렇게 적어주시면 됩니다.

![image](https://user-images.githubusercontent.com/64893709/99247198-f4388300-2849-11eb-921d-dc1aa69dede4.png)

blame은 어떤 파일의 특성 코드를 누가 작성했는지 찾아내기 위한 커맨드입니다. 그리고 그 코드를 작성한 사람의 탓으로 돌리기 위한 커맨드인 겁니다.

여기까지 썼으면 한 칸을 띄우고 원하는 대상인 calculator.py 파일을 적어주겠습니다.

그리고 실행을 하면,

![image](https://user-images.githubusercontent.com/64893709/99247346-2cd85c80-284a-11eb-9f83-fe31beb1ddfc.png)

이렇게 calculator.py의 각 부분이 어떤 commit으로 인해 탄생했는지를 한 눈에 볼 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/99247412-44afe080-284a-11eb-9927-385d2d6286f1.png)

위에서 왼쪽에 있는 것들은 모두 commit 아이디 입니다.

![image](https://user-images.githubusercontent.com/64893709/99247599-8476c800-284a-11eb-9035-0393bbd60d50.png)

그러니까 위에서 세 번째로 표시된 코드는 첫 번째로 표시된 commit에 의해 탄생한 코드라는 겁니다.

그러면 이 commit을 누가 한 것인지는 어떻게 볼 수 있을까요? 바로 두 번째로 표시된 부분을 보면 되는데요. 이것 말고 다른 방법도 있습니다.

예전에 배웠었는데요. ```git show```를 쓰면 됩니다.

![image](https://user-images.githubusercontent.com/64893709/99247680-a1130000-284a-11eb-8f3d-f3d92878e24e.png)

git show를 쓰고 위에서 궁금한 commit의 아이디를 씁니다. 실행하면,

![image](https://user-images.githubusercontent.com/64893709/99247756-bc7e0b00-284a-11eb-87c5-a85234737f50.png)

누가 이 commit을 한 것인지 알 수 있습니다.

이제 이 코드를 작성한 사람은 codeit이라는 것을 알 수 있습니다.

