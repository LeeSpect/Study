# 생성
```java
enum CoffeeType {
    AMERICANO,
    ICE_AMERICANO,
    CAFE_LATTE
};
```

정의한 상수 집합은 다음과 같이 사용할 수 있다.
```java
public class Sample {
    enum CoffeeType {
        AMERICANO,
        ICE_AMERICANO,
        CAFE_LATTE
    };
  
    public static void main(String[] args) {
        System.out.println(CoffeeType.AMERICANO);   // AMERICANO 출력
        System.out.println(CoffeeType.ICE_AMERICANO);   // ICE_AMERICANO 출력
        System.out.println(CoffeeType.CAFE_LATTE);   // CAFE_LATTE 출력
    }
}
```
또는 다음과 같이 반복문에서 사용할수도 있다.
```java
public class Sample {
    enum CoffeeType {
        AMERICANO,
        ICE_AMERICANO,
        CAFE_LATTE
    };
    
    public static void main(String[] args) {
        for(CoffeeType type: CoffeeType.values()) {
            System.out.println(type);   // 순서대로 AMERICANO, ICE_AMERICANO, CAFE_LATTE 출력
        }
    }
}
```

장점
* 매직넘버(1과 같은 숫자 상수값)를 사용할 때보다 코드가 명확해진다.
* 잘못된 값을 사용함으로 인해 발생할 수 있는 위험성이 사라진다.

※ 프로그래밍에서 상수로 선언하지 않은 숫자를 매직넘버라고 한다.

출처: https://wikidocs.net/157271
