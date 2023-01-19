![image](https://user-images.githubusercontent.com/64893709/213379207-f3b279d9-240c-4ac7-8f60-801bd6fe6c10.png)
![image](https://user-images.githubusercontent.com/64893709/213379229-814fb27e-03d0-42da-a687-3593f0c6f1ce.png)
![image](https://user-images.githubusercontent.com/64893709/213379246-c50c5a4f-e15f-4a64-8f95-6e867d180c84.png)


```java
import java.util.*;

class Point {
    private double x; // 점의 x 좌표
    private double y; // 점의 y 좌표

    public void setX(double a) { // 좌표값이 private면 set, get의 메소드를 통해 main함수에서 접근해야 함
        x = a;
    }

    public void setY(double a) {
        y = a;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

}

class Circle {
    private Point center;
    private Point px;

    public void setCenter(Point a) {  // Point 변수로 받아와야 함
        center = a;
    }

    public void setPx(Point a) {
        px = a;
    }

    public Point getCenter() {
        return center;
    }

    public Point getPx() {
        return px;
    }

    public double calRadius() {
        double radius;
        radius = Math.sqrt(Math.pow(center.getX() - px.getX(), 2) + Math.pow(center.getY() - px.getY(), 2));
        return radius;
    }

    public double calArea() {
        return calRadius() * calRadius() * Math.PI;
    }

    public double calLength() {
        return 2 * calRadius() * Math.PI;
    }
}

public class Test {
    public static void main(String[] args) {
        Point p1 = new Point();
        Point p2 = new Point();
        Scanner keyboard = new Scanner(System.in);
        System.out.println("중점의 x, y 좌표를 입력하세요");
        p1.setX(keyboard.nextDouble());
        p1.setY(keyboard.nextDouble());
        System.out.println("원 위의 한 점의 x, y 좌표를 입력하세요");
        p2.setX(keyboard.nextDouble());
        p2.setY(keyboard.nextDouble());

        Circle c = new Circle();
        c.setCenter(p1);
        c.setPx(p2);
        System.out.println("이 원의 넓이는 " + c.calArea() + "입니다."); 
        System.out.println("이 원의 둘레는 " + c.calLength() + "입니다."); 

        keyboard.close();
    }
}
```
