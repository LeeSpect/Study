## 1. HashSet 생성
```java
// 타입을 지정 가능
HashSet<String> animals1 = new HashSet<String>();

// 타입을 생략하여 사용 가능 -> 빈 HashSet생성 시 사용
HashSet<String> animals2 = new HashSet<>();  

// 초기 용량(Capacity) 설정
HashSet<String> animals3 = new HashSet<>(10); 

 // animal의 모든 값을 가진 HashSet 생성 
HashSet<String> animals4 = new HashSet<>(animals1);

//초기값 지정 가능
HashSet<String> animals5 = new HashSet<>(Arrays.asList("tiger", "lion", "fox")); 
```

## 2. HashSet 요소 값 추가
```java
HashSet<String> animals = new HashSet<>()
    animals.add("tiger");
    animals.add("lion");
    animals.add("fox");

HashSet은 저장 순서가 보장되지 않기에 특정 위치에 값을 추가하거나 할 수는 없다는 것을 명심 !
```
만약 입력되는 값이
- HashSet 내부에 존재하지 않는다면 그 값을 HashSet에 추가하고 true를 반환한다.
- HashSet 내부에 존재한다면 false를 반환한다.

## 3. HashSet 크기 구하기
```size()``` 메서드를 사용하여 Hash의 크기를 구할 수 있다.
```java
HashSet<Integer> set = new HashSet<Integer>(Arrays.asList(1,2,3));

//set 크기 : 3
System.out.println(set.size());
```

## 4. HashSet 요소 값 삭제
- ```remove(value)```와 ```clear()``` 메서드를 사용하여 Hash값을 제거할 수 있다.
```java
HashSet<Integer> set = new HashSet<Integer>(Arrays.asList(1,2,3));

//값 1 제거
set.remove(2);

//모든 값을 제거
set.clear();
```
만약 삭제하려는 값이
- HashSet 내부에 존재한다면 그 값을 삭제하고 true를 반환한다.
- HashSet 내부에 존재하지 않는다면, false를 반환한다.

## 5. HashSet 요소 값 검색
- 원하는 값에 대해 ```contains(value)``` 메서드를 통해 Hash 내부에 존재하는지 확인이 가능하다.
```java
HashSet<Integer> set = new HashSet<Integer>(Arrays.asList(1,2,3));

////set내부에 값 1이 있다면 true 출력, 없다면 false 출력
System.out.println(set.contains(1)); 
```

## 6. HashSet 요소 값 출력
Set 컬렉션을 그냥 'print' 처리 할 경우 대괄호( '[ ]' )로 묶여 Set의 전체값이 출력된다.
때문에, 전체 객체를 대상으로 한번씩 반복해서 가져오는 ```반복자 (Iterator)```를 사용해 출력해야 한다.
```java
HashSet<Integer> set = new HashSet<Integer>(Arrays.asList(1,2,3));

//출력결과 :  [1,2,3]
System.out.println(set); 
		

Iterator iter = set.iterator();	

//hasNext() : 가져올 객체가 있다면 true 리턴, 없다면 false 리턴
// next() : Iterator에서 하나의 객체를 가져올 수 있는 메소드
while(iter.hasNext()) {
    System.out.println(iter.next());
}
```

출처: https://velog.io/@acacia__u/hashSet
