지금 저희는 premium branch에 있는데요.   
master branch로 이동한 다음에 commit history를 살펴보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/98672400-16895700-2399-11eb-8a45-f19c56643ac3.png)

그런데 여기서 HEAD가 master branch를 가리키고 있네요. 여기 있는 이 화살표는 무슨 뜻일까요?

![image](https://user-images.githubusercontent.com/64893709/98672797-b515b800-2399-11eb-845b-67555ca7272f.png)

일단 HEAD는 어떤 commit을 가리키는 존재라고 배웠습니다. 그리고 branch는 우리가 프로젝트의 코드를 관리하는 하나하나의 흐름이고요.   
이 둘 사이에 무슨 관계가 있길래 화살표가 표시되는 걸까요?

이번 수업에서는 HEAD와 branch의 의미, 그리고 둘 사이의 관계에 대해서 제대로 짚고 넘어가겠습니다.

![image](https://user-images.githubusercontent.com/64893709/98673040-1c336c80-239a-11eb-87eb-fa9e35a890db.png)

먼저 branch를 생각해봅시다.   
branch는 프로젝트에서 코드를 관리하는 하나의 흐름이라고 배웠는데요. 뭔가 추상적인 느낌이 들죠? 이번에 정확하게 설명해드리겠습니다.   
사실 branch도 HEAD처럼 어떤 commit을 가리키는 존재인데요. 앞으로는 이렇게 commit을 가리키는 존재를 포인터라고 하겠습니다.

그림을 한번 볼까요?

![image](https://user-images.githubusercontent.com/64893709/98673470-ba273700-239a-11eb-919f-b242670f375c.png)

우리가 commit을 처음으로 하게 되면 master branch가 첫 번째 commit부터 시작해서 매번 새롭게 생기는 commit을 가리키게 됩니다.   
Git에서 commit은 이전 commit에 대한 정보를 가지고 있습니다. 그래서 master 포인터가 최신의 commit만 가리키고 있다고 해도 결국 그 이전 commit으로 하나씩  거슬러 올라갈 수 있기 때문에 지금까지 어떻게 프로젝트가 변해왔는지 추적할 수 있습니다.   
그래서 branch라는 것이 어떤 코드의 관리 흐름이라는 개념이 성립하는 겁니다.

![image](https://user-images.githubusercontent.com/64893709/98673681-0bcfc180-239b-11eb-886d-a743992b1f3b.png)

그럼 HEAD는 뭘까요? HEAD도 commit을 가리키는 포인터라고 배웠었죠? 그리고 HEAD가 가리키는 commit의 내용대로 working directory의 내용이 바뀐다고 했습니다.   
하지만 정확하게 말하자면, 보통 HEAD는 commit을 직접적으로 가리키지는 않습니다. HEAD는 보통 branch를 가리킬 뿐입니다.

![image](https://user-images.githubusercontent.com/64893709/98675177-3d498c80-239d-11eb-8e5e-dd720bd8d3c0.png)

결국 HEAD는 master branch를 통해 간접적으로 commit을 가리킵니다.

이제 이 상태에서 새로운 commit을 하면 master branch는 이제 다섯 번째 commit을 가리키게 됩니다.

![image](https://user-images.githubusercontent.com/64893709/98675332-75e96600-239d-11eb-8d7c-d65f366549d6.png)

HEAD는 여전히 master branch를 가리키고 있죠? 그래서 결국 HEAD도 다섯 번째 commit을 가리키게 되는 겁니다. 이게 바로 branch와 HEAD의 실제 모습입니다. 이 개념을 잘 이해하시면 Git에서 어려울 것이 없습니다.

이 상태에서 premium branch를 만들면 어떻게 될까요?

![image](https://user-images.githubusercontent.com/64893709/98675584-cb257780-239d-11eb-9d16-107031e4b6fc.png)

premium branch를 만들면 HEAD가 가리키던 commit을 premium branch가 가리키게 됩니다.

여기서 premium branch로 가면 어떻게 될까요? 

![image](https://user-images.githubusercontent.com/64893709/98675713-f90abc00-239d-11eb-9e51-92c4e3558cab.png)

다른 branch로 가는 커맨드는 git checkout이었죠. git checkout premium을 하면 HEAD가 premium branch를 가리킵니다.

이전에 코드의 관리 흐름이 master에서 premium branch로 바뀐다고 했던게 사실 이렇게 HEAD가 가리키는 branch를 변경하는 작업일 뿐이었던 겁니다. 

이 상태에서 제가 또 commit을 하면,

![image](https://user-images.githubusercontent.com/64893709/98676485-04121c00-239f-11eb-8d01-6a5b02f79970.png)

이렇게 여섯 번째 commit이 생기고 HEAD가 가리키던 premium branch가 이제 새로운 branch를 가리키게 됩니다.

이 상태에서 또 master branch로 checkout하면 어떻게 될까요.

![image](https://user-images.githubusercontent.com/64893709/98677562-818a5c00-23a0-11eb-8404-262cafc28845.png)

HEAD는 다시 master branch를 가리키게 됩니다.   
HEAD는 다시 다섯 번째 commit을 가리키게 되고 다섯 번째 commit의 내용대로 working directory도 바뀌게 됩니다.

그리고 여기서 다시 commit을 하면,

![image](https://user-images.githubusercontent.com/64893709/98677663-a5e63880-23a0-11eb-8317-865fc1a1fe5e.png)

이렇게 commit history의 흐름이 갈리집니다. 어려운 말로는 '분기한다'라고도 하는데요.

이제 이 상태에서 master branch에서도 몇 번 commit을 더 하고, premium branch에서도 몇 번 commit을 더 하면,

![image](https://user-images.githubusercontent.com/64893709/98677852-fcec0d80-23a0-11eb-910d-f040a501b2d9.png)

이런 모습이 되겠죠?

이제 우리가 배웠던 branch merge를 생각해 봅시다.   
지금 HEAD는 master branch를 가리키고 있는데요.   
이 상태에서 premium branch를 merge하면(git merge premium),

![image](https://user-images.githubusercontent.com/64893709/98678057-52281f00-23a1-11eb-8093-8f48d50426d4.png)

master branch에서 가리키던 commit의 내용에 premium branch에서 가리키던 내용을 합쳐서 새로운 commit을 만들어 주는 겁니다.

![image](https://user-images.githubusercontent.com/64893709/98678200-8c91bc00-23a1-11eb-88dc-d64e1de87a14.png)

이 때의 commit을 merge commit이라고 한다고 했죠?   
그러니까 merge는 결국 HEAD가 가리키던 commit에 다른 branch가 가리키던 commit을 합쳐서 새로운 commit을 만드는 작업인 겁니다.
