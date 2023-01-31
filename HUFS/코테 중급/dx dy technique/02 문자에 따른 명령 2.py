# 개념
dir_num = 3 
x, y = 1, 5
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

# 시계방향으로 90' 회전
# if dir_num == 0:
#     dir_num = 1
# elif dir_num == 1:
#     dir_num = 2
# elif dir_num == 2:
#     dir_num = 3
# else:
#     dir_num = 0

dir_num = (dir_num + 1) % 4

# 앞으로 한 칸 이동
nx, ny = x + dx[dir_num], y + dy[dir_num]

# ----------------------------------------------------------------------------------------------------
# 문제 풀이
dir_num = 3 
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

commands = input()

for cmd in commands:
    if cmd == "L":   # 반시계방향으로 90' 회전
        dir_num = (dir_num - 1 + 4) % 4
    elif cmd == "R": # 시계방향으로 90' 회전
        dir_num = (dir_num + 1) % 4 
    else:
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)
