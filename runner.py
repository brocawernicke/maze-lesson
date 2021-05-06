class Channel:
  def __init__(self):
    self.buf = []

  def receive(self):
    return self.buf

  def send(self, buf):
    self.buf = buf


class Runner:
  def __init__(self):
    self.pos = {'x': 0, 'y': 0, 'dir': 'N'}
    self.map = []

  def updateMap(self):
    self.map = []

  def getNextMove(self):
    return None

  def getShortestPath(self):
    return []


class RunnerClient:
  def __init__(self):
    self.runner = Runner()
    self.channel = Channel()
    self.sendCmd("Start")

  def task(self):
    while "THE_END_OF_EXPLORATION":
      surroundings = self.get3x3map()
      self.runner.updateMap(surroundings)
      motion = self.runner.getNextMove()
      self.requestMove(motion)

    path = self.runner.getShortestPath()
    self.requestEvaluation(path)

  def get3x3map(self):
    surroundings = self.channel.receive()
    return surroundings

  def requestMove(self, motion):
    self.channel.send(motion)
    