![image](https://user-images.githubusercontent.com/64893709/131237542-1d2c9af9-983c-438c-8e4a-d80fc6c9e5d0.png)

HTML은 사이트의 내용을 담고 CSS는 그 내용의 스타일링을 맡는다.

![image](https://user-images.githubusercontent.com/64893709/131237665-44e568c8-c0f1-4374-8591-990a2b4746c8.png)

이것은 CSS의 기본 문법입니다.   
우선 스타일링 하고 싶은 요소를 써야 합니다.   
저는 페이지에 있는 모든 h1 태그를 꾸미도록 하겠습니다.

그리고 중괄호 사이에 바꾸고 싶은 속성을 써주고 콜론을 쓰고   
원하는 값을 쓰고 세미콜론으로 끝내 주면 됩니다.   
이 경우에는 h1의 폰트 사이즈를 64px로 설정하고 h1의 글을 가운데 정렬하는 거곘죠.

이제 우리 사이트의 스타일을 입히겠습니다.

![image](https://user-images.githubusercontent.com/64893709/131237678-07222edd-d657-4ae4-9cf3-3aae845b0cc8.png)

CSS를 써 주기 위해서 여기 밑에 style 태그를 써주세요.   
이 사이에 CSS 코드를 써주면 사이트에 스타일이 반영됩니다.   

![image](https://user-images.githubusercontent.com/64893709/131237693-b33ba6ea-3ae7-4537-8413-3b4c1a675ab4.png)

먼저 h1 태그에 스타일을 입혀 보겠습니다.   
h1을 쓰고 중괄호 열고 닫고 폰트 크기를 64px로 설정하겠습니다. 그리고 가운데 정렬도 하고.   
여기서 align은 정렬이라는 뜻입니다.

여기는 들여 쓰기를 해주시고   
콜론(:) 뒤에만 띄어쓰기를 한 칸 해주시고 세미콜론(;)을 꼭 써주세요.   
저장하고 새로고침해보면 폰트가 커져있고 가운데 정렬이 되었습니다.

이번에는 이 위에 100px의 간격을 주도록 하겠습니다.

![image](https://user-images.githubusercontent.com/64893709/131237710-fe8b7689-064a-4fb0-b75c-8bfd81c36b5d.png)

그러면 이렇게 h3에 margin-top: 100px;   
여기서 margin은 여백이라는 듯이니까, h3 위에 100px의 여백을 주라는 겁니다.   
저장하고 다시 새로고침하면 여백이 생겼습니다.

![image](https://user-images.githubusercontent.com/64893709/131237729-f89dc858-5886-49c7-9b29-7ad6da347df5.png)

마지막으로 폰트를 키워 보겠습니다.   
i 태그니까 `i (font-size: 48px;)` 이렇게 하고 새로고침을 하면 커지는데, love도 커졌습니다.

우리가 키우고 싶은 폰트는 p 안에 있는 i 태그입니다.   
그럼 여기에 그냥 i 대신 p 띄고 i 이렇게 써 주시면, p 태그 안에 있는 i 태그만 스타일링 해주겠다는 뜻입니다.
