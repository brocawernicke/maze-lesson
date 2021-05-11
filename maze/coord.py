DIR = ['Forward', 'Right', 'Backward', 'Left']
NESW = 'NESW'
STEPS = [[-1, 0], [0, 1], [1, 0], [0, -1]]
CCW = [6, 3, 0, 7, 4, 1, 8, 5, 2]
CW = [2, 5, 8, 1, 4, 7, 0, 3, 6]

def num2dir(num: int) -> str:
  return DIR[num]

def dir2num(dir: str) -> int:
  return DIR.index(dir)

def num2card(num: int) -> str:
  return NESW[num]

def card2num(card: str) -> int:
  return NESW.index(card)

def steps(num: int) -> list:
  return STEPS[num]

def cw3x3(m: str) -> str:
  return [m[CW[i]] for i in range(9)]

def ccw3x3(m: list) -> list:
  return [m[CCW[i]] for i in range(9)]
