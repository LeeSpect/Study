이번에는 premium branch에서 팩토리얼이라는 함수를 추가해보겠습니다.

서브라임 텍스트로 이동해서,

![image](https://user-images.githubusercontent.com/64893709/104598611-1ddf2080-56ba-11eb-8ee6-b13866bae899.png)

이렇게 함수를 적어주시고요. commit을 해줍니다.

![image](https://user-images.githubusercontent.com/64893709/104598676-351e0e00-56ba-11eb-9618-a657f8106dc7.png)

그런데 프로그래밍을 하다가 팩토리얼의 값을 더 효율적으로 계산해주는 방법을 찾았다고 가정해봅시다.

그래서 서브라임 텍스트에서 방금 작성한 코드를 수정해줘야 한다고 해봅시다.

![image](https://user-images.githubusercontent.com/64893709/104598871-6991ca00-56ba-11eb-84c2-6142ff1ad4f8.png)

위처럼 수정을 하고 다시 터미널로 이동해 commit을 해줍시다.

![image](https://user-images.githubusercontent.com/64893709/104598943-83cba800-56ba-11eb-86c3-6f29ef6e8df5.png)

commit history를 보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/104599010-98a83b80-56ba-11eb-81f1-8198d5ecd723.png)

그러면 위에서 노란색으로 표시된 것처럼 제가 추가한 factorial function이 잘 보입니다.

그런데 불만이 하나 있는데요. 

![image](https://user-images.githubusercontent.com/64893709/104599233-dad17d00-56ba-11eb-8b3f-5f570f7be26a.png)

위에서 노란색으로 표시된 것처럼 맨 처음 팩토리얼 함수를 추가하고 했던 commit은 지금 와서 보면 필요 없는 commit입니다.

이 commit을 그냥 없었던 것으로 하고 싶으면 어떻게 해야할까요? 이때는 우리가 배웠던 git reset 커맨드를 쓰면 됩니다.

![image](https://user-images.githubusercontent.com/64893709/104599424-12d8c000-56bb-11eb-85e0-fd28c2c8c6aa.png)

지금 이 상태에서 팩토리얼 함수가 없을 때의, 위에서 노란색으로 표시된 commit으로 reset을 해봅시다.

대신에 옵션으로 soft나 mixed를 써서 현재 working directory의 모습은 건드리지 않아야 합니다.   
그래야 효율적인 팩토리얼 함수의 코드가 유지되겠죠? 저는 --soft 옵션을 써보겠습니다. 일단 ```q```를 눌러서 나가주시고요.

![image](https://user-images.githubusercontent.com/64893709/104599762-867acd00-56bb-11eb-988f-af5a048c94f8.png)

위처럼 실행하면 과거의 commit으로 reset이 되면서도 현재 working directory의 모습은 보존됩니다.

이제 우리가 해야할 작업은 간단한데요. 일단 working directory의 모습은 최신 상태이기 때문에 이 상태에서 그냥 commit을 해주면됩니다.

그리고 다시 commit history를 살펴보면,

![image](https://user-images.githubusercontent.com/64893709/104599991-c93ca500-56bb-11eb-9235-53d297aecbab.png)

위처럼 Add commit도 하나가 되었고 팩토리얼 함수도 효율적으로 바뀌었음을 알 수 있습니다.
