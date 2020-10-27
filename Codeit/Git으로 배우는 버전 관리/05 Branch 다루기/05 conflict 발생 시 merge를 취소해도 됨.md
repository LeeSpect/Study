이전 영상에서는 premium 브랜치에서 master 브랜치를 머지(merge)하다가 __Conflict__ 가 발생했고, 저는 그것을 해결하고 머지에 성공했습니다.

하지만 꼭 이렇게 Conflict를 해결하지 않고, 일단 merge 자체를 취소하는 방법도 있습니다. 

이전 영상에서 머지하려다가 아래 그림처럼 Conflict가 났을 때 

![image](https://user-images.githubusercontent.com/64893709/97314781-63563380-18ab-11eb-943a-6b700f1e40f7.png)

__calculator.py__ 파일의 모습은 이랬습니다. 

![image](https://user-images.githubusercontent.com/64893709/97314844-7406a980-18ab-11eb-8b12-bac1187a5377.png)

저는 이전 영상에서 이때 
* Conflict가 발생한 빨간 박스 부분을 다 삭제하고
* 제가 merge의 결과로 원하는 모습대로 코드를 수정한 다음(divide_new 함수 추가)
* commit을 함으로써 문제를 해결했는데요.

꼭 이렇게 Conflict를 해결하지 않아도 됩니다.

머지를 시도하기 이전의 상태로 돌아가고 싶다면 그냥 머지 자체를 취소하는 방법도 있는데요. 

머지 작업을 취소하려면
```
git merge --abort
```
라고 쓰면 됩니다. --abort는 우리말로 '버리다, 취소하다'라는 뜻입니다.

아래 그림처럼 이 커맨드를 실행하고 

![image](https://user-images.githubusercontent.com/64893709/97315045-a31d1b00-18ab-11eb-893c-7ef218fbb7fd.png)

다시 calculator.py 파일을 보면

![image](https://user-images.githubusercontent.com/64893709/97315076-afa17380-18ab-11eb-8bd0-0b7741b4d8cf.png)

Conflict 표시가 말끔히 사라지고 __premium 브랜치에 있던 calculator.py의 원래 모습 그대로 즉, 머지를 시도하기 이전 모습__ 으로 돌아옵니다.

자, 정리할게요! 만약 꼭 머지를 해야하는 상황이라면 이전 영상에서 봤던 것처럼 Conflict를 해결하고 커밋을 하는 게 정석입니다. 

하지만 
*  Conflict가 발생한 파일들이 너무 많아서 conflict를 최소화할 수 있는 방식으로 파일들을 다시 수정하고 commit한 다음에 merge를 하고 싶다거나
* 그냥 좀더 나중에 merge하고 싶을 때라면

방금처럼 그냥 머지 자체를 취소해도 됩니다.
