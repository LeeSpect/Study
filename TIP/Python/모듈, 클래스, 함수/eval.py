# eval(expression)
# 매개변수로 받은 expression (=식)을 문자열로 받아서 실행하는 함수
# 식 : <>+-/* while for 

# 장점 : input 함수를 이용해 사용자로부터 원하는 파이썬 함수 또는 식을 입력받아서 마음대로 프로그램을 조종할 수 있음
# 단점 : 사용자가 마음대로 프로그램을 조종할 수 있다. 즉, 프로그램에 명령을 입력할 수 있다. 결국 그 말은 프로그램을 상처입히거나 해킹을 하거나 할 수 있다는 뜻임
# 너무 많은 자유를 주기 때문에, 실제 릴리즈 하는 프로그램에서 사용하는 것은 위험함

# 파이썬 eval(expression) 예제
 
# 1. 문자열 덧셈
a = eval('"a + B"')
print(f"1. eval('\"a\"' + '\" B\"') : {a}")
# 1. eval('"a"' + '" B"') : aB
 
# 2. 숫자 덧셈
b = eval("100 + 32")
print(f'2. eval("100 + 32") : {b}')
# 2. eval("100 + 32") : 132
 
# 3. 내장 함수 abs
c = eval("abs(-56)")
print(f'3. eval("abs(-56)") : {c}')
# 3. eval("abs(-56)") : 56
 
# 4. 리스트 길이
d = eval("len([1,2,3,4])")
print(f'4. eval("len([1,2,3,4])") : {d}')
# 4. eval("len([1,2,3,4])") : 4
 
# 5. round 함수
e = eval("round(1.5)")
print(f'5. eval("round(1.5)") : {e}')
# 5. eval("round(1.5)") : 2


# : https://blockdmask.tistory.com/437 [개발자 지망생]
