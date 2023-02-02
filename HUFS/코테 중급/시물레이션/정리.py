# 1. 참조만 할 땐 그대로
# 2. 일정 부분만 바꿀 땐 mutable일 땐 필요 x
# 3. 전체 부분 바꿀 땐 둘다 global

# 변수 선언 및 입력
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


# (row_s, col_s) ~ (row_e, col_e) 사이의 금의 개수를 계산합니다.
def get_num_of_gold(row_s, col_s, row_e, col_e):
    num_of_gold = 0

    for row in range(row_s, row_e + 1):
        for col in range(col_s, col_e + 1):
            num_of_gold += grid[row][col]

    return num_of_gold


max_gold = 0
# (row, col)이 3 * 3 격자의 좌측 상단 모서리인 경우를 전부 탐색합니다. 
for row in range(n):
    for col in range(n):
        # 3 * 3 격자가 n * n 격자를 벗어나는 경우는 계산하지 않습니다.
        if row + 2 >= n or col + 2 >= n:
            continue
        
        num_of_gold = get_num_of_gold(row, col, row + 2, col + 2)
            
        # 최대 금의 개수를 저장합니다.
        max_gold = max(max_gold, num_of_gold)

print(max_gold)



# ------------------------------------------------------



# 변수 선언 및 입력
n, t = tuple(map(int, input().split()))
u = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(t):
    # Step 1
    # 위에서 가장 오른쪽에 있는 숫자를 따로 temp값에 저장해놓습니다.
    temp = u[n - 1]
    
    # Step 2
    # 위에 있는 숫자들을 완성합니다. 
    # 오른쪽에서부터 채워넣어야 하며, 
    # 맨 왼쪽 숫자는 아래에서 가져와야함에 유의합니다.
    for i in range(n - 1, 0, -1):
        u[i] = u[i - 1]
    u[0] = d[n - 1]
    
    # Step 3
    # 아래에 있는 숫자들을 완성합니다. 
    # 마찬가지로 오른쪽에서부터 채워넣어야 하며, 
    # 맨 왼쪽 숫자는 위에서 미리 저장해놨던 temp값을 가져와야함에 유의합니다.
    for i in range(n - 1, 0, -1):
        d[i] = d[i - 1]
    d[0] = temp

# 출력
for elem in u:
    print(elem, end=" ")
print()

for elem in d:
    print(elem, end=" ")


# -------------------------------

# 변수 선언 및 입력
n = int(input())
numbers = [
    int(input())
    for _ in range(n)
]
end_of_array = n


# 입력 배열에서 지우고자 하는 부분 수열을 삭제합니다.
def cut_array(start_idx, end_idx):
    global end_of_array, numbers
    temp_arr = []
    # 구간 외의 부분만 temp 배열에 순서대로 저장합니다.
    for i in range(end_of_array):
        if i < start_idx or i > end_idx:
            temp_arr.append(numbers[i])

    # temp 배열을 다시 numbers 배열로 옮겨줍니다.
    end_of_array = len(temp_arr)
    for i in range(end_of_array):    
        numbers[i] = temp_arr[i]


# 두 번에 걸쳐 지우는 과정을 반복합니다.
for _ in range(2):
    s, e = tuple(map(int, input().split()))
    # [s, e] 구간을 삭제합니다.
    cut_array(s - 1, e - 1)

# 출력:
print(end_of_array)
for i in range(end_of_array):
    print(numbers[i])

