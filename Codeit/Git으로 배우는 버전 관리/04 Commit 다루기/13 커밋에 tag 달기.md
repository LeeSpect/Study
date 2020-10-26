우리는 commit을 할 때 해당 commit에 관한 정보를 commit 메시지로 남기는데요.
그런데 commit 중에서는 다른 것들보다 좀더 중요한 의미가 있는 commit들도 있습니다.
이런 중요한 commit에는 commit 메시지뿐만 아니라 태그(tag)라는 것을 추가적으로 달기도 합니다.

보통 프로젝트에서 주요 버전의 시작점이 되는 commit에 이렇게 태그를 다는데요.
잠깐 아래 그림을 봅시다.
아래 그림에서 첫 번째 commit에는 Version 1이라는 태그를 달고,
여섯 번째 commit에는 Version 2라는 태그를 달고 싶다고 해봅시다.

![image](https://user-images.githubusercontent.com/64893709/97167713-a12f5b00-17ca-11eb-9a7b-1cf44dc22796.png)

아래와 같은 형식으로 태그를 달아줄 수 있는데요.
```
git tag [태그 이름] [커밋 아이디]
```
한번 해볼게요.

![image](https://user-images.githubusercontent.com/64893709/97167770-b99f7580-17ca-11eb-8427-84922662e857.png)

총 2개의 태그를 달았습니다.

그 다음에 이 프로젝트 디렉토리에 있는 모든 태그를 조회해볼게요.
```
git tag
```
라고 쓰면 됩니다. 실행해보면

![image](https://user-images.githubusercontent.com/64893709/97167828-d50a8080-17ca-11eb-9712-2f8bcd398b5a.png)

제가 추가했던 Version1, Version2 태그들이 보이죠?

그 다음 각 태그와 연결된 commit이 보고 싶으면,

```
git show [태그 이름]
```
의 형식으로 실행해주면 됩니다. 저는 Version_1 태그가 가리키는 commit을 살펴볼게요.

![image](https://user-images.githubusercontent.com/64893709/97167938-01260180-17cb-11eb-86b6-ae5ff184b0a2.png)

Version_1 태그에 연결된 커밋의 정보가 잘 보이죠? 이렇게 새 버전의 시작점이 되는 커밋처럼,
특히 그 의미가 중요한 커밋들은 이렇게 태그를 달아주면 나중에 프로젝트의 이력을 파악할 때 도움이 됩니다.
