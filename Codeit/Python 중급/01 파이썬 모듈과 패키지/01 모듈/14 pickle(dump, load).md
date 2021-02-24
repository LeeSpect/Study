### pickle

**pickle**을 사용하면 파이썬 오브젝트(객체)를 바이트(byte) 형식으로 바꿔서 파일에 저장할 수 있고 저장된 오브젝트를 읽어올 수도 있습니다.

```
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
```
----------------------------------------------------------------------------------------------------
{'my': 'dictionary'}
----------------------------------------------------------------------------------------------------
```
