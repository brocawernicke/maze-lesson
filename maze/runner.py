from maze import conversion

class Runner:
  def __init__(self):
    self.pos = [1, 1]
    self.dir = 'N'
    self.map = [[0 for _ in range(10)] for _ in range(10)]

  """ update runner's imaginary map per 3x3 map """
  def update_map(self, surr: str):
    for i in range(-1, 2):
      for j in range(-1, 2):
        self.map[self.pos[0]+i][self.pos[1]+j] = surr[(i+1)*3+(j+1)]

  """ calculate a next moving direction """
  def get_next_move(self) -> str:
    dir = 'Forward'
    i, j = self.pos[0], self.pos[1]
    if self.map[i-1][j] == 'O':
      self.pos[0] -= 1
      dir = conversion.DIR[-conversion.NESW.index(self.dir)]
      self.dir = 'N'
    elif self.map[i][j+1] == 'O':
      self.pos[1] -= 1
      dir = conversion.DIR[1 - conversion.NESW.index(self.dir)]
      self.dir = 'E'
    elif self.map[i+1][j] == 'O':
      self.pos[0] += 1
      dir = conversion.DIR[2 - conversion.NESW.index(self.dir)]
      self.dir = 'S'
    elif self.map[i][j-1] == 'O':
      self.pos[1] -= 1
      dir = conversion.DIR[3 - conversion.NESW.index(self.dir)]
      self.dir = 'W'
    return dir

  """ calculate the shortest path on runner's map """
  def get_shortest_path(self) -> list:
    return []
