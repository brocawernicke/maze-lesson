import argparse

from channel.pipe import Channel
from maze.runner import Runner

class RunnerClient:
  def __init__(self):
    self.runner = Runner()
    self.channel = Channel()
    self.channel.open("/tmp/to.runner", "/tmp/to.maze")

  def __exit__(self):
    self.channel.close()
    return True

  def run(self):
    self.channel.send("Start")

    #while "UNTIL_THE_END_OF_EXPLORATION":
    for _ in range(5):
      surr = self._get3x3map()
      self.runner.update_map(surr)
      motion = self.runner.get_next_move()
      self._request_move(motion)
      
    self.channel.send("End")

    path = self.runner.get_shortest_path()
    self._request_evaluation(path)

  def _get3x3map(self):
    surr = self.channel.receive()
    return surr

  def _request_move(self, motion: tuple):
    self.channel.send(motion)

  def _request_evaluation(self, path: list):
    self.channel.send(str(len(path)))
    for dir in path:
      self.channel.send(dir)

def parse_args():
    parser = argparse.ArgumentParser(description="Tutorial code for on-boarding program.")
    args = parser.parse_args()
    return args

def main(args):
  runner = RunnerClient()
  runner.run()

if __name__ == "__main__":
  args = parse_args()
  main(args)
