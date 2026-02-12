def DFS(x, y, counter_hodove):
    if x == 0 or x == n-1 or y == 0 or y == y - m:
        if maze[x][y] == " ":
            global max_hodove
            max_hodove = max(max_hodove, counter_hodove)
            return


n = int(input())
maze = []
for _ in range(n):
    row = input()
    maze.append(row)

m = len(maze[0])
max_hodove = 0

for i in range(n):
    for j in range(m):
        if maze[i][j] == "k":
            start_x = i
            start_y = j

visited = [[False for _ in range(m)] for _ in range(n)]
max_hodove = 0
