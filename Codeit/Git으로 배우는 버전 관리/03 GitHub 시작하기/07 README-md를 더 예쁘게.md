보통 README.md 파일에는 

- 이 프로젝트가 어떤 프로젝트인지 설명하거나

- 프로그램의 주요 사용법을 알려주거나

- 프로그램을 실행시키려면 어떤 사전 작업이 필요한지를 알려주는 

내용들이 적혀있습니다. GitHub에서는 README.md 파일을 프로젝트의 메인 화면에 보여주기 때문에 README.md 파일의 내용을 가독성있게 작성하는 것이 중요한데요.

그러고보니 저도 MathTool 디렉토리에 README.md 파일을 추가했었죠? 잠깐 저의 README.md 파일을 살펴볼게요. 

![1](https://user-images.githubusercontent.com/64893709/96348791-47ea6c00-10e6-11eb-8557-987fbcb016a6.png)

그런데 저의 README.md 파일은 Numpy 프로젝트의 README.md 파일에 비해 뭔가 좀 초라하네요. 물론 내용 자체가 많지 않아서 그런 것도 있겠지만 딱히 뭔가 꾸며진 효과가 없어서 더 그렇게 보이는 건데요. 어떻게 하면 좀더 예쁘게 꾸밀 수 있을까요? 그 답은 README.md 파일의 확장자인 .md에 있습니다. 이 확장자는 markdown이라는 단어의 줄임말입니다.

markdown은 이 파일에 마크다운으로 내용을 작성할 수 있다는 걸 나타냅니다. 마크다운이란 특정 규칙에 맞게, 간단한 텍스트만으로 어떤 표시를 해두면, 그것이 자동으로 HTML 태그로 전환되도록 약속된 문법입니다. 그래서 단지 텍스트만으로도 내용의 디자인을 예쁘게 만들 수 있는데요. 마크다운이 정확히 뭔지 알고 싶으시면 이 위키피디아의 마크다운 문서를 참조하세요.

저는 마크다운을 활용해서 담백하게 생긴 저의 README.md 파일을 좀더 화려하게 만들어볼게요. 지금 저의 README.md 파일의 내용을 편집기로 보면 아래 그림과 같습니다.

![2](https://user-images.githubusercontent.com/64893709/96348842-a7487c00-10e6-11eb-9e54-002a74c3e5fa.png)

사실 ###(샵 3개)도 마크다운 중 하나입니다. 저렇게 쓰면 그 줄의 텍스트를 제목처럼 보이게 만들어주는 효과가 생기죠. 이렇게요.

![3](https://user-images.githubusercontent.com/64893709/96349677-0a88dd00-10ec-11eb-99aa-1824bf517a01.png)

자, 또다른 마크다운들도 추가해서 더 제대로 꾸며볼게요. 원래 내용을 아래 그림처럼 수정할게요.

![4](https://user-images.githubusercontent.com/64893709/96349716-5e93c180-10ec-11eb-86c5-c7662ea7a329.png)

그리고 이렇게 이 상태에서 "Make README.md look nice"라는 커밋 메시지로 커밋을 할게요. 

![5](https://user-images.githubusercontent.com/64893709/96349874-5be59c00-10ed-11eb-932f-1c3c5dbb6b11.png)

다시 README.md 파일을 보면

![6](https://user-images.githubusercontent.com/64893709/96349894-70c22f80-10ed-11eb-9278-44572a3738a4.png)

뭔가 미세하게 달라진 부분들이 생겼습니다. README.md 파일이 좀더 보기 편해졌죠? 제가 작성했던 #, *, - 이런 기호들이 마크다운에서 이미 정해진 의미를 갖고 있고, 그 의미에 맞게 시각적 효과가 더해진 건데요. 어떤 기호가 어떤 시각적 효과를 만들어냈는지는 여러분이 직접 비교해보면 좋을 것 같습니다.

그리고 GitHub에서 사용되는 이런 마크다운 언어의 규칙은 이 [링크](https://guides.github.com/features/mastering-markdown/)에 있으니, 관심이 있으신 분은 잘 읽어보세요. 코드잇에 있는 마크다운 관련 노트도 참고하시구요. 그리고나서 저와는 또다른 방식으로 README.md 파일을 화려하게 만들어도 좋습니다.

자, 방금 GitHub의 리모트 레포지토리에서 커밋을 했으니 이제 어떻게 해야할까요? 제 컴퓨터의 로컬 레포지토리에도 반영시켜야겠죠? 이전 영상에서 배운 git pull 커맨드를 실행할게요.

![image](https://user-images.githubusercontent.com/64893709/96350104-d82caf00-10ee-11eb-9863-dc58b87745ab.png)

이렇게 하면 remote repository의 최신 commit이 local repository에도 잘 반영됩니다.
