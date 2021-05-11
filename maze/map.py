import logging

from maze import coord
from maze.bfs import bfs

class Map:
  def __init__(self):
    self.pos = [0, 0]
    self.dir = 'N'
    self.map = []
    self.path = []

  """ map setter """
  def set_map(self, map_data: list):
    self.map = map_data
    self._find_R()
    for i in range(len(self.map)):
      logging.debug('{0}'.format(self.map[i]))

  """ calculate the shortest path """
  def calc_shortest_path(self):
    self.path = bfs(self.map)
    logging.debug('{0}'.format(self.path))

  """ get surrounding 3x3 map """
  def get3x3map(self) -> str:
    row, col = self.pos[0], self.pos[1]
    dir = coord.card2num(self.dir)
    surr = [self.map[i][j] for i in [row-1, row, row+1] for j in [col-1, col, col+1]]
    for _ in range(dir):
      surr = coord.cw3x3(surr)
    return ''.join(surr)

  """ update runner position per runner's message """
  def update_pos(self, cmd: str):
    if cmd == 'Start':
      self._find_R()
      return

    new_nesw = (coord.card2num(self.dir) + coord.dir2num(cmd)) % 4

    logging.debug('move: {0} {1} ({2}+{3})'.format(self.dir, new_nesw, coord.card2num(self.dir), coord.dir2num(cmd)))

    self.dir = coord.num2card(new_nesw)
    self.pos = [sum(x) for x in zip(self.pos, coord.steps(new_nesw))]

    logging.debug('{0}'.format(self.pos))

  """ check if a runner's path is the shortest path """
  def evaluate_path(self, path: list) -> str:
    return self.path == path

  """ find initial position """
  def _find_R(self):
    self.dir = 'N'
    for i in range(len(self.map)):
      for j in range(len(self.map[0])):
        if self.map[i][j] == 'R':
          self.pos = [i, j]
          return
