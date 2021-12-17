import sys

def triangular_number(x):
  return int((x*(x+1))/2)

def main(part_two):
  pos = []
  for line in sys.stdin:
    pos = list(map(int, line.split(",")))

  largest = max(pos)

  ans = sys.maxsize
  for i in range(largest + 1):
    total = 0
    for val in pos:
      if not part_two:
        total += abs(val - i)
      else:
        total += triangular_number(abs(val-i))
    ans = min(ans, total)
  print(ans)

if __name__ == "__main__":
  main(True)
