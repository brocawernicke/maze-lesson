DIR = {'Forward': 0, 'Right': 1, 'Backward': 2, 'Left': 3}
NESW = 'NESW'
STEPS = [[1,0], [0,1], [-1,0], [0,-1]]
CW = [6,3,0,7,4,1,8,5,2]

class Map:
  def __init__(self):
    self.pos = [0, 0]
    self.dir = 'N'
    self.map = []
    self.path = []

  def set_map(self, map_data: list):
    self.map = map_data

  def calc_shortest_path(self):
    self.path = []

  def get3x3map(self) -> str:
    pos = self.pos
    dir = NESW.index(self.dir)
    surr = [self.map[i][j] for i in range(pos[0] - 1, pos[0] + 2) for j in range(pos[1] - 1, pos[1] + 2)]
    for _ in range(dir):
      surr = [surr[CW[i]] for i in range(9)]
    return ''.join(surr)

  def update_pos(self, cmd: str):
    if cmd == 'Start':
      self.pos = [1, 1]
      self.dir = 'N'
    else:
      new_nesw = (NESW.index(self.dir) + DIR[cmd]) % 4
      self.dir = NESW[new_nesw]
      self.pos = [sum(x) for x in zip(self.pos, STEPS[new_nesw])]

  def evaluate_path(self, path: list) -> str:
    return False
