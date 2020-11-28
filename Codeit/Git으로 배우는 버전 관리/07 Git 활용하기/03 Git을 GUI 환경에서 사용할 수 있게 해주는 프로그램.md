우리는 이때까지 **CLI(Command Line Interface)** 환경에서 Git을 사용해왔습니다.

하지만 **GUI(Graphic User Interface)** 환경에서 Git을 사용하도록 도와주는 프로그램도 있는데요. [GitKraken](https://www.gitkraken.com/?utm_expid=.W2nHbF0ARIqaOuS7QxW-pA.0&utm_referrer=https%3A%2F%2Fwww.google.com%2F), [Sourcetree](https://www.sourcetreeapp.com/) 등 다양한 프로그램들이 있습니다.

이 중에서도 꽤 널리 쓰이고 있는 **Sourcetree**의 사용방법을 간단히 보여드릴게요.

Sourcetree는 Atlassian이라는 회사에서 만든 프로그램으로 깔끔하고 직관적인 UI로 유명한데요.

한번 사용해보겠습니다.

## 1. Sourcetree 설치하기

1> 먼저 [Sourcetree 다운로드 페이지](https://www.sourcetreeapp.com/)로 가서 Download for Mac OS X 버튼을 클릭할게요.

![image](https://user-images.githubusercontent.com/64893709/100514193-06a1ad80-31b6-11eb-968e-5acf4305f5c2.png)

2> 그런 다음 약관에 동의하고 Download 버튼을 누를게요.

![image](https://user-images.githubusercontent.com/64893709/100514212-15886000-31b6-11eb-9814-8ece30ccdbf4.png)

3> zip 파일 하나가 다운로드되었습니다.

![image](https://user-images.githubusercontent.com/64893709/100514219-1faa5e80-31b6-11eb-937c-5a7a96a2345c.png)

4> zip 파일의 압축을 풀고나니, Sourcetree 아이콘이 보이는데요. Sourcetree 아이콘을 클릭하겠습니다.

![image](https://user-images.githubusercontent.com/64893709/100514231-38b30f80-31b6-11eb-849b-5f96f278452f.png)

5> 그 다음 뜨는 알림창에서 실행 허용을 해줄게요.

![image](https://user-images.githubusercontent.com/64893709/100514235-449ed180-31b6-11eb-9f38-5b30509623d6.png)

6> 그리고 Sourcetree를 Application 디렉토리로 옮기겠습니다.

![image](https://user-images.githubusercontent.com/64893709/100514266-829bf580-31b6-11eb-9ce7-6744e8a48a1b.png)

7> 자, 그럼 이렇게 Sourcetree 화면이 뜹니다. 여기서부터는 제가 직접

* 새로운 local repository를 만들 수도 있고,
* 원래 있던 local repository를 import할 수도 있습니다.

저는 이때까지 작업을 해온 **MathTool이라는 로컬 레포지토리**가 있으니까 이걸 임포트해볼게요. 

![image](https://user-images.githubusercontent.com/64893709/100514289-c262dd00-31b6-11eb-96a0-2ba9b765a96c.png)

8> '새로 만들기' 버튼을 눌러서 ‘로컬 저장소 추가하기’ 버튼을 클릭할게요. 

![image](https://user-images.githubusercontent.com/64893709/100514299-cdb60880-31b6-11eb-8fa0-5bb8c8f71e45.png)

9> 그 다음 뜨는 Finder 창에서 MathTool 디렉토리를 선택하고 열기를 누르겠습니다. 

![image](https://user-images.githubusercontent.com/64893709/100514301-d9093400-31b6-11eb-87c2-a966ea8d0fa1.png)

10> 그럼 MathTool 디렉토리가 Sourcetree에 뜹니다. 여기서 MathTool을 클릭하면 

![image](https://user-images.githubusercontent.com/64893709/100514308-e58d8c80-31b6-11eb-9d62-93d76f8d1a9d.png)

11> 이렇게 Sourcetree가 MathTool 디렉토리를 분석해서 준비한 화면이 나타나는데요. 화면을 자세히 보면 우리가 이때까지 배웠던 용어들을 볼 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/100514315-f211e500-31b6-11eb-9680-82b3118fab53.png)

화면의 각 영역에 대해서 간단하게 설명하면 다음과 같습니다.

(1) : 아이콘을 클릭해서 커밋, 풀, 푸시 등의 작업을 할 수 있는 영역

(2) : 커밋 히스토리를 그래픽적으로 보여주는 영역(커밋 히스토리를 깔끔하게 보여주는 장점 때문에 이런 프로그램을 사용하는 경우가 많습니다.)

(3) : 커밋 히스토리 중에서 파란색으로 활성화된 커밋에 대한 정보를 보여주는 영역(해당 커밋 당시 생성되거나 수정된 파일 목록입니다.) 

(4) : 커밋 히스토리 중에서 파란색으로 활성화된 커밋에 관해 '커밋을 한 사람, 커밋 메시지, 커밋 일시' 등의 정보를 보여주는 영역

(5) : (3)에서 선택한 파일의 구체적인 수정 내용을 보여주는 영역

자, 이제 Sourcetree 화면의 각 영역에 대해 살펴봤으니 이 프로그램을 어떻게 사용할 수 있는지도 간단하게 알아볼게요.

## 2 Sourcetree의 기능 간단히 살펴보기

Sourcetree는 누구나 그래픽 요소(아이콘, 설명 등)만 보고도 바로 사용할 수 있을 정도로 직관적인 UI(User Interface)를 갖고 있습니다. 간단히 몇 가지 기능만 보여드릴게요. 

(1) **커밋(commit)하기** : 어떤 파일을 생성하거나 수정하고 나서 Sourcetree에서 커밋 메시지를 입력하고 커밋할 수 있습니다. 

![image](https://user-images.githubusercontent.com/64893709/100514343-31d8cc80-31b7-11eb-9a4d-b3d2e6bd4c47.png)

(2) **풀(pull)하기** : 리모트 레포지토리의 내용을 로컬 레포지토리로 가져와서 머지할 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/100514351-3ef5bb80-31b7-11eb-9234-dfaf2cafbbc4.png)

(3) **푸시(push)하기** : 로컬 레포지토리의 내용을 리모트 레포지토리로 보낼 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/100514357-53d24f00-31b7-11eb-9474-f2979c6235a0.png)

(4) **페치(fetch)하기** : 리모트 레포지토리의 내용을 로컬 레포지토리로 가져올 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/100517248-9bafa100-31cc-11eb-87f9-a7dcfbd9da56.png)

(5) **브랜치(branch) 생성하기** : 새로운 브랜치를 생성할 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/100517258-b255f800-31cc-11eb-90e5-ae2990fe9d8d.png)

(6) **브랜치 병합(merge)하기** : 현재 브랜치에서 다른 브랜치를 머지(merge)할 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/100517476-0a412e80-31ce-11eb-9372-d0a9bac964ac.png)

(7) **커밋 메시지를 기준으로 커밋 검색(search)하기** : 커밋 메시지에 관한 키워드 검색으로 특정 커밋을 찾을 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/100517485-1cbb6800-31ce-11eb-97d0-94884a58b0c6.png)

(8) **브랜치 변경(checkout) 하기** : 다른 브랜치로 이동할 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/100517538-80de2c00-31ce-11eb-9c7d-fc7cb233b475.png)

(9) **리모트 레포지토리의 브랜치 살펴보기** : 리모트 레포지토리에 있는 브랜치들도 살펴볼 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/100517548-8dfb1b00-31ce-11eb-8cf4-aa96021af064.png)

Sourcetree의 기능 몇 가지를 살펴보았는데요. 이때까지 다 저희가 배웠던 기능들입니다. 

**이런 GUI 프로그램을 사용하면 터미널에 Git 커맨드를 치지 않아도 Git을 사용할 수 있습니다. CLI 환경에서 필요했던 커맨드를 몰라도 Git을 사용할 수 있다는 뜻입니다.**

이뿐만 아니라 **commit history를 아래 그림처럼 터미널에서 봤던 commit history보다 더 깔끔한 모습으로 볼 수 있다는 장점도 있습니다.**

![image](https://user-images.githubusercontent.com/64893709/100517562-b7b44200-31ce-11eb-8039-489215f5a6a7.png)

하지만 아직 Git 커맨드를 사용하는 방법도 모르는데 바로 이런 프로그램을 사용하는 건 좋지 않습니다. 일단 커맨드부터 하나씩 배워야 나중에 이런 프로그램을 사용하다가 문제가 생기더라도 현명하게 대처할 수 있습니다.

여러분이 이 Git 토픽을 전부 다 마치고나서, 어느 정도 Git 커맨드에 익숙해진다면 그 후에는 Sourcetree같은 GUI 프로그램도 한번 사용해보세요. 

이번 노트에서 배운 Sourcetree는 실무에서도 많이 쓰이는 프로그램입니다. 혹시 Sourcetree를 좀더 제대로 배우고 싶으면 이 [튜토리얼 문서](https://confluence.atlassian.com/bitbucket/tutorial-learn-bitbucket-with-sourcetree-760120235.html)를 참고하세요. 

그리고 만약 다른 GUI 프로그램을 사용하고 싶으면 [이 링크](https://git-scm.com/downloads/guis)를 클릭해서 나오는 프로그램 중에 자신이 원하는 것을 설치해서 쓰셔도 됩니다. 
