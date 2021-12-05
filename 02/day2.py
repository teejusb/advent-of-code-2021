import sys

from operator import add

def part1():
  commands = {
      "forward": [1, 0],
      "down" : [0, 1],
      "up": [0, -1],
  }

  pos = [0, 0]

  for line in sys.stdin:
    command, val = line.split()
    for i in range(len(pos)):
      pos[i] += commands[command][i] * int(val)
  print(pos[0] * pos[1])

def part2():
  commands = {
      "forward": lambda p,v: [v, p[2] * v, 0],
      "down" : lambda p,v: [0, 0, v],
      "up": lambda p,v: [0, 0, -v],
  }

  pos = [0, 0, 0]

  for line in sys.stdin:
    command, val = line.split()
    pos = list(map(add, pos, commands[command](pos, int(val))))
  print(pos[0] * pos[1])

if __name__ == "__main__":
  part2()
