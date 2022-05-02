# 형변환

```java
String num = '123';
```

자료형은 문자열이지만 그 내용은 숫자로 이루어진 값이다.
이럴 경우에 문자열을 정수로 바꿀 수 있다.
문자열을 정수로 바꾸려면 다음과 같이 Integer 클래스를 사용한다.   
※ Integer는 int자료형의 Wrapper 클래스이다.

```java
public calss Sample {
    public static void main(String[] args) {
        String num = '123';
        int n = Integer.parseInt(num);
        System.out.println(n);   // 123 출력
    }
}
```

### 정수 -> 문자열
```java
public class Sample {
    public static void main(String[] args) {
        int n = 123;
        String num = '' + n;
        System.out.println(num);   // 123 출력
    }
}
```
또는
```java
public class Sample {
    public static void main(String[] args) {
        int n = 123;
        String num1 = String.valueOf(n);
        String num2 = Integer.toString(n);
        System.out.println(num1);   // 123 출력
        System.out.println(num2);   // 123 출력
    }
}
```

### 문자열 -> 실수형
```Double.parseDouble``` 또는 ```Folat.parseFloat```를 사용하여 형변환할 수 있다.
```java
public class Sample {
    public static void main(String[] args) {
        String num = '123.456';
        double d = Double.parseDouble(num);
        System.out.println(d);
    }
}
```

### 실수 -> 정수, 정수-> 실수
```java
public class Sample {
    public static void main(String[] args) {
        int n1 = 123;
        double d1 = n1;   // 정수를 실수로 바꿀 때는 캐스팅이 필요없다.
        System.out.println(d1);   // 123.0 출력
      
        double d2 = 123.456;
        int n2 = (int) d2;   // 실수를 정수로 바꿀 때는 반드시 정수형으로 캐스팅해야 한다.
        System.out.println(n2)   // 소숫점이 생략된 123 출력
    }
}
```
      
# final
자료형에 값을 단 한번만 설정할 수 있게 강제하는 키워드이다.
즉, 값을 한번 설정하면 그 값을 다시 설정할 수 없다.
```java
public class Sample {
    public static void main(String[] args) {
        final int n = 123;   // final 로 설정하면 값을 바꿀 수 없다.
        n = 456;   // 컴파일 에러 발생
    }
}
```
리스트의 경우도 final로 선언시 재할당은 불가능하다.

final은 프로그램 수행 도중 그 값이 변경되면 안 되는 상황에 사용한다.

※ **Unmodifiable List**   
리스트의 경우 final로 선언시 리스트에 값을 더하거나(add) 빼는(remove) 것은 가능하다.
다만 재할당만 불가능할 뿐이다.
만약 그 값을 더하거나 빼는 것도 불가능하게 하고 싶은 경우에는 **List.of**로 수정이 불가능한 리스트(Unmodifiable List)를 생성해야 한다.
```java
import java.util.List;

public class Sample {
    public static void main(String[] args) {
        final List<String> a = List.of('a', 'b');
        a.add('c');    // UnsupportedOperationException 발생
    }
}
```
      
출처: https://wikidocs.net/158529
