x, y = 0, 0
n = int(input())

#     0.  1.  2. 3
dx = [1,  0, -1, 0]
dy = [0, -1,  0, 1]
for i in range(n):
    c_dir, dist = tuple(input().split()) # c_dir : "N" / dist : "3"
    dist = int(dist)

    # c_dir : "N" / dist : 3

    # if c_dir == "E":
    #     dir_num = 0
    # elif c_dir == "S":
    #     dir_num = 1
    # elif c_dir == "W":
    #     dir_num = 2
    # else:
    #     dir_num = 3

    mapper = {
        "E": 0,
        "S": 1,
        "W": 2,
        "N": 3
    }
    dir_num = mapper[c_dir]

    x, y = x + dx[dir_num] * dist, y + dy[dir_num] * dist

print(x, y)






