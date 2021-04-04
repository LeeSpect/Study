![image](https://user-images.githubusercontent.com/64893709/113499658-b1561e00-9552-11eb-888c-864c62466be6.png)


``` python
import numpy as np

# 1: 행렬 A를 정의해보세요
A = np.array([
    [0, 1, -1],
    [1, 2, 3],
    [2, 1, 0],
    [-1, 2, -4]
    ])

# 2: 행렬 B를 정의해보세요
B = np.array([
    [0, 2],
    [1, 1],
    [-1, -2]
    ])

print(A)
print(B)
print(A[1][1])  # 3: 여기서 A의 2행 2열 원소에 접근해보세요
print(A[3][0])  # 4: 여기서 A의 4행 1열 원소에 접근해보세요
```
```python
[[ 0  1 -1]
 [ 1  2  3]
 [ 2  1  0]
 [-1  2  -4]]
[[ 0  2]
 [ 1  1]
 [-1 -2]]
2
-1
```

![image](https://user-images.githubusercontent.com/64893709/113499683-e2cee980-9552-11eb-9f7f-94f19f746b65.png)

![image](https://user-images.githubusercontent.com/64893709/113499685-efebd880-9552-11eb-8fa5-69abbb2d4069.png)


