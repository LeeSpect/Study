이전 수업에서는 git stash가 뭔지 어떤 상황에서 쓰는 지 배웠습니다.

그런데 git stash를 쓰는 또다른 경우가 있습니다.

그것은 바로 잘못된 branch에서 작업했을 때인데요.

![image](https://user-images.githubusercontent.com/64893709/102707776-30478380-42e1-11eb-8a21-8ee12cc9e4b4.png)

잠시 무료 버전을 위한 master branch로 이동하겠습니다.

![image](https://user-images.githubusercontent.com/64893709/102707786-45241700-42e1-11eb-933a-0350fd20e1ed.png)

그리고 퍼센트를 구하는 함수를 하나 추가해보겠습니다. 서브라임 텍스트로 이동해주세요.

![image](https://user-images.githubusercontent.com/64893709/102707799-6422a900-42e1-11eb-9b75-453f226c385d.png)

퍼센트를 구하는 함수를 쓰고 저장을 하겠습니다.

앞서 말씀드린 대로 잘못된 branch에서 작업하고 있을 때를 예시로 들고 있는데요.

![image](https://user-images.githubusercontent.com/64893709/102707831-b368d980-42e1-11eb-8a05-12ed3de09d2a.png)

위에서 새로 추가한 get_Percent 함수는 무료버전에 있으면 안 되고 premium branch에 있어야 하는 함수였다고,
그러니까 premium branch에서 해야할 작업을 master branch에서 한 상황이라고 가정해봅시다.

이런 상황에서는 git stash를 쓰면 문제를 쉽게 해결할 수 있습니다.

일단 터미널로 돌아가서 git stash를 입력하겠습니다.

![image](https://user-images.githubusercontent.com/64893709/102707846-c54a7c80-42e1-11eb-96db-5d50355d2292.png)

저장이 잘 되었습니다.

그리고 premium branch로 이동해주세요.

![image](https://user-images.githubusercontent.com/64893709/102707868-0478cd80-42e2-11eb-9b98-e7877dc1ebbd.png)

앞서 말씀드린 대로 get_Percent 함수는 master branch에 있으면 안 되고 premium branch에 있어야 합니다.
하지만 저희는 master branch에서 작업을 했었죠?

그럼 아까 작업한 내용을 다시 불러와 보겠습니다.

git stash로 저장한 작업물은 꼭 같은 branch에서만 적용할 수 있는 것은 아닙니다.

잠시 저장된 작업 내용을 살펴보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/102707908-5f122980-42e2-11eb-9b99-1f5f8847c165.png)

그러면 이전 수업에서 작업한 내용까지 총 2개의 내용이 있습니다.

이 상황에서 ```git stash apply```를 써주면 위에서 노란색으로 표시된 것처럼 더 최근에 작업한 내용이 적용됩니다.   
그래서 git stash apply를 써줘도 되지만 보통 어떤 작업을 적용할 것인지 정확하게 지정하는 것이 좋습니다.

그래서 작업 내용의 id를 apply 뒤에 써주겠습니다. 그리고 실행을 하면, 

![image](https://user-images.githubusercontent.com/64893709/102707926-7ea95200-42e2-11eb-8056-8a0132e996a5.png)

위에서 노란색으로 표시된 것처럼 CONFLICT가 발생합니다.   
CONFLICT를 해결하기 위해서 서브라임 텍스트로 이동해주세요.

![image](https://user-images.githubusercontent.com/64893709/102707970-d8aa1780-42e2-11eb-9eca-9c831bf7e9d5.png)

지금 원래 premium branch에 있던 calculator.py 내용과 방금 작업했던 내용 사이에 충돌이 생겨서 그런 것인데요.

위에서 노란색으로 표시된 방금 master branch에서 작업한 get_Percent 함수가 보이죠?

이제 CONFLICT를 해결하기 위해서 필요 없는 내용을 다 지우고 저장하겠습니다.   
그리고 divide_free 함수도 삭제해주셔야 하는데요. 지금 있는 premium branch는 유료 버전이기 때문에 divide_free는 필요가 없습니다.

이제 commit을 하겠습니다. 터미널로 이동해서 commit을 해주세요.

![image](https://user-images.githubusercontent.com/64893709/102708236-d21c9f80-42e4-11eb-9624-79e535a833fe.png)

![image](https://user-images.githubusercontent.com/64893709/102711453-35b2c700-42fd-11eb-8cd5-4ff69c841174.png)

branch 수가 많을 때는 종종 잘못된 branch에서 작업하는 실수를 할 수 있습니다.   
그럴 때는 우선 git stash로 stack에 작업 내용을 저장한 다음, 올바른 branch로 가서 다시 git stash apply를 하면 됩니다.

그런데 git stash를 이런 식으로 자주 사용하다 보면 stack에 작업 내용이 쌓여서 나중에 보기가 힘들겠죠?
보통 이미 적용한 작업은 지워주는 것이 좋습니다.

다시 작업 내용들을 보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/102711469-55e28600-42fd-11eb-9bf0-343a5b125687.png)

여기에서 첫 번째 작업 내용을 삭제하려면 

![image](https://user-images.githubusercontent.com/64893709/102711473-6692fc00-42fd-11eb-8c05-c6b58d42e4a6.png)

위처럼 ```drop```을 이용하는데요. drop은 '떨어뜨리다'라는 뜻을 가지지만 Git에서는 stack에서 작업내용을 삭제하는 용도로 쓰입니다.

이 뒤에 삭제하고 싶은 작업 내용의 id를 적으면 되는데요.

![image](https://user-images.githubusercontent.com/64893709/102711530-bbcf0d80-42fd-11eb-88ab-ac9dd94c8fe5.png)

이렇게 삭제가 잘 되었다는 메세지가 출력됩니다.

그리고 다시 리스트를 보면,

![image](https://user-images.githubusercontent.com/64893709/102711543-cdb0b080-42fd-11eb-8234-492fd9862542.png)

삭제된 결과물을 볼 수 있습니다.
