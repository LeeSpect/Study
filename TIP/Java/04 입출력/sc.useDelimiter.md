두 값이 공백이 아닌 특정 문자를 사이에 두고 입력되는 경우에는, sc.useDelimiter("특정 문자") 을 통해 해당 문자 단위로 자를 수 있다.

상황이 복잡한 경우라면, 전체를 하나의 문자열로 입력받은 다음, s.split("특정 문자") 함수를 이용하여 문자열을 특정 문자를 기준으로 나눈 뒤 각 값을 원소로 하는 배열을 받을 수 있다. 

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        sc.useDelimiter(":");
        int hour = sc.nextInt(), minute = sc.nextInt();
        System.out.println((hour + 1) + ":" + minute);
        sc.close();
    }   
}
```

```java
sc.useDelimiter(".");
```
```java
sc.useDelimiter("\\.");
```

useDelimiter 안의 값은 정규 표현식을 쓰는데, 정규 표현식에서 "."은 '모든 단어' 와 같은 의미를 가지고 있어 오류가 발생합니다. "."을 기준으로 나누고 싶다면 "." 대신 "`\\.`"을 이용해야 합니다.

정규 표현식에서는 ".", "^", "$", "*" 와 같은 문자는 다른 뜻을 가지고 있습니다. 따라서 이런 문자로 나눌 때에는 "." 대신 "`\\.`"으로, "^" 대신 "`\\^`" 으로 적어야 제대로 나눠짐을 유의해야 합니다!
