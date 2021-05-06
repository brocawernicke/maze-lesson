class Maze:
  pos, dir, map, path
  def setMap():
  def move():
  def get3x3map():
  def calcShortestPath():

class MazeServer(Maze):
  def readMap():
    maze.getMap()
  def task():
    getCmd()
    maze.move()
    maze.get3x3map()
    sendCmd()
  def evaluation():
    getPath()
    sendResult()

class Runner:
  pos, dir, map, path
  def getNextMove():
  def updateMap():
  def calcShortestPath():

class RunnerClient(Runner):
  def task():
    runner.getNextMove()
    server.get3x3map()
    runner.updateMap()
  def get3x3map():
  def evaluation():
    runner.getPath()
    server.sendPath()