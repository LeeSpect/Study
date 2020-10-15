우선 MathTool이라는 repository를 만들어보겠습니다.

![1](https://user-images.githubusercontent.com/64893709/96124992-97863780-0f2e-11eb-9727-3865a1c12f9a.png)

이제 이 디렉토리 안으로 이동해보겠습니다.

![2](https://user-images.githubusercontent.com/64893709/96125425-c7cdd600-0f2e-11eb-8832-b2e552c5a8f6.png)

이제 이 안에서 프로젝트를 위한 각종 파일과 자식 디렉토리를 만들겁니다. 
그러면 이 MathTool 디렉토리가 프로젝트 디렉토리가 되는겁니다.   
그리고 Git으로 이 MathTool 디렉토리의 버전 관리를 시작할 건데요. 그러기 위해서는 아래와 같은 설정이 필요합니다.

![3](https://user-images.githubusercontent.com/64893709/96126551-1f6c4180-0f2f-11eb-89c5-d8e3ac304c9a.png)

위와 같이 git init을 치고 enter를 누르면 됩니다.  
여기서 git은 앞으로 우리가 git으로 어떤 작업을 할 때마다 써야하는 커멘드입니다. 이 git이라는 단어 뒤에 어떤 커멘드를 붙였으냐에 따라 하게되는 작업이 달라집니다.   
위에서는 git init를 통해 비어있는 repository를 생성했다는 뜻이 출력되었습니다. 여기서 repository는 앞서 배운 것처럼 프로젝트 디렉토리의 각 버전이 담기는 저장소입니다.   

이제 ls -al 명령어를 통해 어떤 변화가 생겼는지 보겠습니다.

![4](https://user-images.githubusercontent.com/64893709/96128045-ccdf5500-0f2f-11eb-8d78-d52ac43074c2.png)

이 .git이라는 디렉토리가 바로 레포지토리입니다.

.git 디렉토리 안으로 들어간 후 내부에 무엇이 있는지 살펴보겠습니다.

![5](https://user-images.githubusercontent.com/64893709/96131956-cacbc500-0f34-11eb-9c15-14d1b0c4ed8a.png)

여러가지 자식 디렉토리와 파일들이 보입니다.   
git은 프로젝트 디렉토리의 버전 관리를 하기 위해서 자신만의 규칙을 가지고 복잡한 작업을 처리합니다.   
위 사진에서 표시된 것들은 모두 그 작업을 하기 위해 사용되는 것들입니다.
