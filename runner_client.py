import logging
import sys, argparse

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

  """ main task for runner """
  def run(self):
    self.channel.send("Start")

    cur = '?'
    while cur != 'S':
      surr = self._get3x3map()
      self.runner.update_map(surr)
      cur, motion = self.runner.get_next_move()
      self._request_move(motion)
      
    #while "UNTIL_THE_END_OF_EXPLORATION":
    while cur != 'E':
      surr = self._get3x3map()
      self.runner.update_map(surr)
      cur, motion = self.runner.get_next_move()
      if self.runner.get_exploring_status():
        break
      self._request_move(motion)

    self.channel.send("End")

    path = self.runner.get_shortest_path()
    self._request_evaluation(path)
    result = self.channel.receive()

    return result

  """ get surrounding 3x3 map """
  def _get3x3map(self):
    surr = self.channel.receive()
    return surr

  """ send move information to map server """
  def _request_move(self, motion: tuple):
    self.channel.send(motion)

  """ request an evaluation of the runner's shortest path """
  def _request_evaluation(self, path: list):
    self.channel.send(str(len(path)))
    for dir in path:
      self.channel.send(dir)


""" main """
def main(args):
  runner = RunnerClient()
  result = runner.run()

  if result == 'Incorrect':
    logging.info('Incorrect')
    sys.exit(1)

  logging.info('Correct')
  sys.exit(0)

def parse_args():
    parser = argparse.ArgumentParser(description="Tutorial code for on-boarding program.")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
  args = parse_args()
  logging.basicConfig(level=logging.INFO)
  main(args)
