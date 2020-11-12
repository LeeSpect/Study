머지(merge)에 관한 좀더 깊은 이야기를 해볼게요. merge를 하면 새로운 commit이 생긴다고 했습니다.

그리고 merge를 통해서 생겨난 commit을 머지 커밋(merge commit)이라고 부른다고 했는데요.

![image](https://user-images.githubusercontent.com/64893709/98935060-4ca81180-2526-11eb-9954-643fb7c10f17.png)

이 그림을 보면 지금 master branch에서 premium branch를 merge해서 검은색의 merge commit이 생긴 것을 알 수 있습니다.

하지만 merge를 한다고 항상 이렇게 새로운 commit이 생기는 건 아닙니다.

아래 그림를 보세요.

![image](https://user-images.githubusercontent.com/64893709/98935274-a01a5f80-2526-11eb-8831-6e6a45317d18.png)

지금 저는 master branch에 있죠? HEAD가 master branch를 가리키고 있으니까요. 이 상태에서
```
git merge premium
```
을 실행하면 어떻게 될까요?

그럼 이렇게 됩니다.

![image](https://user-images.githubusercontent.com/64893709/98935352-c17b4b80-2526-11eb-9559-0ee2cb64a97b.png)

premium branch가 가리키던 commit을, master commit도 똑같이 가리키게 되는데요. 지금 총 commit 수는 그대로죠?

이렇게 새로운 commit이 생기는 게 아니라 단지 branch가 이동하게 되는 merge를 __Fast-forward merge__ 라고 합니다. Fast-forward는 어떤 영상이나 소리를 __빨리감기__ (앞으로 감기)한다는 뜻인데요. 지금 master branch가 더 최신 commit으로 이동하는 모습이 꼭 빨리감기같죠?

어떤 경우에 이렇게 되는 걸까요?

commit history에서 같은 선(line) 상에 있는 branch를 merge할 때 Fast-forward merge가 이루어집니다. 방금 전에는 master branch와 premium branch가 둘다 같은 선 상에 있었죠? 바로 이런 경우입니다.

하지만 노트 초반부에서 봤던

![image](https://user-images.githubusercontent.com/64893709/98939690-28036800-252d-11eb-8911-dac1c3e45caf.png)

이 그림처럼 두 branch가, commit history 상에서 분리된 2개의 선에 각각 존재할 때 merge를 하면 merge commit이 새롭게 생기는 거구요. . 

그리고 이런 merge는 __3-way merge__ 라고 합니다. __이름이 3-way인 이유는 지금 1, 2, 3 표시한 3가지 커밋을 고려해서 머지를 하기 때문입니다.__ 지금 각각
* (1)번 : 두 갈래로 갈라지기 전 공통 조상이 되는 commit
* (2)번 : 한 branch가 가리키는 commit
* (3)번 : 다른 branch가 가리키는 commit

인데요. __3-way merge는 자신만의 방식을 갖고 이 3가지 commit을 기준으로 merge commit을 자동으로 만들어냅니다.__ 

그 방식에 대해서 간단하게 알려드릴게요. 아래 표에는 master branch와 premium branch를 merge했을 때 다양한 상황별로 그 결과가 정리되어 있는데요.

![image](https://user-images.githubusercontent.com/64893709/98941095-6732b880-252f-11eb-95b2-9cfd9e5b5a30.png)

각 컬럼(column, 열)에 대해서 설명할게요. 지금 모든 commit에 sample.txt 파일이 있다고 가정할게요.

1. __base__ : 두 branch의 공통 부모 commit의 sample.txt 파일의 내용 중 일부 = 위 그림 (1)번
2. __master__ : master branch의 최신 commit의 sample.txt 파일의 내용 중 일부 = 위 그림 (2)번
3. __premium__ : premium branch의 sample.txt 파일의 내용 중 일부 = 위 그림 (3)번
4. __merge 결과__ : master branch에서 premium branch를 merge했을 때의 최종 결과

자, 각각의 경우에 왜 표와 같은 merge 결과가 생기는 건지 설명해드릴게요.

__case1__

지금 base가 A이고, master는 A, premium은 B죠? 그럼 base를 기준으로 볼 때, master에서는 변화가 없었지만, premium에서는 A가 B로 변경된 상태입니다. __3-way merge는 base에서 변화가 발생한 것을 우선 채택__ 합니다. 그래서 merge 결과는 'B'가 됩니다.

__case2__

지금 base가 1이고, master는 2, premium은 1이죠? 이 경우에도 base에서 변화가 발생한 2가 merge 결과가 됩니다.

__case3__

지금 base가 "hello"이고, master는 "hello"를 삭제한 공백 상태, premium은 "hello"입니다. "hello"를 삭제해서 공백 상태가 된 것이 변화가 더 발생한 것이기 때문에 merge 결과는 공백이 됩니다.

__case4__

지금 base가 "bye", master가 "fighting", premium이 "please" 인데요. 지금은 이전 경우들과 좀 다르네요. 둘 다 base 때와는 다른 변화가 일어났는데요. 이렇게 두 브랜치에서 다 변화가 있을 때 Git은 어떤 변화를 선택해야할까요? 정답은 바로 ' __Git도 모른다!__ ' 입니다. 사실, 바로 이런 경우에 여러분이 배운 __Conflict가 발생__ 합니다. 이전에 Conflict가 발생했을 때 그것을 해결하고 머지를 마무리했던 거 기억나시죠? 바로 이런 경우였던 겁니다.

3-way merge가 어떤 방식으로 이루어지는지 아시겠죠?

* base때의 내용과 비교했을 때 달라진 부분이 있는 것이 우선시되고,
* 두 branch에서 둘다 변화가 일어났을 때는 Conflict를 발생시켜서 사용자가 스스로 선택하게끔 한다는 걸 기억하시면 됩니다.

자, 지금까지 merge에 대해서 좀 깊게 배워봤습니다. 방금 배운 내용을 다 기억하지 못하더라도

merge의 종류에는 크게
* Fast-forward merge
* 3-way merge

이렇게 두 가지 종류가 있다는 사실만큼은 꼭 기억하세요.

