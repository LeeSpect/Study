# PriorityQueue 선언
```java
// 낮은 숫자가 우선순위가 높은 방식
PriorityQueue<Integer> pq = new PriorityQueue<>();
// 높은 숫자가 우선순위가 높은 방식
PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
// 이중 배열에서 0번째 낮은 숫자가 우선순위가 높은 방식(람다식)
PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[0] - o2[0]);
// 이중 배열에서 0번째 낮은 숫자가 우선순위가 높은 방식(Comparator)
PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
    @Override
    public int compare(int[] o1, int[] o2) {
        return o1[0] - o2[0];
    };
});
```
# 메서드
- add() :  　    우선순위 큐에 원소를 추가. 큐가 꽉 찬 경우 에러 발생
- offer()  :       우선순위 큐에 원소를 추가. 값 추가 실패 시 false를 반환
- poll() :         우선순위 큐에서 첫 번째 값을 반환하고  제거, 비어있으면 null 반환
- remove() :   우선순위 큐에서 첫 번째 값을 반환하고  제거, 비어있으면 에러 발생
- isEmpty() :   우선순위 큐에서 첫 번째 값을 반환하고  제거, 비어있으면 에러 발생
- clear() :       우선순위 큐를 초기화
- size() :         우선순위 큐에 포함되어 있는 원소의 수를 반환

# PriorityQueue 기본적인 사용방법
```java
import java.util.PriorityQueue;
 
public class Example {
    public static void main(String[] args) {
 
        // 기본형: 우선순위가 낮은 숫자가 먼저 나옴 (작은 숫자)
        PriorityQueue<Integer> pQ = new PriorityQueue<>();
 
        pQ.offer(1);    // pQ에 원소 1 추가
        pQ.offer(6);    // pQ에 원소 6 추가
        pQ.offer(2);    // pQ에 원소 2 추가
        
        // pQ가 비어있면: true, 그렇지 않으면 : false
        while(!pQ.isEmpty()) {
            // pQ에 첫 번째 값을 반환하고 제거, 비어있다면 null 반환
            System.out.println("pQ.poll() = " + pQ.poll());
        }
 
    }
}
// pQ.poll() = 1
// pQ.poll() = 2
// pQ.poll() = 6
```

# PriorityQueue 클래스 객체 우선순위 정의하기
```java
import java.util.PriorityQueue;
public class Example {
    private class Student {
        int mathScore; // 수학점수
        int engScore;  // 영어점수
        Student(int mathScore, int engScore){
            this.mathScore = mathScore;
            this.engScore = engScore;
        }
    }
    public static void main(String[] args) {
        PriorityQueue<Student> pQ = new PriorityQueue<>();
    }
}
```

# PriorityQueue 클래스 객체 우선순위 정의하기 방법
```java
import java.util.Comparator;
import java.util.PriorityQueue;
 
class Student {
    int mathScore; // 수학점수
    int engScore;  // 영어점수
 
    public Student(int mathScore, int engScore){
        this.mathScore = mathScore;
        this.engScore = engScore;
    }
}
// 클래스 객체의 우선순위를 위한 클래스
class StudentComparator implements Comparator<Student> {
    @Override
    public int compare(Student o1, Student o2) {
        if (o1.mathScore == o2.mathScore) {
            return o2.engScore - o1.engScore;
        } else {
            return o1.mathScore - o2.mathScore;
        }
    }
}
 
public class Example {
 
    public static void main(String[] args) {
 
        // 클래스 객체에 대한 우선순위 기준 제공
        PriorityQueue<Student> pQ = new PriorityQueue<>(1, new StudentComparator());
 
        pQ.offer(new Student(70, 50));  // 우선순위 큐에 클래스 객체를 추가
        pQ.offer(new Student(60, 50));  // 우선순위 큐에 클래스 객체를 추가
        pQ.offer(new Student(70, 40));  // 우선순위 큐에 클래스 객체를 추가
 
        while (!pQ.isEmpty()) {
            Student s = pQ.poll();
            System.out.printf("Student\'s MathScore and engScore: %d, %d \n", s.mathScore, s.engScore);
        }
    }
}

// Student's MathScore and engScore: 60, 50 
// Student's MathScore and engScore: 70, 50 
// Student's MathScore and engScore: 70, 40
```

출처: https://kbj96.tistory.com/49
