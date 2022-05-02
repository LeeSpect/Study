Set 자료형에는 HashSet, TreeSet, LinkedHashSet 등의 Set 인터페이스를 구현한 자료형이 있다.
여기서 말하는 Set 자료형은 인터페이스인데 인터페이스에 대해서는 뒤에서 자세히 다루도록 한다.

# 생성
집합 자료형은 HashSet을 사용하여 만들 수 있다.
```java
import java.util.Arrays;
import java.util.HashSet;

public class Sample {
    public static void main(String[] args) {
        HashSet<String> set = new HashSet<>(Arrays.asList("H", "e", "l", "l", "o"));
        System.out.println(set);   // [e, H, l, o] 출력
```

# 집합 자료형의 특징
* 중복을 허용하지 않는다.
* 순서가 없다.(Unordered)

# 교집합, 합집합, 차집합 구하기

다음과 같이 2개의 집합 자료형을 만든 후 따라 해보자. s1은 1부터 6까지의 값을 가지게 되었고, s2는 4부터 9까지의 값을 가지게 되었다.
```java
import java.util.Arrays;
import java.util.HashSet;

public class Sample {
    public static void main(String[] args) {
        HashSet<Integer> s1 = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5, 6));
        HashSet<Integer> s2 = new HashSet<>(Arrays.asList(4, 5, 6, 7, 8, 9));
    }
}
```
※ 제네릭스로 int를 사용하고 싶은 경우에는 int의 Wrapper 클래스인 Integer를 대신 사용해야 한다.

## 1. 교집합 (retainAll)
```java
import java.util.Arrays;
import java.util.HashSet;

public class Sample {
    public static void main(String[] args) {
        HashSet<Integer> s1 = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5, 6));
        HaseSet<Integer> s2 = new HashSet<>(Arrays.asList(4, 5, 6, 7, 8, 9));
      
        HashSet<Integer> intersection = new HashSet<>(s1);   // s1으로 intersection 생성
        intersection.retainAll(s2);   // 교집합 수행
        System.out.println(intersection);   // [4, 5, 6] 출력
    }
}
```
s1의 데이터를 유지하기 위해 s1으로 intersection이라는 HashSet 객체를 Copy하여 생성하였다.
만약 intersection 대신 s1에 retainAll 메소드를 사용하면 s1의 내용이 변경될 것이다.

## 2. 합집합 (addAll)
```java
import java.util.Arrays;
import java.util.HashSet;

public class Sample {
    public static void main(String[] args) {
        HashSet<Integer> s1 = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5, 6));
        HashSet<Integer> s2 = new HashSet<>(Arrays.asList(4, 5, 6, 7, 8, 9));
        
        HashSet<Integer> union = new HashSet<>(s1);   // s1으로 union 생성
        union.addAll(s2);
        System.out.println(union);   // [1, 2, 3, 4, 5, 6, 7, 8, 9] 출력
    }
}
```

## 3. 차집합
```java
import java.util.Arrays;
import java.util.HashSet;

public class Sample {
    public static void main(String[] args) {
        HashSet<Integer> s1 = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5, 6));
        HashSet<Integer> s2 = new HashSet<>(Arrays.asList(4, 5, 6, 7, 8, 9));
      
        HashSet<Integer> substract = new HashSet<>(s1);   // s1으로 substract 생성
        substract.removeAll(s2);   // 차집합 수행
        System.out.println(substract);   // [1, 2, 3] 출력
```

# 관련 메소드
## 값 추가하기 (add)
```java
set.add("Jump");
set.add("To");
set.add("Java");
```

## 값 여러 개 추가하기 (addAll)
```java
set.addAll(Arrays.asList("To", "Java"));
```

## 특정 값 제거하기 (remove)
```java
set.remove("To");
```

※ **TreeSet과 LinkedHashSet**   
Set 자료형은 순서가 없다는 특징이 있다.
하지만 가끔은 Set에 입력된 순서대로 데이터를 가져오고 싶은 경우도 있고 때로는 오름차순으로 정렬된 데이터를 가져오고 싶을 수도 있을 것이다.
이런 경우에는 TreeSet과 LinkedHashSet을 사용한다.

* TreeSet - 오름차순으로 값을 정렬하여 저장하는 특징이 있다.
* LinkedHashSet - 입력한 순서대로 값을 정렬하여 저장하는 특징이 있다.


출처: https://wikidocs.net/157108
