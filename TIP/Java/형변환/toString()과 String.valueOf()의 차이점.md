### 차이점
변경하고자 하는Object가 null인 경우   
toString()과 같은 경우 Null PointerException(NPE)을 발생시키지만 valueOf는 "null"이라는 문자열로 처리한다.

- String.valueOf() - 파라미터가 null이면 문자열 "null"을 만들어서 반환한다.
- toString() - 대상 값이 null이면 NPE를 발생시키고 Object에 담긴 값이 String이 아니여도 출력한다.

```java
destItemMap.get("LOWER_VAL") 이 null 일 경우
String lowerCoatingVal1 = String.valueOf(destItemMap.get("LOWER_VAL"));
String lowerCoatingVal2 = destItemMap.get("LOWER_VAL").toString();
 
lowerCoatingVal1 = "null"
lowerCoatingVal2 = NullPointerException 발생
 
String.valueOf()의 null 체크
String lowerCoatingVal1 = String.valueOf(destItemMap.get("LOWER_VAL"));
if("null".equals(lowerCoatingVal1)) {
    // To do Somting....
}
 
// equals함수를 사용할때 왼쪽에 있는 것을 기준으로 비교하기 때문에 변수보다는 문자열을 왼쪽에 두는 것을 추천한다.
// 즉 strTestVal이 null인 경우 ret = "1"인 if문은 NPE를 발생시킨다.
String strTestVal = null;
String ret = "";
 
/* Exception 발생 */
if( !(strTestVal .equals("")) ) ret = "1";
 
/* 정상 */
if( !("".equals(strTestVal)) ) ret = "2";
```

- 차이점은 null값에 따른 NPE의 발생 유무

이런 차이점 때문에 valueOf의 null체크 방법은 "null".equals(string) 형태로 체크를 해야한다.   
null로 인해 발생된 에러는 시간이 지나고, 타인의 소스인경우 디버깅하기 어렵고 어떤의미를 내포하고 있는지 판단하기 어렵다. 때문에 NPE를 방지하기 위해 toString보다는 ```valueOf를 사용하는 것을 추천```한다.

출처: https://swjeong.tistory.com/146
