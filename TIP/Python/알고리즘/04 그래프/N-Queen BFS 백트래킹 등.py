# BFS 백트래킹
def solution(n):
    cases = [0] # shallow copy of the cases (list)
    def dfs(queens, next_queen):
        # column check
        if next_queen in queens:
            return

        # diagonal check
        for row, column in enumerate(queens):
            h = len(queens) - row
            if next_queen == column + h or next_queen == column - h:
                return

        queens.append(next_queen)
        # end check
        if len(queens) == n:
            cases[0] += 1
            return

        for next_queen in range(n):
            dfs(queens[:], next_queen) # deep copy of queens

    for next_queen in range(n):
        queens = []
        dfs(queens, next_queen)
    return cases[0]
# 출처: https://davi06000.tistory.com/73



n = int(input())
ans = 0
row = [0] * n
def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            print(row)
            if is_promising(x):
                n_queens(x+1)
n_queens(0)
print(ans)
# 출처: https://seongonion.tistory.com/103
