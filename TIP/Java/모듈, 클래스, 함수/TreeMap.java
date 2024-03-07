package BTest;

import java.util.*;

public class TreeMapExample {

	public static void main(String[] args) {
		// TreeMap 생성
		TreeMap<Integer, String> treeMap = new TreeMap<>();

		// 엘리먼트 추가
		treeMap.put(5, "Value 5");
		treeMap.put(1, "Value 1");
		treeMap.put(8, "Value 8");
		treeMap.put(3, "Value 3");
		treeMap.put(6, "Value 6");
		treeMap.put(4, "Value 4");
		treeMap.put(7, "Value 7");
		treeMap.put(2, "Value 2");
		treeMap.put(9, "Value 9");
		treeMap.put(10, "Value 10");

		// TreeMap 출력
		System.out.println("TreeMap 내용: " + treeMap);
    // {1=Value 1, 2=Value 2, 3=Value 3, 4=Value 4, 5=Value 5, 6=Value 6, 7=Value 7, 8=Value 8, 9=Value 9, 10=Value 10}

		// 특정 키에 대한 값 검색
		String value = treeMap.get(5);
		System.out.println("key 5에 대응하는 value: " + value); // 5

		// 엘리먼트 삭제
		treeMap.remove(10);
		System.out.println("key 10을 지운 후: " + treeMap);
    // {1=Value 1, 2=Value 2, 3=Value 3, 4=Value 4, 5=Value 5, 6=Value 6, 7=Value 7, 8=Value 8, 9=Value 9}

		// 첫 번째 (가장 낮은) 키와 마지막 (가장 높은) 키 찾기
		Integer firstKey = treeMap.firstKey();
		Integer lastKey = treeMap.lastKey();
		System.out.println("First Key: " + firstKey + ", Last Key: " + lastKey); // 1, 9

		// 부분 맵 추출
		TreeMap<Integer, String> subMap = new TreeMap<>(treeMap.subMap(3, true, 7, true));
		System.out.println("SubMap from 3 to 7: " + subMap);
    // {3=Value 3, 4=Value 4, 5=Value 5, 6=Value 6, 7=Value 7}
		
		// ceilingEntry() 및 ceilingKey()
        Map.Entry<Integer, String> ceilingEntry = treeMap.ceilingEntry(4);
        System.out.println("Ceiling entry for 4: " + ceilingEntry); // 4
        Integer ceilingKey = treeMap.ceilingKey(4);
        System.out.println("Ceiling key for 4: " + ceilingKey); // 4

        // containsKey() 및 containsValue()
        boolean containsKey = treeMap.containsKey(3); // 3
        boolean containsValue = treeMap.containsValue("Value 3");
        System.out.println("Contains key 3: " + containsKey);
        System.out.println("Contains value 'Value 3': " + containsValue); // true

        // entrySet()
        Set<Map.Entry<Integer, String>> entries = treeMap.entrySet();
        System.out.println("Entry set: " + entries);

        // firstEntry() 및 lastEntry()
        Map.Entry<Integer, String> firstEntry = treeMap.firstEntry();
        Map.Entry<Integer, String> lastEntry = treeMap.lastEntry();
        System.out.println("First entry: " + firstEntry);
        System.out.println("Last entry: " + lastEntry);

        // floorEntry() 및 floorKey()
        Map.Entry<Integer, String> floorEntry = treeMap.floorEntry(4);
        Integer floorKey = treeMap.floorKey(4);
        System.out.println("Floor entry for 4: " + floorEntry);
        System.out.println("Floor key for 4: " + floorKey);

        // headMap()
        TreeMap<Integer, String> headMap = new TreeMap<>(treeMap.headMap(5));
        System.out.println("Head map before 5: " + headMap);

        // higherEntry()
        Map.Entry<Integer, String> higherEntry = treeMap.higherEntry(5);
        System.out.println("Entry higher than 5: " + higherEntry);

        // keySet()
        Set<Integer> keys = treeMap.keySet();
        System.out.println("Key set: " + keys);

        // lowerEntry() 및 lowerKey()
        Map.Entry<Integer, String> lowerEntry = treeMap.lowerEntry(5);
        Integer lowerKey = treeMap.lowerKey(5);
        System.out.println("Entry lower than 5: " + lowerEntry);
        System.out.println("Key lower than 5: " + lowerKey);

        // pollFirstEntry() 및 pollLastEntry()
        Map.Entry<Integer, String> polledFirstEntry = treeMap.pollFirstEntry();
        Map.Entry<Integer, String> polledLastEntry = treeMap.pollLastEntry();
        System.out.println("Polled first entry: " + polledFirstEntry);
        System.out.println("Polled last entry: " + polledLastEntry);

        // replace()
        treeMap.replace(3, "New Value 3");
        System.out.println("After replacing value for key 3: " + treeMap.get(3));
        boolean isReplaced = treeMap.replace(3, "New Value 3", "Replaced Value 3");
        System.out.println("Successfully replaced: " + isReplaced + ", Current value: " + treeMap.get(3));

        // 마무리된 TreeMap 출력
        System.out.println("Final TreeMap: " + treeMap);
    }

}
