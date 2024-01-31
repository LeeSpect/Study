# 1. Deque 선언

```java
Deque que = new ArrayDeque(); // 타입 설정x
Deque<DequeDemo> demo = new ArrayDeque<DequeDemo>(); // DequeDemo 클래스 타입으로 선언
Deque<Integer> i = new ArrayDeque<Integer>(); // Integer 타입
Deque<Integer> i2 = new ArrayDeque<>(); // 뒷부분은 생략 가능
Deque<Integer> i3 = new ArrayDeque<Integer>(Arrays.asList(1, 2, 3, 4)); // 선언과 동시에 초기값 세팅
		
Deque<String> s = new ArrayDeque<String>(); // String 타입
Deque<Character> ch = new ArrayDeque<Character>(); // Char 타입
```

# 2. Deque 값 추가하기
```java
import java.util.ArrayDeque;
import java.util.Deque;

public class DequeDemo {
	public static void main(String[] args)  {
		Deque<String> deque = new ArrayDeque<String>(); // Deque 선언
		
		// 값 추가
		deque.addFirst("Hello");
		deque.offerFirst("Hello");
		deque.addLast("World");
		deque.offerLast("World");
		deque.add("Hello");
		
		System.out.print(deque); // 결과 출력
	}
}
```

- addFirst() : Deque의 맨 앞에 데이터를 삽입합니다. 용량을 초과하는 경우 Exception이 발생합니다
- offerFirst() : Deque의 맨 앞에 데이터를 삽입합니다. 용량을 초과하는 경우 false를 리턴해줍니다
- addLast() : Deque의 맨 뒤에 데이터를 삽입합니다. 용량을 초과하는 경우 Exception이 발생합니다
- offerLast() : Deque의 맨 뒤에 데이터를 삽입합니다. 용량을 초과하는 경우 false를 리턴해줍니다
- add() : addLast()와 동일합니다. 맨 뒤에 데이터를 삽입하고 용량을 초과하는 경우 Exception이 발생합니다

# 3. Deque 값 삭제하기
```java
import java.util.ArrayDeque;
import java.util.Deque;

public class DequeDemo {
	public static void main(String[] args)  {
		Deque<String> deque = new ArrayDeque<String>(); // Deque 선언
		
		// 값 추가
		deque.add("Hello1");
		deque.add("World2");
		deque.add("Hello3");
		deque.add("World4");	
		deque.add("Hello5");
		deque.add("World6");	
		deque.add("Hello7");
		deque.add("World8");	
						
		System.out.println(deque); // 결과 출력

		deque.removeFirst(); // 첫 번째 삭제
		System.out.println(deque); // 결과 출력

		deque.pollFirst(); // 첫 번째 삭제
		System.out.println(deque); // 결과 출력

		deque.remove(); // 첫 번째 삭제
		System.out.println(deque); // 결과 출력

		deque.poll(); // 첫 번째 삭제
		System.out.println(deque); // 결과 출력

		deque.removeLast(); // 마지막 삭제
		System.out.println(deque); // 결과 출력

		deque.pollLast(); // 마지막 삭제
		System.out.println(deque); // 결과 출력

		deque.remove("World6"); // 원하는 데이터 삭제
		System.out.println(deque); // 결과 출력

		deque.clear(); // 모두 삭제
		System.out.println(deque); // 결과 출력
	}
}
```

### remove와 poll차이점
- remove는 deque가 비어있다면 Exception을 출력
- poll은 deque가 비어있다면 null을 리턴합니다
 
마지막부터 순서대로 삭제하는 방법은 removeLast(), pollLast()가 있습니다
- remove는 deque가 비어있으면 Exception 출력
- poll은 null을 리턴
 
- remove(Object) 메서드를 사용하면 deque에서 Object를 찾아 삭제
- clear() 메서드를 사용하면 deque의 모든 데이터를 삭제

# 4. Deque 값 출력하기
```java
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Iterator;

public class DequeDemo {
	public static void main(String[] args)  {
		Deque<String> deque = new ArrayDeque<String>(); // Deque 선언
		
		// 값 추가
		deque.add("Hello1");
		deque.add("World2");
		deque.add("Hello3");
		deque.add("World4");	
		deque.add("Hello5");
		deque.add("World6");	
		deque.add("Hello7");
		deque.add("World8");	
						
		System.out.println("첫 번째 값 : " + deque.getFirst() + ", " + deque.peekFirst() + ", " + deque.peek());
		System.out.println("마지막 값 : " + deque.getLast() + ", " + deque.peekLast());		

		/* Iterator 클래스를 사용하여 값 출력 */
		Iterator iter = deque.iterator();
		
		while(iter.hasNext())
			System.out.print(iter.next() + " ");
	}
}
출처: https://crazykim2.tistory.com/581 [차근차근 개발일기+일상:티스토리]
```



출처: https://crazykim2.tistory.com/581 [차근차근 개발일기+일상:티스토리]
