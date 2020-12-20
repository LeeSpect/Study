이번에는 premium branch에서 get_Abs 라는 함수를 추가해보겠습니다.   
(생략) 먼저 서브라임 텍스트로 이동해주세요.
get_Abs 함수는 어떤 수의 절대값을 구해주는 함수입니다.

이렇게 코드를 하는 중에 회사에서 긴급 공지가 내려왔다고 해봅시다.   
갑자기 무료 버전의 라이센스 정보를 빨리 수정하라는 공지가 떴다고 해봅시다.

![image](https://user-images.githubusercontent.com/64893709/102707341-6c78e500-42dd-11eb-865e-527db29c5040.png)

아직 get_Abs 함수를 다 완성하지도 못했지만 빨리 master branch로 가서 작업을 해야할 것 같습니다.

지금까지 쓴 내용을 저장한 다음에 터미널로 이동해주세요.

터미널로 이동하셨으면 master branch로 가봅시다.

![image](https://user-images.githubusercontent.com/64893709/102707377-bb267f00-42dd-11eb-83ef-770f6640e418.png)

그런데 위에서 노란색으로 표시된 것처럼 에러가 하나 떴습니다.   
이 에러 메세지를 해석하면, 제가 지금 바로 다른 branch로 가버리면 방금까지 작업한 내용이 날라갈 수도 있다는 뜻입니다.

![image](https://user-images.githubusercontent.com/64893709/102707390-d8f3e400-42dd-11eb-8139-e699ff463e7d.png)

그러니까 제가 위 상태에서 master branch로 체크아웃을 하면,

![image](https://user-images.githubusercontent.com/64893709/102707427-2a9c6e80-42de-11eb-9342-10040be0579f.png)

HEAD가 master branch를 통해 새로운 commit을 가리키게 됩니다.   
그럼 working directory의 내부도 그 commit의 내용대로 바뀌죠?

그러니까 방금 제가 작업한 내용이 모두 사라질 수 있기 때문에 이런 에러가 뜨는 겁니다.

이런 상황을 위해서 꼭 알아야 할 커맨드가 있는데요.

```git stash```라는 커맨드입니다.

![image](https://user-images.githubusercontent.com/64893709/102707469-82d37080-42de-11eb-8a0a-e13ac419d38e.png)

stash는 우리말로 안전한 곳에 보관하다, 넣어두다. 이런 뜻을 가지고 있습니다.

git stash를 실행하면 working directory에서 작업하던 내용을 Git이 따로 보관해 줍니다.   
그리고 이때 보관하는 장소를 ```stack```이라고 합니다.   
이 stack은 사실 어떤 데이터를 저장하는 구조를 말합니다.

먼저 넣은 자료일수록 다시 꺼낼 때 가장 마지막에 꺼내지는 구조를 stack이라고 합니다.

![image](https://user-images.githubusercontent.com/64893709/102707485-bd3d0d80-42de-11eb-9099-6d5bd38752a8.png)

git stash를 하면 가장 먼저 저장했던 작업 내용이 가장 아래에 저장되는 구조인데요.

그러면 다시 꺼낼 때 가장 나중에 꺼내지겠죠? 그리고 이런 자료구조를 stack이라고 하고요.

그러면 git stash를 실행해보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/102707510-fb3a3180-42de-11eb-9c44-2fb4ba00c17a.png)

위에서 노란색으로 표시된 것처럼 뭔가 출력되었습니다. 이 말은 제가 작업한 내용을 stack에 잘 저장했다는 뜻인데요.

stack에 저장이 잘 됐는지 보려면 ```git stash``` 뒤에 한 칸을 띄우고 ```list```를 입력하면 됩니다. 실행하면,

![image](https://user-images.githubusercontent.com/64893709/102707537-38062880-42df-11eb-8a84-aa36b1f91dd1.png)

제가 작업했던 내용이 stack에 잘 들어가 있다는 것을 알 수 있습니다.

그리고 다시 calculator.py 파일을 보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/102707547-566c2400-42df-11eb-9785-d534b23bdfd9.png)

그러면 get_Abs 함수를 추가하기 전 모습으로 돌아와 있습니다.

![image](https://user-images.githubusercontent.com/64893709/102707560-8287a500-42df-11eb-93b1-a7c30f164312.png)

git stash를 하면 최근 commit 이후로 작업했던 내용은 모두 stack에 옮겨지고 working directory 내부는 다시 최근 commit의 상태로 초기화됩니다.

작업한 내용은 어차피 stack에 저장되어 있기 때문에 걱정하지 않으셔도 됩니다.

다시 터미널로 이동할게요.

git stash를 했기 때문에 이제 master branch로 갈 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/102707573-a814ae80-42df-11eb-8029-9d39c538986f.png)

그리고 서브라임 텍스트로 이동해 보겠습니다.
그리고 라이센스 파일을 수정해주겠습니다.

![image](https://user-images.githubusercontent.com/64893709/102707598-c7134080-42df-11eb-96bc-6c0ba921f16d.png)

저장을 하고 다시 커맨드로 이동해서 commit을 해주겠습니다.

![image](https://user-images.githubusercontent.com/64893709/102707609-ead68680-42df-11eb-8cc8-fb02a49e5fa1.png)

다시 premium branch로 이동해 보겠습니다. 급한 불은 껐으니까 이제 원래 하던 작업을 마무리하러 가겠습니다.

![image](https://user-images.githubusercontent.com/64893709/102707634-0c377280-42e0-11eb-8969-cf872382d48f.png)

이제 stack에 저장했던 내용을 불러오겠습니다.

불러오려면 git stash 다음에 한 칸 띄고 ```apply```를 입력하면 되는데요. apply는 적용하다라는 뜻을 가지고 있습니다.

![image](https://user-images.githubusercontent.com/64893709/102707666-46a10f80-42e0-11eb-97d5-ba47969bc283.png)

실행을 하고 다시 calculator.py 파일을 열어보면 제가 아까 작업하던 내용이 그대로 복구되었습니다.

( 생략 ) 마저 작업을 완성하고 저장한 후 터미널로 이동하여 commit을 하겠습니다.

![image](https://user-images.githubusercontent.com/64893709/102707705-a1d30200-42e0-11eb-81e6-b0eec6861e8e.png)

![image](https://user-images.githubusercontent.com/64893709/102707712-b6af9580-42e0-11eb-9d47-fc2af13c92d6.png)

git stash는 어떤 branch에서 하던 작업을 아직 commit하지 않았는데 다른 branch로 가야하는 상황에서,
작업 중이던 내용을 잠깐 저장하고 싶을 때 사용합니다.
