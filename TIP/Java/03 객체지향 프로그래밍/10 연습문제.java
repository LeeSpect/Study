

//6번 문제
// 다음은 Calculator 객체를 생성하고 값을 더한 후에 그 결과값을 출력하는 예제이다.
// 하지만 코드를 실행하면 오류가 발생한다.
// Calculator 클래스를 수정하여 다음의 코드에서 오류가 발생하지 않도록 하시오.

// class Calculator {
//     Integer value;
//     void add(int val) {
//         this.value += val;
//     }

//     public Integer getValue() {
//         return this.value;
//     }
// }

// public class Sample {
//     public static void main(String[] args) {
//         Calculator cal = new Calculator();
//         cal.add(3);  // 여기서 NullPointerException 이 발생한다.
//         System.out.println(cal.getValue());
//     }
// }


class Calculator {
    Integer value;
    
    Calculator(){     // Calculator 클래스의 생성자를 만들고 초기값을 설정해야 한다.
        this.value = 0;
    }
    void add(int val) {
        this.value += val;
    }

    public Integer getValue() {
        return this.value;
    }
}

public class Main {
    public static void main(String[] args) {
        Calculator cal = new Calculator();
        cal.add(3);
        System.out.println(cal.getValue());
    }
}

//7번 문제
// 이 광물 계산기는 광물이 추가될 때마다 add 메서드를 추가해야 한다는 단점이 있다.
// 광물이 추가되더라도 MineralCalculator 클래스를 변경할 필요가 없도록 코드를 수정하시오.

// class Gold {
// }

// class Silver {
// }

// class Bronze {
// }

// class MineralCalculator {
//     int value = 0;

//     public void add(Gold gold) {
//         this.value += 100;
//     }

//     public void add(Silver silver) {
//         this.value += 90;
//     }

//     public void add(Bronze bronze) {
//         this.value += 80;
//     }

//     public int getValue() {
//         return this.value;
//     }
// }

// public class Sample {
//     public static void main(String[] args) {
//         MineralCalculator cal = new MineralCalculator();
//         cal.add(new Gold());
//         cal.add(new Silver());
//         cal.add(new Bronze());
//         System.out.println(cal.getValue());  // 270 출력
//     }
// }


interface Mineral{ 
    int getVal();
}

class Gold implements Mineral {
    public int getVal() {
        return 100;
    }
}

class Silver implements Mineral{
    public int getVal() {
        return 90;
    }
}

class Bronze implements Mineral{
    public int getVal() {
        return 80;
    }
}

class MineralCalculator {
    int value = 0;
    
    public void add(Mineral mineral){
        this.value+=mineral.getVal();
    }

    public int getValue() {
        return this.value;
    }
}

public class Main {
    public static void main(String[] args) {
        MineralCalculator cal = new MineralCalculator();
        cal.add(new Gold());
        cal.add(new Silver());
        cal.add(new Bronze());
        System.out.println(cal.getValue());  // 270 출력
    }
}
