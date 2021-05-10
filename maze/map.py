from maze import conversion

class Map:
  def __init__(self):
    self.pos = [0, 0]
    self.dir = 'N'
    self.map = []
    self.path = []

  """ map setter """
  def set_map(self, map_data: list):
    self.map = map_data

  """ calculate the shortest path """
  def calc_shortest_path(self):
    self.path = []

  """ get surrounding 3x3 map """
  def get3x3map(self) -> str:
    pos = self.pos
    dir = conversion.NESW.index(self.dir)
    surr = [self.map[i][j] for i in range(pos[0] - 1, pos[0] + 2) for j in range(pos[1] - 1, pos[1] + 2)]
    for _ in range(dir):
      surr = [surr[conversion.CW[i]] for i in range(9)]
    return ''.join(surr)

  """ update runner position per runner's message """
  def update_pos(self, cmd: str):
    if cmd == 'Start':
      self.pos = [1, 1]
      self.dir = 'N'
    else:
      new_nesw = (conversion.NESW.index(self.dir) + conversion.DIR.index(cmd)) % 4
      self.dir = conversion.NESW[new_nesw]
      self.pos = [sum(x) for x in zip(self.pos, conversion.STEPS[new_nesw])]

  """ check if a runner's path is the shortest path """
  def evaluate_path(self, path: list) -> str:
    return False
