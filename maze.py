m, n = map(int, input().split())

maze = ['X' * n] * m
path = []

for i in range(m):
  maze[i] = input()

for i in range(m):
  path.append([])
  for j in range(n):
    path[i].append(0)
    if maze[i][j] == 'S':
      path[i][j] = 1
    if maze[i][j] == 'E':
      goal = {'x': i, 'y': j}

def makeStep(k):
  for i in range(m):
    for j in range(n):
      if path[i][j] == k:
        if i > 0 and path[i-1][j] == 0 and (maze[i-1][j] == 'o' or maze[i-1][j] == 'E'):
          path[i-1][j] = k + 1
        if j > 0 and path[i][j-1] == 0 and (maze[i][j-1] == 'o' or maze[i][j-1] == 'E'):
          path[i][j-1] = k + 1
        if i < m-1 and path[i+1][j] == 0 and (maze[i+1][j] == 'o' or maze[i+1][j] == 'E'):
          path[i+1][j] = k + 1
        if j < n-1 and path[i][j+1] == 0 and (maze[i][j+1] == 'o' or maze[i][j+1] == 'E'):
          path[i][j+1] = k + 1

k = 0
while path[goal['x']][goal['y']] == 0:
  k += 1
  makeStep(k)

i, j = goal['x'], goal['y']
k = path[goal['x']][goal['y']]
traj = [(i, j)]
while k > 1:
  if i > 0 and path[i-1][j] == k-1:
    i, j = i-1, j
    traj.append((i, j))
    k -= 1
  elif j > 0 and path[i][j-1] == k-1:
    i, j = i, j-1
    traj.append((i, j))
    k -= 1
  elif i < m-1 and path[i+1][j] == k-1:
    i, j = i+1, j
    traj.append((i, j))
    k -= 1
  elif i < m-1 and path[i][j+1] == k-1:
    i, j = i, j+1
    traj.append((i, j))
    k -= 1

traj.reverse()
print(traj)

# BFS
# https://levelup.gitconnected.com/solve-a-maze-with-python-e9f0580979a1
