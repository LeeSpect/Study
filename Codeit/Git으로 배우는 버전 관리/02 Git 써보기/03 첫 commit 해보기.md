이전 수업에서는 MathTool이라는 프로젝트 디렉토리를 만들었고 그 안에서 repository를 생성했습니다.   
.git 디렉토리에서 다시 MathTool 디렉토리로 돌아가 봅시다.

![1](https://user-images.githubusercontent.com/64893709/96137001-0b2c4280-0f37-11eb-9c7c-0cb9d3cfbea8.png)

MathTool 디렉토리에 파일 2개를 추가해보겠습니다.   
첫번째는 +와 - 함수를 제공하는 calculator.py 파일과 유료인지 무료인지를 나타내는 License 파일을 추가하겠습니다.

![2](https://user-images.githubusercontent.com/64893709/96139118-7aa33180-0f39-11eb-9500-4e6217a3f181.png)

위 상태를 MathTool 디렉토리의 첫번째 버전으로 남겨보겠습니다. 이럴 때 commit을 하면 됩니다.   
그런데 첫 commit을 하기 전에 꼭 해야할 것이 있습니다. 바로 깃에게 commit한 사람을 알려주는 것입니다.   

내가 누구인지를 Git에게 알려주려면 이름과 이메일 주소를 설정하면 됩니다.

그리고 이름을 설정하기 위해 한 칸 띈 후 user.name이라고 씁니다. 그리고"Leespect"이라고 덧붙이면 Leespect라는 이름이 설정됩니다.   
이메일도 비슷하게 설정합니다.

![3](https://user-images.githubusercontent.com/64893709/96141179-b939eb80-0f3b-11eb-9584-65d9bba5e1a5.png)

이제부터는 commit을 하면 이름과 이메일이 자동으로 저장될 것입니다.
여기서 config는 configure의 줄임말로, 설정하다, 구성하다의 뜻을 가지고 있습니다.   

그리고 commit을 할 때 git commit을 치고 바로 enter를 누르면 안 됩니다. commit을 할 때는 커밋에 대한 정보도 필요하기 때문입니다.

![4](https://user-images.githubusercontent.com/64893709/96141604-23529080-0f3c-11eb-8123-89491c289729.png)

즉 어떤 변동 사항이 생겨서 이런 commit을 하게 됐는지 등의 정보가 필요합니다.   
이런 정보를 '커밋 메시지'라고도 부릅니다. 이런 커밋 메시지를 남기려면 옵션이 필요합니다.

![5](https://user-images.githubusercontent.com/64893709/96142059-9a882480-0f3c-11eb-928d-a8a6814e7293.png)

우선 위처럼 옵션 -m을 한 후

![6](https://user-images.githubusercontent.com/64893709/96142847-7d078a80-0f3d-11eb-823d-9cd80962d190.png)

위처럼 큰 따옴표 안에 commit에 대한 정보를 을 씁니다. 이 내용을 잘 쓰는 것이 정말 중요합니다.   
강금 MathTool 디렉토리 안에 파일 2개를 추가했기 때문에 일단 위와 같이 써본 후 enter를 누르겠습니다.

![7](https://user-images.githubusercontent.com/64893709/96142861-8133a800-0f3d-11eb-9b47-aa5b0873ad2a.png)

위와 같은 오류가 나왔는데요. 우선 untracked는 깃에 의해 아직 추적되지 않고 있다라는 뜻입니다.   
아직 Git으로 무언가를 해준 적이 없어서 파일이 버전 관리 대상이 아닌 상태를 untracked라고 합니다.

![8](https://user-images.githubusercontent.com/64893709/96144199-e20fb000-0f3e-11eb-8f85-a303a688700c.png)

commit을 하기 전에는 commit할 파일을 미리 지정해줘야 합니다. 그러니까 파일을 새로 생성하거나 원래 있던 파일의 내용을 수정하고 
나면 그 파일들은 새로운 모습으로 commit에 포함될 것이라고 지정하는 것입니다. 이 작업을 해야 그 후에 commit을 할 수 있습니다.   
이런 사전 작업을 add라고 합니다. 

add를 하려면 다음과 같이 하면 됩니다.

![9](https://user-images.githubusercontent.com/64893709/96144793-8560c500-0f3f-11eb-9e98-108a2851b483.png)

이러면 calculattor.py 파일이 commit에 반영될 파일롤 지정되는 것입니다.

License도 add를 해준 후 commit을 해주면 다음과 같이 뜨는데요.

![11](https://user-images.githubusercontent.com/64893709/96147944-bbec0f00-0f42-11eb-8df8-6b96705a9200.png)

위 출력결과는 commit이 되었다는 뜻이고 그 결과를 보여주는 것입니다.   
그리고 root-commit이라는 말은 이 commit이 첫 번째 commit이라는 뜻입니다.

![10](https://user-images.githubusercontent.com/64893709/96147974-c4dce080-0f42-11eb-884f-72a6c9e39b88.png)
