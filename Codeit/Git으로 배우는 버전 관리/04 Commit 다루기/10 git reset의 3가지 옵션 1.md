이전 수업에서는 git reset을 써서 HEAD가 과거의 commit을 가리키게 했습니다.
그리고 이때 --hard라는 옵션을 사용했습니다. 사실 git reset에는 그 외에도 --soft, --mixed라는 옵션이라는 옵션이 있습니다.   
이 옵션들의 차이를 이해하려면 Git의 3가지 작업 영역을 잘 이해하고 있어야 합니다.

Git의 3가지 작업 영역은 working directory, staging area, repository였습니다. 혹시 기억이 안 난다면 2번째 챕터에 있는 'Git의 3가지 작업 영역'을 보고 옵시다.   
Git의 3가지 작업 영역을 알아야 하는 이유는 --soft, --mixed, --hard 중 어떤 옵션을 쓰느냐에 따라 어떤 작업 영역들이 reset되는지가 달라지기 때문입니다.

표를 한번 보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97107271-053e1a80-170a-11eb-85b9-f4f877c47bea.png)

이 표는 git reset 뒤에 옵션을 쓴 다음 제가 했던 특정 commit의 아이디 앞부분, 예를 들어 eea5를 적은 상황을 나타냅니다.   
옵션 별로 결과를 살펴보겠습니다.

먼저 --hard 옵션부터 보겠습니다.   
가장 오른쪽의 repository부터 보겠습니다. --hard 옵션을 쓰면 repository에서는 HEAD가 eea5 commit을 가리키게 됩니다.

![image](https://user-images.githubusercontent.com/64893709/97107411-b6dd4b80-170a-11eb-8b46-b72311b4e1ad.png)

그리고 staging area도 eea5 commit의 모습처럼 변합니다.

![image](https://user-images.githubusercontent.com/64893709/97107441-e68c5380-170a-11eb-8c2d-14e65fb2879d.png)

working directory의 경우에도 eea5의 모습처럼 바뀝니다.

![image](https://user-images.githubusercontent.com/64893709/97107451-f6a43300-170a-11eb-9b24-82554a82832a.png)

##### 즉 --hard 옵션은 eea5 commit을 한 이후로 working directory에서 했던 작업이 모두 사라져 버린다는 뜻입니다. 

이제 --mixed 옵션을 살펴보겠습니다. 여기부터는 조금 더 집중하셔야 합니다.   
--mixed 옵션에서도 repository가 eea5 commit을 가리킨다는 점은 같습니다.

![image](https://user-images.githubusercontent.com/64893709/97107507-539fe900-170b-11eb-85a9-86b62cb544f8.png)

그리고 staging area가 eea5 commit처럼 바뀌는 것도 같습니다.

![image](https://user-images.githubusercontent.com/64893709/97107527-6f0af400-170b-11eb-8807-4ed71b11c394.png)

하지만 --hard 옵션 때와는 다르게 --mixed 옵션에서 working directory의 모습은 바뀌지 않습니다.

![image](https://user-images.githubusercontent.com/64893709/97107565-9c57a200-170b-11eb-922b-f063ac9f102d.png)

##### 그러니까 repository에서 HEAD가 eea5 commit을 가리키고 있더라도 working directory는 가장 최근에 작업했던 모습 그대로라는 뜻입니다.   
이점이 아주 중요하니까 꼭 기억해 두세요.

마지막으로 --soft 옵션도 보겠습니다.   
--soft 옵션도 repostory에서는 HEAD가 eea5 commit을 가리키게 되지만,

![image](https://user-images.githubusercontent.com/64893709/97107626-dd4fb680-170b-11eb-8cff-14075d95261b.png)

staging area와 working directory는 아무런 변화 없이 최근에 작업했던 모습 그대로 남아 있습니다.

![image](https://user-images.githubusercontent.com/64893709/97107659-0708dd80-170c-11eb-8d45-d6ba3945f328.png)

정리하자면 --hard, --mixed, --soft 옵션은 Git의 3가지 작업 영역 중 몇 개의 영역까지 reset을 하느냐에 따라서 구분됩니다.

--hard는 표현 그대로 hard하게 모든 영역을 reset해 버리고,   
--mixed는 중간 정도로 2개의 영역 정도만 reset,   
--soft는 한 개의 영역만 reset하는 겁니다.

사실 --hard 옵션은 별로 권장되지 않습니다. 왜냐하면 commit 이후로 working directory에서 했던 내용들이 다 사라지고 복구를 할 수 없기 때문입니다.   
commit 이후로 했던 작업들이 전부 사라져도 상관 없을 때만 --hard 옵션을 쓰고 보통은 --soft 옵션이나 --mixed 옵션을 쓰는 것이 좋습니다.

![image](https://user-images.githubusercontent.com/64893709/97107834-f311ab80-170c-11eb-8763-8e544d1b8358.png)

