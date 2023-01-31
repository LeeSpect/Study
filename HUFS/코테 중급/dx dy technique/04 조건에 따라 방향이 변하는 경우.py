# 방향이 180도 바뀌는 문제는 0,3 을 묶고, 1,2를 묶는 것이 좋다
# dir_num = 3 - dir_num으로 하면 현재 방향이 나오기 때문이다.
# 합이 3이 되도록 만들었기 때문에, 3을 빼면 뒤집힌 결과가 나오기 때문이다.

def in_range(n, xr, xc):
    return 1 <= xr and 1 <= xc and xr <= n and xc <= n

n , t = map(int, input().split())
r, c, d = map(str, input().split())
r, c = int(r), int(c)

dr, dc = [-1,1, 0, 0], [0, 0, 1, -1]

D = {
    'U': 0,
    'D': 1,
    'R': 2,
    'L': 3
}

for _ in range(t):
    if in_range(n, r + dr[D[d]], c + dc[D[d]]):
        r += dr[D[d]]
        c += dc[D[d]]
    else:
        if d == 'U': d = 'D'
        elif d == 'D': d = 'U'
        elif d == 'R': d = 'L'
        else: d = 'R'
print(r, c)
