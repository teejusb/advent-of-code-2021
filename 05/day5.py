import sys

SIZE = 999

def main(part_two):
  grid = [[0 for i in range(SIZE)] for j in range(SIZE)]
  lines = []
  for line in sys.stdin:
    start, end = line.split(" -> ")
    x1, y1 = map(int, start.split(","))
    x2, y2 = map(int, end.split(","))

    if y2 == y1:
      if x1 > x2:
        x1, y1, x2, y2, = x2, y2, x1, y1
      for i in range(x1, x2 + 1):
        grid[i][y1] += 1

    elif x2 == x1:
      if y1 > y2:
        x1, y1, x2, y2, = x2, y2, x1, y1
      for i in range(y1, y2 + 1):
        grid[x1][i] += 1

    elif part_two:
      if x1 > x2:
        x1, y1, x2, y2, = x2, y2, x1, y1
      m1 = y2 - y1
      m2 = x2 - x1
      for i in range(x1, x2 + 1):
        # Works for all lines (not just 45 degrees).
        y = m1 * i + (m2 * y1 - m1 * x1)
        if y % m2 == 0:
          j = int(y/m2)
          if 0 <= j and j <= SIZE - 1:
            grid[i][j] += 1

  count = 0
  for row in grid:
    for cell in row:
      if cell >= 2:
        count += 1
  print(count)

if __name__ == "__main__":
  main(False)
