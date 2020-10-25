이전 수업에서는 HEAD가 가리키고 있는 commit에 맞춰서 working directory의 내부가 구성된다는 것을 배웠습니다. 이 말이 무슨 말인지 조금 더 알아보도록 하겠습니다.   
우선 다시 commit history를 살펴보도록 하겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97106302-18e68280-1704-11eb-8911-13bea1199664.png)

지금 HEAD가 최신 commit을 가리키고 있습니다. 이 HEAD가 더 이전에 했던 commit을 가리키도록 해보겠습니다. 이때는 git reset을 사용합니다.   
우선 git reset을 입력하고 --hard라는 옵션을 줍니다. 그리고 한 칸을 띄운 후 가고 싶은 commit의 아이디를 써주면 됩니다.   
저는 최신 commit 바로 밑에 있는 Make README.md look nice 파일을 지정하도록 하겠습니다. 그리고 실행을 하면

![image](https://user-images.githubusercontent.com/64893709/97106473-2a7c5a00-1705-11eb-8e2b-b673a534c908.png)

실행이 잘 되었습니다. commit history를 다시 보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97106489-42ec7480-1705-11eb-9f3b-3a0856737ba6.png)

뭔가 달라졌습니다.

![image](https://user-images.githubusercontent.com/64893709/97106510-6a434180-1705-11eb-993c-8ea7cfad01fe.png)

원래 있던 ADD multiply function이 사라졌고 HEAD는 Make README.md look nice로 옮겨졌습니다.

그러면 HEAD가 가리키는 commit에 맞게 working directory의 내용도 바뀌었을까요? 다시 calculator.py 파일을 출력해보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97106530-965ec280-1705-11eb-9d87-90863bc4920e.png)

최근에 추가했었던 multiply 함수가 보이지 않습니다. Make README.md look nice가 작성되었을 때의 모습으로 돌아간 것입니다.

![image](https://user-images.githubusercontent.com/64893709/97106543-b8f0db80-1705-11eb-9322-a8c563029f8f.png)

git reset은 특정 시점 이후의 commit들이 전부 마음에 들지 않을 때 사용할 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/97106554-c7d78e00-1705-11eb-9fb7-7f61486978e0.png)
