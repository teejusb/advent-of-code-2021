import sys

from operator import add

def part1():
  n = 0
  ones = []
  for line in sys.stdin:
    input_list = list(map(int, list(line.strip())))
    if not ones:
      ones = input_list
    else:
      ones = list(map(add, ones, input_list))
    n += 1
  gamma = int(''.join(['1' if i > n/2 else '0' for i in ones]), 2)
  epsilon = int(''.join(['0' if i > n/2 else '1' for i in ones]), 2)
  print(gamma * epsilon)

def part2():
  n = 0
  o = []
  co = []
  for line in sys.stdin:
    s = line.strip()
    n = len(s)
    o.append(s)
    co.append(s)

  def func(i, match):
    return lambda s: s[i] == match

  for i in range(n):
    if len(o) == 1:
      break
    count = 0
    for s in o:
      count = count + 1 if s[i] == '1' else count
    o = filter(func(i, '1' if count*2 >= len(o) else '0'), o)

  for i in range(n):
    if len(co) == 1:
      break
    count = 0
    for s in co:
      count = count + 1 if s[i] == '1' else count
    co = filter(func(i, '0' if count*2 >= len(co) else '1'), co)

  print(int(o[0], 2) * int(co[0], 2))

if __name__ == "__main__":
  part2()
