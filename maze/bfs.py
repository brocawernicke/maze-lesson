# reference: https://levelup.gitconnected.com/solve-a-maze-with-python-e9f0580979a1

from maze import coord

m, n = 0, 0
map = []
path = []

def bfs(maze):
  global m, n, map, path
  map = maze
  m, n = len(map), len(map[0])
  for i in range(m):
    path.append([])
    for j in range(n):
      path[i].append(0)
      if map[i][j] == 'S':
        path[i][j] = 1
      if map[i][j] == 'E':
        goal = {'x': i, 'y': j}

  k = 0
  while path[goal['x']][goal['y']] == 0:
    k += 1
    make_step(k)

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

  return conv_coord(traj)

def make_step(k):
  global m, n, map, path
  for i in range(m):
    for j in range(n):
      if path[i][j] == k:
        if i > 0 and path[i-1][j] == 0 and (map[i-1][j] in 'ORE'):
          path[i-1][j] = k + 1
        if j > 0 and path[i][j-1] == 0 and (map[i][j-1] in 'ORE'):
          path[i][j-1] = k + 1
        if i < m-1 and path[i+1][j] == 0 and (map[i+1][j] in 'ORE'):
          path[i+1][j] = k + 1
        if j < n-1 and path[i][j+1] == 0 and (map[i][j+1] in 'ORE'):
          path[i][j+1] = k + 1

def conv_coord(traj_abs):
  comp_dir = 'N'
  traj_rel = []
  for i in range(len(traj_abs)-1):
    cur = traj_abs[i]
    next = traj_abs[i+1]
    if next[0] == cur[0]-1:
      next_comp_dir = 'N'
    elif next[0] == cur[0]+1:
      next_comp_dir = 'S'
    elif next[1] == cur[1]-1:
      next_comp_dir = 'W'
    elif next[1] == cur[1]+1:
      next_comp_dir = 'E'
    traj_rel.append(coord.num2dir(coord.card2num(next_comp_dir) - coord.card2num(comp_dir)))
    comp_dir = next_comp_dir
  return traj_rel
