import logging
import argparse

from channel.pipe import Channel
from maze.map import Map

class MazeServer:
  def __init__(self):
    self.map = Map()
    self.channel = Channel("/tmp/to.maze", "/tmp/to.runner")
    self.channel.open()
    logging.debug('Open named pipe')

  def __exit__(self):
    self.channel.close()
    return True

  """ Loading map from a file """
  def load_map(self, file_name: str):
    buf = []
    with open(file_name, "r") as file:
      rows, cols = map(int, file.readline().rstrip().split())
      for _ in range(rows):
        buf.append(file.readline().rstrip())
    self.map.set_map(buf)
    logging.info('Succeeded loading {0}x{1} map: "{2}"'.format(rows, cols, file_name))
    self.map.calc_shortest_path()

  """ Map exploring mode """
  def exploring_mode(self):
    while True:
      cmd = self.channel.listen()
      if cmd == "End":
        break
      self.map.update_pos(cmd)
      surr = self.map.get3x3map()
      self.channel.send(surr)

  """ Path evaluation mode """
  def evaluation_mode(self):
    path = []
    step_num = int(self.channel.receive())
    for _ in range(step_num):
      path.append(self.channel.receive())
    if self.map.evaluate_path(path) == True:
      logging.debug('Correct')
      self.channel.send('Correct')
    else:
      logging.debug('Incorrect')
      self.channel.send('Incorrect')


""" main """
def main(args):
  server = MazeServer()

  server.load_map(args.map_file[0])
  server.exploring_mode()
  server.evaluation_mode()

def parse_args():
    parser = argparse.ArgumentParser(description="Tutorial code for on-boarding program.")
    parser.add_argument("map_file", nargs=1, help="map file to load")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
  args = parse_args()
  logging.basicConfig(level=logging.INFO)
  main(args)
