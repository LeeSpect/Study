def in_range(n, x, y):
    return 0 <= x and 0 <= y and x < n and y < n

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]

ans = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy
            if in_range(n, nx, ny) and l[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            ans += 1
print(ans)
