이전 영상에서는 __파일 하나__ 에서 conflict가 발생하는 상황을 봤습니다.
하지만 개발 실무에서는 파일 여러 개를 수정하는 경우가 많다보니 머지할 때 __conflict도 파일 여러 개에서__ 나는 경우가 많습니다. 이럴 땐 어떻게 해야할까요? 원리는 파일 하나일 때와 같습니다.

일단 아래 그림과 같은 프로젝트가 있다고 해볼게요.

![image](https://user-images.githubusercontent.com/64893709/97318798-96022b00-18af-11eb-9197-8f59e9ef13fd.png)

지금 빨간색 박스 안의 commit(세번째 commit)에서 어떤 상품의 정보를 담기 위한 
__파일 3가지(price, after_service, size)__ 를 만들었습니다. 

지금은 master branch나, premium branch나 그 history가 같죠?

이제 여기서부터 각 branch에서 서로 다르게 커밋을 해볼게요. 

master branch와 premium branch에서 __3가지 파일을 각각 서로 다르게 수정__ 하고 commit하겠습니다.
그 과정은 별도로 보여드리지 않고 생략할게요. 

그 다음 master branch에서 premium branch를 머지하려고 하면 

![image](https://user-images.githubusercontent.com/64893709/97319079-dfeb1100-18af-11eb-98ba-a2dfe0c9a11f.png)

위 그림처럼 3가지 파일 모두에서 conflict가 발생합니다.
꼭 이런 출력 결과가 아니더라도 이전에 우리가 배운 __git status__ 커맨드를 사용하면 현재 conflict가 발생한 파일들의 목록을 언제든지 확인할 수 있습니다. 

![image](https://user-images.githubusercontent.com/64893709/97319176-fabd8580-18af-11eb-881e-ff9d0a70d152.png)

자, 각 파일에서 conflict가 어떻게 났는지 하나씩 살펴볼까요? 

* price 파일

![image](https://user-images.githubusercontent.com/64893709/97319299-188aea80-18b0-11eb-9fbf-f54b2c774c69.png)

* after_service 파일 

![image](https://user-images.githubusercontent.com/64893709/97319368-280a3380-18b0-11eb-9ca7-c9f7133c7c08.png)

* size 파일

![image](https://user-images.githubusercontent.com/64893709/97319422-36584f80-18b0-11eb-9ffa-c3c5a9739799.png)

======= 기호를 기준으로
* master branch에서 했던 commit이 위쪽에,
* premium branch에서 했던 commit이 아래쪽에

보이는 상태입니다.

__일단 price 파일에서만__ conflict를 해결해볼게요.

![image](https://user-images.githubusercontent.com/64893709/97319845-98b15000-18b0-11eb-91cf-4476054be0d1.png)

이렇게 conflict를 해결하고, 

* git add price

를 실행하고, 

다시 git status로 확인을 해보면 

![image](https://user-images.githubusercontent.com/64893709/97319945-b1ba0100-18b0-11eb-8a5e-76d0ebac2737.png)

price 파일은 conflict를 해결하고 staging area에 올려주었기 때문에 commit할 수 있는 파일이라는 걸 확인할 수 있습니다.
이렇게 conflict가 해결된 상태를 __resolved(해결된) 상태__ 라고 말하기도 합니다.

자, 이제 나머지 두 파일(after_service, size)도 모두 conflict를 해결하고 나서, 늘 하던대로 

* git add .

를 실행하고 commit해주면 됩니다.

![image](https://user-images.githubusercontent.com/64893709/97320554-4290dc80-18b1-11eb-80ad-aee42353a822.png)

그럼 merge가 정상적으로 마무리됩니다! 

자, 여러 개의 파일에서 conflict가 발생했을 때도 앞으로 잘 해결할 수 있겠죠?
파일 여러개가 conflict가 났을 때는

* 파일 하나씩 conflict를 해결하고 git add [파일 이름] 커맨드로 하나씩 staging area에 올리거나(중간중간에 git status 커맨드로 현재 상태 확인하면서)
* 모든 파일들의 conflict를 다 해결하고, git add . 커맨드로 한번에 staging area에 올리고

commit을 하면 됩니다.
