class Channel:
  def __init__(self):
    self.buf = []

  def receive(self):
    return self.buf

  def send(self, buf):
    self.buf = buf

  def listen(self):
    return self.buf


class Maze:
  def __init__(self):
    self.pos = {'x': 0, 'y': 0, 'dir': 'N'}
    self.map = []
    self.path = []

  def setMap(self, mapData):
    self.map = mapData

  def calcShortestPath(self):
    self.path = []

  def get3x3map(self):
    return self.map

  def updatePos(self, dir):
    self.pos = {}

  def evaluatePath():
    return False


class MazeServer:
  def __init__(self):
    self.maze = Maze()
    self.channel = Channel()

  def readMap(self):
    self.maze.setMap()

  def exploringMazeMode(self):
    while True:
      cmd = self.channel.listen()
      if (cmd == "End"):
        break
      self.maze.updatePos(cmd)
      surroundings = self.maze.get3x3map()
      self.channel.send(surroundings)

  def evaluationPathMode(self):
    path = []
    step_num = self.channel.read()
    for _ in range(step_num):
      path.append(self.channel.read())
    self.maze.evaluationPath(path)

if __name__ == "__main__":
  server = MazeServer()

  server.readMap()
  server.exploringMazeMode()
  server.evaluationPathMode()
  