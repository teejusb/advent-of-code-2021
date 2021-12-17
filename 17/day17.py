import re
import sys

PATTERN = r"target area: x=(-?[\d]+)\.\.(-?[\d]+), y=(-?[\d]+)\.\.(-?[\d]+)"

def triangular_number(x):
  return int((x*(x+1))/2)

def main():
  for line in sys.stdin:
    match = re.search(PATTERN, line)
    x1, x2, y1, y2 = map(int, match.groups())

  max_y = 0
  count = 0
  for x in range(x2+1):
    for y in range(y1, -y1):
      pos_x, pos_y = 0, 0
      cur_x, cur_y = x, y
      while pos_x <= x2 and y1 <= pos_y:
        pos_x += cur_x
        pos_y += cur_y

        cur_x = max(0, cur_x - 1)
        cur_y -= 1
        if x1 <= pos_x and pos_x <= x2 and y1 <= pos_y and pos_y <= y2:
          max_y = max(max_y, triangular_number(y))
          count += 1
          break
  print((max_y, count))
    
if __name__ == "__main__":
  main()
