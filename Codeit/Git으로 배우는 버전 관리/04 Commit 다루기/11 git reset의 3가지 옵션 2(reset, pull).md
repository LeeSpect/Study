이번 수업에서는 git reset의 3가지 옵션인 --soft, --mixed, --hard의 차이를 직접 보여드리겠습니다.   
우선 서브라임으로 이동해서 calculator.py 파일을 수정하겠습니다.(생략)

다시 터미널로 이동한 다음에 git add .를 해주겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97144842-877d1c00-17a8-11eb-898a-ed23d9ed54e9.png)

지금 상태를 working directory와 staging area의 관점에서 생각해봅시다.   
일단 calculator.py 파일은 working directory에서 내용이 수정되어 있는 상태이고, staging area에도 역시 추가되어 있습니다.

staging area를 확인해보면,

![image](https://user-images.githubusercontent.com/64893709/97145010-d7f47980-17a8-11eb-933d-30adafed6603.png)

위처럼 claculator.py 파일이 잘 보입니다.

이 상태에서 commit history를 잠깐 살펴보겠습니다. 그리고 commit을 가리키기 위해서 commit에 번호를 붙여보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97145103-03776400-17a9-11eb-97f0-66a8b77078d3.png)

5번 commit이 최신 commit인데요. 현재 상태를 그림으로 나타내면 다음과 같습니다. 

![image](https://user-images.githubusercontent.com/64893709/97145216-30c41200-17a9-11eb-9845-3c848c93b8e0.png)

이제 --soft, --mixed, --hard 순으로 git reset을 해보겠습니다. 일단 5번 commit에서 4번 commit으로 reset을 해볼 건데요. 먼저 --soft 옵션을 사용하겠습니다.

우선 repository부터 살펴보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97145400-7d0f5200-17a9-11eb-89b0-53d566023961.png)

HEAD가 4번을 잘 가리키고 있습니다.   
그렇다면 working directory의 모습은 어떨까요.

![image](https://user-images.githubusercontent.com/64893709/97145600-cf507300-17a9-11eb-8328-17e177d411e5.png)

최근까지 작업했던 내용이 반영되어 있습니다. working directory는 --soft 옵션 reset의 영향을 받지 않았네요.   
이제 staging area도 살펴보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97148369-5dc6f380-17ae-11eb-89ee-51453d0b0131.png)

staging area도 reset의 영향을 받지 않았기 때문에 calculator.py 파일이 추가된 상태 그대로 있습니다.   
그런데 위의 git status 실행결과를 살펴보면,

![image](https://user-images.githubusercontent.com/64893709/97148497-9535a000-17ae-11eb-8681-905be3d1c089.png)

위와 같이 노란색으로 표시된 README.md 파일도 보이는데요. 아까 저는 calculator.py 파일만 수정해서 git add를 해줬기 때문에 staging area에는 calculator.py 파일만 있어야 할 것 같은데 왜 README.md 파일도 staging area에서 보이는 걸까요?

혹시 예전에 배웠던 내용 기억 나시나요? staging area에 한 번 올렸던 파일이 commit을 했다고 staging area에서 사라지는 것은 아니라고 했는데요.

![image](https://user-images.githubusercontent.com/64893709/97148790-0d9c6100-17af-11eb-9f73-e45d3e1f74bc.png)

잠깐 reset하기 전의 commit history를 보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97148941-49cfc180-17af-11eb-8ef8-a85041be6400.png)

5번 commit에는 Make README.md look nice라는 commit 메시지가 쓰여 있습니다.   
그렇다면 제가 4번 commit 이후에 README.md 파일을 수정하고(working directory) staging area에 추가했다는 뜻이겠죠.   
이렇게 한 번 staging area에 올려진 파일은 그 상태 그대로 남아있습니다.   
reset을 하기 전에는 5번 commit의 README 파일과 staging area의 README 파일 이 두 개가 똑같았습니다.
그래서 아까 강의 초반부에 git status를 했을 때는,

![image](https://user-images.githubusercontent.com/64893709/97149289-e3976e80-17af-11eb-9b26-58134fd49b65.png)

위처럼 calculator.py 파일만 보이고 README 파일이 출력되지 않은 것입니다.

하지만 reset을 한 후에는, 

![image](https://user-images.githubusercontent.com/64893709/97149538-3a9d4380-17b0-11eb-9c88-0816166d640f.png)

HEAD가 가리키는 4번 commit의 README 파일과 staging area의 README 파일에 차이가 생겼기 때문에,

![image](https://user-images.githubusercontent.com/64893709/97149579-48eb5f80-17b0-11eb-9490-278336da8050.png)

위처럼 README 파일도 staging area에서 보이는 것입니다.

이번엔 --mixed 옵션을 사용하겠습니다. 그 전에 일단 지금 상태를 확인해보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97149740-82bc6600-17b0-11eb-8acd-6c496bb56d1b.png)

이 상태의 4번 commit에서 3번 commit으로 reset을 해보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97149952-c911c500-17b0-11eb-9b57-1e35ccccfc52.png)

결과가 잘 출력되었습니다. 이 결과를 그림으로 살펴보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97150084-f6f70980-17b0-11eb-9dba-af4b32781446.png)

--soft 옵션 때와 달리 --mixed 옵션은 staging area도 reset 했습니다. 무슨 말인지 하나씩 확인해보겠습니다. 먼저 repository를 확인하면,

![image](https://user-images.githubusercontent.com/64893709/97150168-1726c880-17b1-11eb-9a68-cf186c7a691a.png)

HEAD가 3번 commit을 잘 가리키고 있습니다.   
그리고 working directory의 calculator.py를 살펴보면, 

![image](https://user-images.githubusercontent.com/64893709/97150272-39204b00-17b1-11eb-809e-22337bc109ec.png)

여전히 파일의 모습은 최신의 것 그대로입니다. working directory는 reset의 영향을 받지 않았습니다.   
하지만 git status를 보면,

![image](https://user-images.githubusercontent.com/64893709/97150475-80a6d700-17b1-11eb-897a-17b5cb00e515.png)

staging area를 살펴보면 Unstaged changes after reset 이라는 문장의 뜻처럼 변화가 생겼습니다. 이 문장의 뜻은 staging area에 있던 최신 파일들이 reset 때문에 staging area에서 내려왔다는 뜻입니다. 

마지막으로 --hard 옵션을 써보겠습니다. 우선 잠깐 지금 상황을 확인해보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97150717-e4310480-17b1-11eb-9772-1e132b3ac794.png)

이제 3번 commit에서 2번 commit으로 reset을 해보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97150821-088ce100-17b2-11eb-9cc4-a70098017cdb.png)

실행이 잘 되었습니다. 그림으로 살펴보면,

![image](https://user-images.githubusercontent.com/64893709/97150915-2c502700-17b2-11eb-94be-130035d4d3a3.png)

이젠 staging area 뿐만 아니라 working directory도 2번 commit처럼 변했습니다. 하나씩 살펴보겠습니다.   
먼저 repository를 확인해보면,

![image](https://user-images.githubusercontent.com/64893709/97151017-4ab62280-17b2-11eb-8969-3df0ca20fc50.png)

HEAD가 2번 commit을 잘 가리키고 있습니다.   
working directory도 보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97151139-6de0d200-17b2-11eb-977c-fdf634c80e7d.png)

새로 추가된 divide 함수가 사라졌습니다. reset이 working directory까지 영향을 미치고 있습니다.   
staging area도 살펴보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97151288-a97b9c00-17b2-11eb-9677-0851d1c23df6.png)

staging area도 2번 commit처럼 변했기 때문에 노란색으로 표시된 것처럼 아무것도 뜨지 않습니다.

이제 --hard 옵션이 얼마나 무서운지 감이 오시나요? 사실 staging area가 이전 commit처럼 변하는 것은 큰 문제가 아닙니다. 그냥 git add를 다시 해주면 되기 때문입니다.
하지만 --hard 옵션은 staging area 뿐만 아니라 working directory까지 이전 commit처럼 변화시킵니다. 그리고 이것은 심각한 문제를 일으킬 수도 있는데요.
여러분이 commit 이후로 작업했던 모든 내용이 다 날라가 버리기 때문입니다. 물론 정말 다 날려버리기 위해서 의도적으로 --hard 옵션을 사용한 것이라면 상관이 없지만, 이 옵션의 의미를 잘 모르고 썼다가는 큰일날 수 있으니 조심해야 합니다.

여기서 작업 내용을 다시 복구하고 싶을 때 어떻게 해야할까요? 이럴 때 GitHub에 올려뒀던 remote repository를 사용하면 됩니다. 저는 예전에 commit을 할 때마다 git push를 이용해서 local repository의 내용을 remote repository로 보냈었는데요.   
덕분에 그냥 이 상태에서 ```git pull```을 입력하면, HEAD가 최신 commit을 가리키던 예전의 상태, 즉 reset을 하기 전 상태로 돌아갈 수 있습니다.

![image](https://user-images.githubusercontent.com/64893709/97152090-c2d11800-17b3-11eb-90e2-b6139377d99b.png)

다시 commit history를 살펴보겠습니다.

![image](https://user-images.githubusercontent.com/64893709/97152151-d9776f00-17b3-11eb-8c6e-7b862fb3beae.png)

HEAD가 다시 최신 commit을 가리키고 있고 reset을 할 때 날렸던 내용들도 모두 복구가 되었습니다.
