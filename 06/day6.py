import sys

DAYS = 256

def main():
  states = []
  for line in sys.stdin:
    states = list(map(int, line.split(",")))

  counts = [0] * 9
  for state in states:
    counts[state] += 1

  for day in range(DAYS):
    counts[(day + 7) % 9] += counts[day % 9]
  print(sum(counts))

if __name__ == "__main__":
  main()
