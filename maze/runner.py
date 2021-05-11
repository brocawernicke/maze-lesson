import logging

from maze import coord
from maze.bfs import bfs

class Runner:
  def __init__(self):
    self.pos = [20, 20]
    self.dir = 'N'
    self.map = [['?' for _ in range(40)] for _ in range(40)]
    self.visited = [[False for _ in range(40)] for _ in range(40)]
    self.stack = [(20, 20)]
    self.goal_found = False
    self.start_found = False

  """ update runner's imaginary map per 3x3 map """
  def update_map(self, surr: str):
    for _ in range(coord.card2num(self.dir)):
      surr = coord.ccw3x3(surr)
    row, col = self.pos[0], self.pos[1]
    for i in [row-1, row, row+1]:
      for j in [col-1, col, col+1]:
        self.map[i][j] = surr[(i-row+1)*3+(j-col+1)]

  """ calculate a next moving direction """
  def get_next_move(self) -> str:
    dir, cur = 'Lost', '?'
    i, j = self.pos[0], self.pos[1]

    logging.debug('pos: {0}, {1}'.format(i, j))
    logging.debug('{0}{1}{2} {3}{4}{5}'.format(self.map[i-1][j-1], self.map[i-1][j], self.map[i-1][j+1], self.visited[i-1][j-1], self.visited[i-1][j], self.visited[i-1][j+1]))
    logging.debug('{0}{1}{2} {3}{4}{5}'.format(self.map[i-0][j-1], self.map[i-0][j], self.map[i-0][j+1], self.visited[i-0][j-1], self.visited[i-0][j], self.visited[i-0][j+1]))
    logging.debug('{0}{1}{2} {3}{4}{5}'.format(self.map[i+1][j-1], self.map[i+1][j], self.map[i+1][j+1], self.visited[i+1][j-1], self.visited[i+1][j], self.visited[i+1][j+1]))

    if self.map[i-1][j] in 'ROSE' and self.stack[-1] != (i-1, j) and not self.visited[i-1][j]:
      dir = coord.num2dir(-coord.card2num(self.dir))
      self.dir = 'N'
      self.pos[0] -= 1
      self.stack.append((i, j))
      self.visited[i-1][j] = True
      cur = self.map[i-1][j]
    elif self.map[i][j+1] in 'ROSE' and self.stack[-1] != (i, j+1) and not self.visited[i][j+1]:
      dir = coord.num2dir(1 - coord.card2num(self.dir))
      self.dir = 'E'
      self.pos[1] += 1
      self.stack.append((i, j))
      self.visited[i][j+1] = True
      cur = self.map[i][j+1]
    elif self.map[i+1][j] in 'ROSE' and self.stack[-1] != (i+1, j) and not self.visited[i+1][j]:
      dir = coord.num2dir(2 - coord.NESW.index(self.dir))
      self.dir = 'S'
      self.pos[0] += 1
      self.stack.append((i, j))
      self.visited[i+1][j] = True
      cur = self.map[i+1][j]
    elif self.map[i][j-1] in 'ROSE' and self.stack[-1] != (i, j-1) and not self.visited[i][j-1]:
      dir = coord.num2dir(3 - coord.NESW.index(self.dir))
      self.dir = 'W'
      self.pos[1] -= 1
      self.stack.append((i, j))
      self.visited[i][j-1] = True
      cur = self.map[i][j-1]
    else:
      next_pos = self.stack.pop()
      if next_pos[1] > self.pos[1]:
        next_dir = 'E'
      elif next_pos[1] < self.pos[1]:
        next_dir = 'W'
      elif next_pos[0] < self.pos[0]:
        next_dir = 'N'
      elif next_pos[0] > self.pos[0]:
        next_dir = 'S'
      else:
        next_dir = '?'
      logging.debug('next: {0} {1}'.format(next_pos, next_dir))
      logging.debug('stack: {0}'.format(self.stack))
      dir = coord.num2dir(coord.card2num(next_dir) - coord.card2num(self.dir))
      self.pos = [next_pos[0], next_pos[1]]
      self.dir = next_dir
      cur = self.map[i][j]

    logging.debug('[{0}] next: {1} -> {2} {3}'.format(cur, dir, self.dir, self.pos))

    if cur == 'E':
      self.goal_found = True
    elif cur == 'S':
      self.start_found = True

    return dir

  """ calculate the shortest path on runner's map """
  def get_shortest_path(self) -> list:
    return bfs(self.map)
