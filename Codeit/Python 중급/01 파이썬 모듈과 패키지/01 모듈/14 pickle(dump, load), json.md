### pickle

**pickle**을 사용하면 파이썬 오브젝트(객체)를 바이트(byte) 형식으로 바꿔서 파일에 저장할 수 있고 저장된 오브젝트를 읽어올 수도 있습니다.

```python
import pickle

# 딕셔너리 오브젝트
obj = {'my': 'dictionary'}

# obj를 filename.pickle 파일에 저장
with open('filename.pickle', 'wb') as f:
    pickle.dump(obj, f)
    
# filename.pickle에 있는 오브젝트를 읽어옴
with open('filename.pickle', 'rb') as f:
    obj = pickle.load(f)
    
print(obj)
```
```python
----------------------------------------------------------------------------------------------------
{'my': 'dictionary'}
----------------------------------------------------------------------------------------------------
```

### json

**json** module은 **pickle**과 비슷하지만 오브젝트를 JSON 형식으로 바꿔줍니다. JSON 형식에 맞는 데이터 (기본 데이터 타입들, 리스트, 딕셔너리)만 바꿀 수 있습니다.

```python
import json

# 딕셔너리 오브젝트
obj = {'my': 'dictionary'}

# obj를 filename.json 파일에 저장
with open('filename.json', 'w') as f:
    json.dump(obj, f)

# filename.json에 있는 오브젝트를 읽어옴
with open('filename.json', 'r') as f:
    obj = json.load(f)
    
print(obj)
```
```python
------------------------------------------------------------------------------------------
{'my': 'dictionary'}
------------------------------------------------------------------------------------------
```
