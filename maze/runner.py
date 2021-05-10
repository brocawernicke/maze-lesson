from maze import conversion
from maze.bfs import bfs

class Runner:
  def __init__(self):
    self.pos = [20, 20]
    self.dir = 'N'
    self.map = [['?' for _ in range(40)] for _ in range(40)]
    self.visited = [[False for _ in range(40)] for _ in range(40)]
    self.stack = [(20, 20)]

  """ update runner's imaginary map per 3x3 map """
  def update_map(self, surr: str):
    for _ in range(conversion.NESW.index(self.dir)):
      surr = [surr[conversion.CCW[i]] for i in range(9)]
    for i in range(-1, 2):
      for j in range(-1, 2):
        self.map[self.pos[0]+i][self.pos[1]+j] = surr[(i+1)*3+(j+1)]

  """ calculate a next moving direction """
  def get_next_move(self) -> str:
    dir, cur = 'Lost', '?'
    i, j = self.pos[0], self.pos[1]
    if self.map[i-1][j] in 'ROSE' and self.stack[-1] != (i-1, j) and not self.visited[i-1][j]:
      self.pos[0] -= 1
      dir = conversion.DIR[-conversion.NESW.index(self.dir)]
      self.dir = 'N'
      cur = self.map[i-1][j]
      self.stack.append((i, j))
      self.visited[i-1][j] = True
    elif self.map[i][j+1] in 'ROSE' and self.stack[-1] != (i, j+1) and not self.visited[i][j+1]:
      self.pos[1] += 1
      dir = conversion.DIR[1 - conversion.NESW.index(self.dir)]
      self.dir = 'E'
      cur = self.map[i][j+1]
      self.stack.append((i, j))
      self.visited[i][j+1] = True
    elif self.map[i+1][j] in 'ROSE' and self.stack[-1] != (i+1, j) and not self.visited[i+1][j]:
      self.pos[0] += 1
      dir = conversion.DIR[2 - conversion.NESW.index(self.dir)]
      self.dir = 'S'
      cur = self.map[i+1][j]
      self.stack.append((i, j))
      self.visited[i+1][j] = True
    elif self.map[i][j-1] in 'ROSE' and self.stack[-1] != (i, j-1) and not self.visited[i][j-1]:
      self.pos[1] -= 1
      dir = conversion.DIR[3 - conversion.NESW.index(self.dir)]
      self.dir = 'W'
      cur = self.map[i][j-1]
      self.stack.append((i, j))
      self.visited[i][j-1] = True
    else:
      pos = self.stack.pop()
      self.pos = [pos[0], pos[1]]
      self.dir = conversion.NESW[2 - conversion.NESW.index(self.dir)]
      dir = conversion.DIR[2 - conversion.NESW.index(self.dir)]
      cur = self.map[i][j]
    print("{0} next: {1}, {2}".format(cur, self.dir, self.pos))
    return cur, dir

  """ calculate the shortest path on runner's map """
  def get_shortest_path(self) -> list:
    return bfs(self.map)
